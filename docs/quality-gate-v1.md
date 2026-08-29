# AgentKit Quality Gate v1

AgentKit Quality Gate v1 turns the repository's existing checks into one deterministic release-oriented pipeline.

## Gate

A commit passes when:

1. `scripts/validate_agentkit.py` passes.
2. Runtime routing smoke cases pass against deterministic fixtures.
3. The official OpenAI `plugin-eval analyze` command completes for MCP Builder.
4. MCP Builder scores at least **80/100**.
5. MCP Builder has **0 hard Plugin Eval failures**.
6. The MCP Builder benchmark fixture/assets are structurally present and Python fixtures compile.

## Deliberately excluded

The gate does **not** require:

- OpenAI API keys;
- Codex CLI installation;
- ChatGPT/Codex login;
- live `codex exec`;
- paid model calls.

Live semantic benchmarking remains an optional future release-quality layer.

## Why 80?

MCP Builder currently measured 86/100 after its first remediation cycle. A floor of 80 prevents structural/budget regressions while leaving room for evaluator-version changes and future iterative improvement.

## Output

The workflow publishes:

- MCP Builder official Plugin Eval report;
- fixture runtime eval JSON;
- fixture runtime eval Markdown;
- GitHub job summary.

## Next evolution

Quality Gate v2 can add per-plugin official Plugin Eval thresholds as the other AgentKit plugins are hardened using the same measurement/remediation loop.
