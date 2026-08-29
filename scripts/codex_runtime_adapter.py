#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shlex
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

ROUTING_INSTRUCTION = """
You are evaluating AgentKit routing only.

Given the user request below, determine which AgentKit plugin(s) and skill(s)
should be selected. Do not execute the requested task. Do not review code, create
artifacts, or solve the domain problem.

Return exactly one JSON object and no markdown:

{
  "actual_plugins": ["plugin-name"],
  "actual_skills": ["skill-name"]
}

Use only plugin and skill names that exist in this workspace marketplace.

User request:
{prompt}
""".strip()

def extract_json(text: str) -> dict[str, Any]:
    text = text.strip()
    try:
        value = json.loads(text)
        if isinstance(value, dict):
            return value
    except json.JSONDecodeError:
        pass

    for line in reversed(text.splitlines()):
        line = line.strip()
        if not line:
            continue
        try:
            value = json.loads(line)
            if isinstance(value, dict):
                return value
        except json.JSONDecodeError:
            continue

    start = text.rfind("{")
    end = text.rfind("}")
    if start >= 0 and end > start:
        candidate = text[start:end+1]
        value = json.loads(candidate)
        if isinstance(value, dict):
            return value

    raise ValueError("Codex output did not contain a parseable JSON object.")

def normalize_names(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [x for x in value if isinstance(x, str)]
    raise ValueError("Routing fields must be a string or array of strings.")

def run_codex(prompt: str, codex_bin: str, model: str | None, extra_args: list[str]) -> dict[str, Any]:
    eval_prompt = ROUTING_INSTRUCTION.format(prompt=prompt)

    cmd = [codex_bin, "exec"]
    if model:
        cmd.extend(["--model", model])
    cmd.extend(extra_args)
    cmd.append(eval_prompt)

    completed = subprocess.run(
        cmd,
        cwd=ROOT,
        capture_output=True,
        text=True,
        env=os.environ.copy(),
    )

    raw = (completed.stdout or "") + (completed.stderr or "")
    if completed.returncode != 0:
        raise RuntimeError(
            f"codex exec failed with exit code {completed.returncode}: {raw.strip()}"
        )

    parsed = extract_json(completed.stdout or "")
    plugins = normalize_names(parsed.get("actual_plugins"))
    skills = normalize_names(parsed.get("actual_skills"))

    return {
        "actual_plugins": plugins,
        "actual_skills": skills,
        "_adapter": {
            "runner": "codex-exec",
            "model": model,
            "command": " ".join(shlex.quote(x) for x in cmd[:-1]) + " <routing-prompt>",
        },
    }

def main() -> int:
    parser = argparse.ArgumentParser(
        description="AgentKit Codex adapter for the runtime eval harness."
    )
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--id", default="")
    parser.add_argument(
        "--codex-bin",
        default=os.environ.get("CODEX_BIN", "codex"),
        help="Codex CLI executable. Default: codex",
    )
    parser.add_argument(
        "--model",
        default=os.environ.get("AGENTKIT_EVAL_MODEL"),
        help="Optional Codex model override.",
    )
    parser.add_argument(
        "--extra-arg",
        action="append",
        default=[],
        help="Additional codex exec argument; repeat as needed.",
    )
    args = parser.parse_args()

    try:
        result = run_codex(
            prompt=args.prompt,
            codex_bin=args.codex_bin,
            model=args.model,
            extra_args=args.extra_arg,
        )
    except Exception as exc:
        print(
            json.dumps(
                {
                    "actual_plugins": [],
                    "actual_skills": [],
                    "error": str(exc),
                    "eval_id": args.id,
                },
                ensure_ascii=False,
            )
        )
        return 1

    result["eval_id"] = args.id
    print(json.dumps(result, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
