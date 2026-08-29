# Official OpenAI Plugin Eval Integration

AgentKit uses OpenAI's official `plugin-eval` as the plugin-wide benchmark layer.

## Current official behavior

As documented by OpenAI, `plugin-eval` is both a local Node.js CLI and a Codex plugin.
It requires Node.js 20 or newer. The package is currently private, so the expected
usage is from a local checkout or linked command rather than npm installation.

The official CLI supports:

```text
plugin-eval analyze <path>
plugin-eval explain-budget <path>
plugin-eval measurement-plan <path>
plugin-eval init-benchmark <path>
plugin-eval benchmark <path>
plugin-eval report <result.json>
plugin-eval compare <before.json> <after.json>
```

The deterministic commands are local-first. The live `benchmark` command runs real
`codex exec` sessions in isolated temporary workspaces and stores artifacts under
`.plugin-eval/`.

## AgentKit integration layers

```text
AgentKit static validator
        ↓
AgentKit routing eval harness
        ↓
Codex routing adapter
        ↓
Official OpenAI plugin-eval
        ↓
Golden workflow acceptance
        ↓
Release decision
```

These layers are complementary:

- AgentKit validator checks repository consistency.
- AgentKit routing evals check our expected plugin/skill routing contract.
- Codex adapter checks live routing behavior.
- OpenAI plugin-eval evaluates a plugin/skill as a broader Codex artifact.
- Golden workflows validate end-to-end business outcomes.

## First benchmark target

`plugins/mcp-builder`

Use:

```bash
python scripts/run_plugin_eval_mcp_builder.py analyze
python scripts/run_plugin_eval_mcp_builder.py init-benchmark
python scripts/run_plugin_eval_mcp_builder.py benchmark --dry-run
```

Live benchmark execution should only be enabled after Codex CLI authentication and
benchmark configuration are reviewed.

## CI

`.github/workflows/mcp-builder-plugin-eval.yml` is manual-only.

It checks out the official `openai/plugins` repository at runtime and uses its
`plugins/plugin-eval/scripts/plugin-eval.js` directly.

v0.1 intentionally does not make live benchmarks a merge/release gate.
