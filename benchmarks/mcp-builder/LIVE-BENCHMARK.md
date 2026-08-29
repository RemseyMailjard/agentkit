# MCP Builder Live Benchmark v0.1

This patch adds a real OpenAI `plugin-eval` benchmark configuration for MCP Builder.

## Official schema used

The benchmark template follows the current OpenAI schema:

- `kind: plugin-eval-benchmark`
- `schemaVersion: 2`
- `runner.type: codex-cli`
- workspace copy provisioning
- target provisioning
- verifier commands
- plain-language scenarios and success checklists

The runner materializes the workspace path at execution time so the configuration stays portable.

## Benchmark workspace

`benchmarks/workspaces/mcp-builder-customer-support/`

It contains:
- a small Customer Support OpenAPI contract;
- an intentionally insecure MCP-style Python server;
- an unrelated C# file for boundary testing.

## Scenarios

1. **Build** — capability-first customer support MCP implementation plus tests.
2. **Review/Security** — evidence-backed review without modifying code.
3. **Boundary** — decline/handoff an ordinary .NET review request instead of forcing MCP Builder.

## Why only three scenarios

These are intentionally high-signal first measurements. More scenarios should be added only after we inspect actual Codex traces, token usage and failure modes.

## Important CI constraint

The supplied GitHub workflow verifies that the `codex` CLI exists before running.

A standard GitHub-hosted runner may not have Codex installed/authenticated. If that check fails, that is an environment/setup failure, not an MCP Builder benchmark failure.

## Result artifacts

OpenAI plugin-eval writes run artifacts below:

`plugins/mcp-builder/.plugin-eval/runs/<timestamp>/`

When Codex emits token usage, it also writes:

`plugins/mcp-builder/.plugin-eval/benchmark-usage.jsonl`

That usage file can be fed back into `plugin-eval analyze --observed-usage`.
