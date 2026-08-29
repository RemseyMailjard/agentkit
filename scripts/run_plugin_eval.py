#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
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
        "plugin-eval CLI not found. Set OPENAI_PLUGINS_DIR to an openai/plugins checkout."
    )

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("plugin", choices=[
        "mcp-builder", "dotnet-reviewer", "lab-generator",
        "training-creator", "onenote"
    ])
    parser.add_argument("--format", default="markdown",
                        choices=["markdown", "json", "html"])
    args = parser.parse_args()
    cmd = find_plugin_eval_cli() + [
        "analyze", f"plugins/{args.plugin}", "--format", args.format
    ]
    print("$", " ".join(cmd))
    return subprocess.run(cmd, cwd=ROOT).returncode

if __name__ == "__main__":
    raise SystemExit(main())
