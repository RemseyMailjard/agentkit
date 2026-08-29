#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def find_plugin_eval_cli() -> list[str]:
    explicit = os.environ.get("PLUGIN_EVAL_CMD")
    if explicit:
        return explicit.split()

    if shutil.which("plugin-eval"):
        return ["plugin-eval"]

    checkout = os.environ.get("OPENAI_PLUGINS_DIR")
    if checkout:
        script = Path(checkout) / "plugins/plugin-eval/scripts/plugin-eval.js"
        if script.exists():
            return ["node", str(script)]

    raise FileNotFoundError(
        "plugin-eval CLI not found. Install/link it, or set OPENAI_PLUGINS_DIR "
        "to a checkout of https://github.com/openai/plugins."
    )

def run(cmd: list[str]) -> int:
    print("$", " ".join(cmd))
    completed = subprocess.run(cmd, cwd=ROOT)
    return completed.returncode

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run official OpenAI plugin-eval workflows against MCP Builder."
    )
    parser.add_argument(
        "mode",
        choices=["analyze", "init-benchmark", "benchmark"],
        help="Official plugin-eval command to run.",
    )
    parser.add_argument(
        "--format",
        default="markdown",
        choices=["markdown", "json", "html"],
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Pass --dry-run to plugin-eval benchmark.",
    )
    args = parser.parse_args()

    cli = find_plugin_eval_cli()
    target = "plugins/mcp-builder"

    if args.mode == "analyze":
        cmd = cli + ["analyze", target, "--format", args.format]
    elif args.mode == "init-benchmark":
        cmd = cli + ["init-benchmark", target]
    else:
        cmd = cli + ["benchmark", target, "--format", args.format]
        if args.dry_run:
            cmd.append("--dry-run")

    return run(cmd)

if __name__ == "__main__":
    raise SystemExit(main())
