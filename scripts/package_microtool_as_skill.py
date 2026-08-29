#!/usr/bin/env python3
"""Convert AgentKit Core micro-tools into standalone Agent Skills spec bundles.

Reads plugins/agentkit-core/micro-tools/<name>/MICROTOOL.md and writes an
Agent-Skills-compliant distribution/chatgpt-skills/<name>/SKILL.md, so the
micro-tool can be uploaded to ChatGPT (or any Agent Skills client) as its own
skill, independent of the agentkit-core plugin's routing surface.

Descriptions are curated by hand in scripts/chatgpt_skill_descriptions.json
because routing quality depends on an explicit "what + when" sentence that a
generic template cannot produce reliably (see https://agentskills.io/specification).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MICRO_TOOLS_DIR = ROOT / "plugins" / "agentkit-core" / "micro-tools"
OUTPUT_DIR = ROOT / "distribution" / "chatgpt-skills"
DESCRIPTIONS_FILE = ROOT / "scripts" / "chatgpt_skill_descriptions.json"

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def load_descriptions() -> dict[str, str]:
    return json.loads(DESCRIPTIONS_FILE.read_text(encoding="utf-8"))


def read_title(body: str) -> str:
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return ""


def validate_name(name: str) -> None:
    if not NAME_RE.match(name):
        raise ValueError(
            f"'{name}' is not a valid Agent Skills name (lowercase, digits, "
            "single hyphens, no leading/trailing/double hyphen)"
        )
    if len(name) > 64:
        raise ValueError(f"'{name}' exceeds the 64-character name limit")


def build_skill_md(name: str, description: str, body: str) -> str:
    if not (1 <= len(description) <= 1024):
        raise ValueError(
            f"description for '{name}' is {len(description)} chars; must be 1-1024"
        )
    frontmatter = (
        "---\n"
        f"name: {name}\n"
        "description: >\n"
        f"  {description}\n"
        "metadata:\n"
        "  source: agentkit-core\n"
        f"  origin_path: plugins/agentkit-core/micro-tools/{name}/MICROTOOL.md\n"
        "---\n"
    )
    return frontmatter + "\n" + body.strip() + "\n"


def package_tool(name: str, descriptions: dict[str, str]) -> Path:
    validate_name(name)
    source = MICRO_TOOLS_DIR / name / "MICROTOOL.md"
    if not source.exists():
        raise FileNotFoundError(f"no MICROTOOL.md found for '{name}' at {source}")

    description = descriptions.get(name)
    if not description:
        raise ValueError(
            f"no curated description for '{name}' in {DESCRIPTIONS_FILE.name}; "
            "add one before packaging (routing quality depends on it)"
        )

    body = source.read_text(encoding="utf-8")
    title = read_title(body)
    skill_md = build_skill_md(name, description, body)

    out_dir = OUTPUT_DIR / name
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "SKILL.md").write_text(skill_md, encoding="utf-8", newline="\n")
    print(f"packaged {name!r} ({title}) -> {out_dir / 'SKILL.md'}")
    return out_dir


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "tools",
        nargs="*",
        help="micro-tool names to package; omit with --curated or --all",
    )
    parser.add_argument(
        "--curated",
        action="store_true",
        help="package every tool listed in scripts/chatgpt_skill_descriptions.json",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="package every micro-tool under plugins/agentkit-core/micro-tools/",
    )
    args = parser.parse_args()

    descriptions = load_descriptions()

    if args.all:
        names = sorted(p.name for p in MICRO_TOOLS_DIR.iterdir() if p.is_dir())
    elif args.curated:
        names = sorted(descriptions.keys())
    elif args.tools:
        names = args.tools
    else:
        parser.error("provide tool names, or pass --curated / --all")
        return 2

    errors = 0
    for name in names:
        try:
            package_tool(name, descriptions)
        except (FileNotFoundError, ValueError) as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            errors += 1

    if errors:
        print(f"{errors} tool(s) failed to package", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
