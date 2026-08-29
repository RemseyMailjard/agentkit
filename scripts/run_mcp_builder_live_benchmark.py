#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "plugins/mcp-builder"
TEMPLATE = TARGET / ".plugin-eval/benchmark.template.json"
RUNTIME = TARGET / ".plugin-eval/benchmark.runtime.json"
WORKSPACE = ROOT / "benchmarks/workspaces/mcp-builder-customer-support"

def plugin_eval_command() -> list[str]:
    explicit = os.environ.get("PLUGIN_EVAL_CMD")
    if explicit:
        return explicit.split()

    plugins_dir = os.environ.get("OPENAI_PLUGINS_DIR")
    if not plugins_dir:
        raise RuntimeError("OPENAI_PLUGINS_DIR is required.")

    script = Path(plugins_dir) / "plugins/plugin-eval/scripts/plugin-eval.js"
    if not script.exists():
        raise RuntimeError(f"plugin-eval script not found: {script}")

    return ["node", str(script)]

def materialize_config(model: str | None = None) -> Path:
    config = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    config["workspace"]["sourcePath"] = str(WORKSPACE.resolve())
    if model:
        config["runner"]["model"] = model
    RUNTIME.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    return RUNTIME

def main() -> int:
    parser = argparse.ArgumentParser(description="Run the real MCP Builder plugin-eval benchmark.")
    parser.add_argument("--model", default=os.environ.get("AGENTKIT_BENCHMARK_MODEL"))
    args = parser.parse_args()

    if not WORKSPACE.exists():
        print(f"Benchmark workspace not found: {WORKSPACE}", file=sys.stderr)
        return 2

    config = materialize_config(args.model)
    cmd = plugin_eval_command() + [
        "benchmark",
        str(TARGET),
        "--config",
        str(config),
        "--format",
        "markdown",
    ]

    print("$", " ".join(cmd))
    return subprocess.call(cmd, cwd=ROOT)

if __name__ == "__main__":
    raise SystemExit(main())
