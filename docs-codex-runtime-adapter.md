# AgentKit Codex Runtime Adapter v0.1

This adapter connects the AgentKit runtime eval harness to the Codex CLI.

## Purpose

The static validator proves repository consistency.

The runtime harness proves expected-vs-actual comparison logic.

The Codex adapter adds the first real model-backed routing layer:

```text
AgentKit cases.json
→ runtime harness
→ Codex adapter
→ codex exec
→ actual plugin/skill routing
→ expected vs actual
→ PASS / FAIL
```

## Design decision

The adapter asks Codex to perform **routing only**.

It explicitly instructs the model not to execute the user's domain task. This keeps
routing evals cheap, focused and comparable.

## Run locally

Prerequisites:

- Codex CLI installed;
- Codex authenticated;
- AgentKit marketplace available in the workspace.

Run:

```bash
python scripts/run_codex_evals.py   --cases "evals/cross-plugin/cases.json"
```

Optional model override:

```bash
AGENTKIT_EVAL_MODEL=<model> python scripts/run_codex_evals.py
```

Optional Codex binary override:

```bash
CODEX_BIN=/path/to/codex python scripts/run_codex_evals.py
```

## Adapter contract

For every prompt, `scripts/codex_runtime_adapter.py` returns:

```json
{
  "actual_plugins": ["mcp-builder"],
  "actual_skills": ["review-mcp-server"]
}
```

The existing runtime harness compares these sets with the eval case expectations.

## CI status

`.github/workflows/codex-runtime-evals.yml` is deliberately manual-only in v0.1.

It should not become a blocking release gate until:

1. Codex CLI installation on the runner is standardized;
2. authentication is configured safely;
3. model/version selection is pinned;
4. cost and flakiness are understood;
5. repeated-run reliability is measured.

## Relationship with OpenAI plugin-eval

OpenAI's official `plugin-eval` is the preferred tool for full plugin benchmarking.
Its live `benchmark` command runs real `codex exec` sessions in isolated temporary
workspaces and preserves benchmark artifacts.

AgentKit's adapter has a narrower purpose: evaluate **AgentKit routing expectations**
from the existing `cases.json` files.

Recommended long-term stack:

```text
AgentKit static validator
→ AgentKit routing harness
→ Codex routing adapter
→ OpenAI plugin-eval for full plugin benchmarks
→ golden workflow acceptance tests
```

## What v0.1 does not claim

- it does not automatically install or authenticate Codex;
- it does not claim semantic quality of generated outputs;
- it does not execute golden workflows;
- it does not measure cost/tokens;
- it does not replace OpenAI plugin-eval.
