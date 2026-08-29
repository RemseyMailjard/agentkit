#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import shlex
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run AgentKit runtime evals through the Codex adapter."
    )
    parser.add_argument("--cases", default="evals/cross-plugin/cases.json")
    parser.add_argument("--model", default=os.environ.get("AGENTKIT_EVAL_MODEL"))
    parser.add_argument("--json-out", default="evals/runtime/codex-results.json")
    parser.add_argument("--markdown-out", default="evals/runtime/codex-results.md")
    args = parser.parse_args()

    adapter_cmd = [
        "python",
        "scripts/codex_runtime_adapter.py",
        "--prompt",
        "{prompt}",
        "--id",
        "{id}",
    ]

    if args.model:
        adapter_cmd.extend(["--model", args.model])

    command_template = " ".join(shlex.quote(x) for x in adapter_cmd)

    cmd = [
        "python",
        "scripts/run_runtime_evals.py",
        "--cases",
        args.cases,
        "--runner",
        "command",
        "--command",
        command_template,
        "--json-out",
        args.json_out,
        "--markdown-out",
        args.markdown_out,
    ]

    return subprocess.call(cmd, cwd=ROOT)

if __name__ == "__main__":
    raise SystemExit(main())
