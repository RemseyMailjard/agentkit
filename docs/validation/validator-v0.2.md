# AgentKit Validator v0.2

Validator v0.2 turns the initial static checker into a stronger repository quality gate.

## Added in v0.2

### Version consistency

- plugin versions must use semantic versioning;
- plugin changelogs are checked for a matching current version where present.

### Skill-to-eval coverage

Every non-scaffold plugin skill must appear in at least one eval expectation.

This prevents adding a new skill without any routing coverage.

### Cross-plugin reference validation

`evals/cross-plugin/cases.json` is checked against the actual marketplace:

- expected plugin names must exist;
- expected skill names must exist.

This catches stale routing tests after renames or restructuring.

### Golden workflow validation

At least one golden workflow must exist.

Each workflow must contain:

- a `README.md`;
- a stated goal;
- acceptance criteria or acceptance language.

### Platform docs

The core platform files are now blocking requirements:

- `README.md`
- `AGENTS.md`
- `docs/architecture.md`
- `docs/routing-matrix.md`
- `docs/plugin-contract.md`

### Better CI output

GitHub Actions writes the validator output into the workflow summary.

## Local use

```bash
python scripts/validate_agentkit.py
```

## Validation philosophy

The validator checks repository consistency.

It still does **not** claim semantic routing correctness or actual plugin execution.
Those belong to runtime evals and end-to-end tests.
