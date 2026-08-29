# AgentKit Runtime Eval Harness v0.1

This harness executes AgentKit routing eval cases against an interchangeable runner.

## Why this exists

The existing `evals/*/cases.json` files describe expected routing.

Static validation can prove that referenced plugin and skill names exist, but it
cannot prove that a runtime actually chooses them.

This harness adds that missing layer.

## Architecture

```text
cases.json
   ↓
Runtime Eval Harness
   ↓
Runner Adapter
   ├── fixture
   └── command
   ↓
Actual plugins + skills
   ↓
Expected vs actual
   ↓
results.json + results.md
```

## Fixture runner

The fixture runner is deterministic and is used only to test the harness itself.

```bash
python scripts/run_runtime_evals.py   --cases "evals/cross-plugin/cases.json"   --runner fixture   --fixtures evals/runtime/fixtures.json
```

It does **not** claim to test Codex routing.

## Command runner

The command runner connects the harness to a real external runtime.

The command must emit JSON:

```json
{
  "actual_plugins": ["training-creator", "lab-generator"],
  "actual_skills": ["design-training", "create-lab"]
}
```

Example shape:

```bash
python scripts/run_runtime_evals.py   --cases "evals/cross-plugin/cases.json"   --runner command   --command 'my-router --prompt "{prompt}"'
```

## Codex integration direction

OpenAI's official `plugin-eval` supports live Codex CLI benchmarking using
isolated temporary workspaces and `codex exec`.

AgentKit should use that as the live execution layer rather than reimplementing
Codex benchmarking.

A future adapter can therefore:

```text
AgentKit eval case
→ plugin-eval benchmark / codex exec
→ routing observation
→ AgentKit expected-vs-actual report
```

## Current scope

v0.1 validates:

- plugin selection;
- skill selection;
- exact set equality;
- machine-readable results;
- Markdown reports;
- CI smoke testing.

## Deliberate limitations

v0.1 does not yet:

- invoke Codex automatically;
- measure token usage;
- score semantic output quality;
- enforce skill execution order;
- validate generated artifacts;
- execute golden workflows end-to-end.

Those belong to later adapters and acceptance tests.
