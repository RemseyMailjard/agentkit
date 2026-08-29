# MCP Builder — Plugin Eval Benchmark Target

This folder documents the first official OpenAI `plugin-eval` benchmark target in AgentKit.

## Target

`plugins/mcp-builder`

## Why MCP Builder first

MCP Builder is the strongest current engineering plugin and already has:

- multiple specialized skills;
- routing evals;
- security and test skills;
- cross-plugin interactions;
- a golden training workflow that depends on MCP correctness.

## Official workflow

The OpenAI `plugin-eval` CLI currently supports:

```text
analyze
explain-budget
measurement-plan
init-benchmark
benchmark
report
compare
```

For MCP Builder, start with:

```bash
python scripts/run_plugin_eval_mcp_builder.py analyze
```

Then initialize the official benchmark configuration:

```bash
python scripts/run_plugin_eval_mcp_builder.py init-benchmark
```

Review the generated `.plugin-eval/` configuration before live execution.

Then perform a dry run:

```bash
python scripts/run_plugin_eval_mcp_builder.py benchmark --dry-run
```

Only after the configuration is reviewed and Codex CLI is installed/authenticated:

```bash
python scripts/run_plugin_eval_mcp_builder.py benchmark
```

## Benchmark scenarios to include

When `init-benchmark` creates the starter configuration, adapt it around these AgentKit cases:

1. Build a capability-first MCP server from an API.
2. Add one business capability to an existing MCP server.
3. Review MCP architecture without modifying code.
4. Review MCP-specific security.
5. Test protocol/backend failure behavior.
6. Reverse engineer an API into MCP capabilities.
7. Ambiguous GET endpoint: tool vs resource.
8. Review then remediate as separate stages.
9. .NET MCP security overlap with .NET Reviewer.
10. MCP training workflow where technical correctness is delegated to MCP Builder.

## Acceptance goals

The first benchmark is exploratory, not a release gate.

Capture:

- static plugin-eval score;
- strongest/weakest skills;
- suggested fixes;
- benchmark configuration;
- live benchmark pass/fail when available;
- observed routing/tool usage;
- any instability between repeated runs.

Do not claim live benchmark success unless `plugin-eval benchmark` actually ran.
