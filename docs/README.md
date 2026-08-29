# AgentKit Documentation

This directory contains durable product, architecture, evaluation, and operational
documentation for AgentKit. Repository entry points, legal files, changelogs, and
agent-specific instruction/context files intentionally remain at the repository root.

## Platform core

- [Architecture](architecture.md)
- [Routing matrix](routing-matrix.md)
- [Plugin contract](plugin-contract.md)
- [Codex installation](codex-installation.md)

These paths are part of the platform's validation and contribution conventions and
should remain stable unless the validator and all instruction files change together.

## Plugin architecture

- [.NET Reviewer](plugins/dotnet-reviewer.md)
- [Lab Generator](plugins/lab-generator.md)
- [Training Creator](plugins/training-creator.md)
- [Skills4-IT training methodology](skills4it-training-methodology.md)

## Evals and benchmarks

- [Runtime eval harness](evals/runtime-evals.md)
- [Codex runtime adapter](evals/codex-runtime-adapter.md)
- [Official OpenAI plugin-eval integration](evals/plugin-eval.md)
- [Plugin Eval remediation v0.1](evals/plugin-eval-remediation-v0.1.md)
- [Live benchmark policy](evals/live-benchmark-policy.md)

## Validation and quality gates

- [Validation overview](validation/overview.md)
- [Validator v0.2](validation/validator-v0.2.md)
- [Quality Gate v1](validation/quality-gate-v1.md)
- [Platform Plugin Eval and Quality Gate v2](validation/platform-quality-gate-v2.md)

## Reference and plans

- [Technical specification](reference/technical-specification.md)
- [Eval suite expansion plan](plans/eval-suite-expansion.md)

## Files intentionally kept at the repository root

- `README.md`, `CHANGELOG.md`, `LICENSE`, `TERMS.md`, and `PRIVACY.md` are conventional
  repository entry-point, release, and legal files.
- `AGENTS.md`, `CLAUDE.md`, `INIT.md`, `AI-HANDOFF-CONTEXT.md`, and
  `codex-plugin-marketplace-ai-context.md` are agent instruction or context files whose
  root placement aids discovery and compatibility.
