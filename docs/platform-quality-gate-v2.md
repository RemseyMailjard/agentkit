# AgentKit Platform Plugin Eval & Quality Gate v2

All AgentKit plugins are now measured by the official OpenAI `plugin-eval analyze` workflow.

## Blocking production plugins

These must score at least **80/100** and report **0 hard failures**:

- MCP Builder
- .NET Reviewer
- Lab Generator
- Training Creator

## Scaffold policy

OneNote is analyzed on every gate run and its report is preserved, but it is deliberately non-blocking while its own manifest describes it as a scaffold and MCP connectivity is intentionally incomplete.

## Common manifest remediation

The v2 patch also applies the structural lessons learned from MCP Builder to the remaining plugins:

- privacy policy URL;
- terms of service URL;
- exactly three default prompts;
- shorter interface descriptions;
- patch version bump to `0.1.1`.

## Gate flow

Structural validator → deterministic routing smoke → official Plugin Eval for all 5 plugins → thresholds for production plugins → OneNote scaffold report → benchmark asset validation.

No OpenAI API key, Codex login or live model execution is required.
