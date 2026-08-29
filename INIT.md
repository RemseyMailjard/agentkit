# AgentKit Workspace Init

Use this file as a compact session bootstrap. `AGENTS.md` remains the authoritative
repository instruction file; this document translates those rules into a practical
working sequence.

## Mission

AgentKit is the Skills4-IT Codex plugin marketplace. Its product is a set of small,
composable AI capabilities with testable routing:

```text
Marketplace -> Plugin -> Skill / workflow -> Concrete output
```

The important assets are plugin manifests, `SKILL.md` workflows, routing and quality
evals, architecture documentation, and representative golden workflows. This is not
a conventional application repository.

## Start every task

1. Read `AGENTS.md` and check `git status --short`; preserve unrelated user changes.
2. Use `README.md`, `docs/architecture.md`, and `docs/routing-matrix.md` to identify
   the smallest plugin and skill set that owns the request.
3. Read only the selected plugin's manifest, README, relevant skills, and eval suite.
4. Decide whether the request is review-only or also authorizes remediation.
5. State evidence accurately as inspected, inferred, generated, executed, or validated.

## Change impact map

| Change | Check or update |
|---|---|
| Skill behavior or routing | `SKILL.md`, plugin evals, `docs/routing-matrix.md` |
| New skill | Plugin manifest/README/changelog, eval coverage, routing and architecture docs |
| New plugin | Marketplace and plugin manifests, README/changelog, evals, routing matrix, architecture docs |
| Cross-plugin orchestration | Ownership per layer, cross-plugin evals, handoff contract, golden workflow |
| Validation/runtime tooling | Tooling docs, fixtures/evals, relevant GitHub workflow |

Do not expand the marketplace until routing boundaries, eval coverage, documentation,
and cross-plugin behavior are stable enough to support the addition.

## Validation

Run the static quality gate after repository changes:

```powershell
python scripts/validate_agentkit.py
```

When routing or runtime-eval behavior changes, also run the relevant eval suite. The
fixture-backed smoke command is documented in `docs-runtime-evals.md`; live Codex runs
are documented in `docs-codex-runtime-adapter.md` and require an available Codex CLI.

Before reporting completion, inspect `git diff --check` and `git diff`. Report exactly
which checks were run and whether they passed; never translate static inspection into
an execution claim.

## Durable versus transient context

Keep durable platform knowledge in repository documentation, plugin references, and
golden workflows. Keep task status, temporary findings, generated reports, and local
scratch data out of durable knowledge unless the task explicitly promotes them.
