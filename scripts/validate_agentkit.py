#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []

SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")
FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)

def error(message: str) -> None:
    ERRORS.append(message)

def warn(message: str) -> None:
    WARNINGS.append(message)

def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        error(f"Missing JSON file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        error(f"Invalid JSON: {path.relative_to(ROOT)}:{exc.lineno}:{exc.colno} {exc.msg}")
    return None

def validate_marketplace() -> list[dict]:
    path = ROOT / ".agents/plugins/marketplace.json"
    data = load_json(path)
    if not isinstance(data, dict):
        return []

    if data.get("name") != "skills4it":
        warn("Marketplace name is expected to be 'skills4it'.")

    plugins = data.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        error("Marketplace must contain a non-empty 'plugins' array.")
        return []

    seen = set()
    for i, item in enumerate(plugins):
        prefix = f"marketplace.plugins[{i}]"
        if not isinstance(item, dict):
            error(f"{prefix} must be an object.")
            continue

        name = item.get("name")
        if not isinstance(name, str) or not name:
            error(f"{prefix}.name is required.")
            continue
        if name in seen:
            error(f"Duplicate marketplace plugin name: {name}")
        seen.add(name)

        source = item.get("source")
        if not isinstance(source, dict) or source.get("source") != "local":
            error(f"{prefix}.source must use local source.")
            continue

        rel_path = source.get("path")
        if not isinstance(rel_path, str) or not rel_path.startswith("./plugins/"):
            error(f"{prefix}.source.path must start with ./plugins/")
            continue

        plugin_dir = ROOT / rel_path[2:]
        if not plugin_dir.is_dir():
            error(f"Marketplace path does not exist: {rel_path}")

        expected = f"./plugins/{name}"
        if rel_path != expected:
            warn(f"Plugin '{name}' source path is '{rel_path}', expected '{expected}'.")

        policy = item.get("policy")
        if not isinstance(policy, dict):
            error(f"{prefix}.policy is required.")
        else:
            if policy.get("installation") not in {"AVAILABLE", "REQUIRED", "BLOCKED"}:
                warn(f"{prefix}.policy.installation has unexpected value.")
            if "authentication" not in policy:
                warn(f"{prefix}.policy.authentication is not defined.")

    return plugins

def validate_frontmatter(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    rel = path.relative_to(ROOT)

    if not match:
        error(f"Missing YAML-style frontmatter in {rel}")
        return

    fm = match.group(1)
    name_match = re.search(r"(?m)^name:\s*(.+?)\s*$", fm)
    description_match = re.search(r"(?m)^description:\s*(?:>\s*)?(.*)$", fm)

    if not name_match:
        error(f"Missing frontmatter 'name' in {rel}")
    else:
        declared = name_match.group(1).strip().strip("'\"")
        folder = path.parent.name
        if declared != folder:
            warn(f"Skill name '{declared}' does not match folder '{folder}' in {rel}")

    if not description_match:
        error(f"Missing frontmatter 'description' in {rel}")

def validate_plugin(item: dict) -> None:
    name = item.get("name")
    source = item.get("source", {})
    rel_path = source.get("path")
    if not isinstance(name, str) or not isinstance(rel_path, str):
        return

    plugin_dir = ROOT / rel_path[2:]
    manifest_path = plugin_dir / ".codex-plugin/plugin.json"
    manifest = load_json(manifest_path)
    if not isinstance(manifest, dict):
        return

    if manifest.get("name") != name:
        error(f"{manifest_path.relative_to(ROOT)} name does not match marketplace name '{name}'.")

    version = manifest.get("version")
    if not isinstance(version, str) or not SEMVER.match(version):
        error(f"{manifest_path.relative_to(ROOT)} has invalid or missing semver version.")

    for field in ["description", "homepage", "repository", "license", "skills"]:
        if field not in manifest:
            error(f"{manifest_path.relative_to(ROOT)} missing required field '{field}'.")

    skills_rel = manifest.get("skills")
    if isinstance(skills_rel, str):
        skills_dir = plugin_dir / skills_rel
        if not skills_dir.exists():
            error(f"Skills path does not exist for {name}: {skills_rel}")
        else:
            skill_files = sorted(skills_dir.glob("*/SKILL.md"))
            if not skill_files:
                error(f"No SKILL.md files found for plugin {name}.")
            for skill in skill_files:
                validate_frontmatter(skill)

    mcp_rel = manifest.get("mcpServers")
    if isinstance(mcp_rel, str):
        mcp_path = plugin_dir / mcp_rel
        if not mcp_path.exists():
            error(f"MCP configuration path does not exist for {name}: {mcp_rel}")
        else:
            load_json(mcp_path)

    ui = manifest.get("interface")
    if not isinstance(ui, dict):
        warn(f"{manifest_path.relative_to(ROOT)} has no interface object.")
    else:
        for field in ["displayName", "shortDescription"]:
            if not ui.get(field):
                warn(f"{manifest_path.relative_to(ROOT)} interface.{field} is missing.")

def validate_eval_file(path: Path) -> None:
    data = load_json(path)
    if not isinstance(data, list):
        error(f"Eval file must contain an array: {path.relative_to(ROOT)}")
        return

    ids = set()
    for i, case in enumerate(data):
        prefix = f"{path.relative_to(ROOT)}[{i}]"
        if not isinstance(case, dict):
            error(f"{prefix} must be an object.")
            continue

        case_id = case.get("id")
        prompt = case.get("prompt")
        if not isinstance(case_id, str) or not case_id:
            error(f"{prefix}.id is required.")
        elif case_id in ids:
            error(f"Duplicate eval id '{case_id}' in {path.relative_to(ROOT)}")
        else:
            ids.add(case_id)

        if not isinstance(prompt, str) or not prompt.strip():
            error(f"{prefix}.prompt is required.")

        if "expected_skill" not in case and "expected_skills" not in case and "expected_plugins" not in case:
            warn(f"{prefix} has no expected routing field.")

        checks = case.get("quality_checks")
        if checks is not None and (not isinstance(checks, list) or not all(isinstance(x, str) for x in checks)):
            error(f"{prefix}.quality_checks must be an array of strings.")

def validate_evals() -> None:
    eval_root = ROOT / "evals"
    if not eval_root.exists():
        error("Missing evals directory.")
        return

    files = sorted(eval_root.glob("*/cases.json"))
    if not files:
        error("No eval cases.json files found.")

    for path in files:
        validate_eval_file(path)

def validate_docs() -> None:
    for rel in ["README.md", "AGENTS.md", "docs/architecture.md", "docs/routing-matrix.md", "docs/plugin-contract.md"]:
        if not (ROOT / rel).exists():
            warn(f"Recommended platform file missing: {rel}")

def main() -> int:
    print("AgentKit Validator")
    print("==================")

    plugins = validate_marketplace()
    for plugin in plugins:
        validate_plugin(plugin)

    validate_evals()
    validate_docs()

    if WARNINGS:
        print("\nWarnings:")
        for item in WARNINGS:
            print(f"  - {item}")

    if ERRORS:
        print("\nErrors:")
        for item in ERRORS:
            print(f"  - {item}")
        print(f"\nFAILED: {len(ERRORS)} error(s), {len(WARNINGS)} warning(s)")
        return 1

    print(f"\nPASS: {len(plugins)} plugin(s), {len(WARNINGS)} warning(s)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
