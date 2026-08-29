# AGENTS.md

## Repository purpose

AgentKit is the Skills4-IT Codex plugin marketplace.

## Platform rules

- Prefer the smallest correct plugin/skill set.
- Do not invoke multiple plugins unless the request spans multiple responsibilities.
- Respect plugin ownership defined in `docs/routing-matrix.md`.
- Review before remediation unless the user asks for both.
- Never claim execution success without evidence.
- Keep durable knowledge separate from transient tasks.
- Add or update evals when routing behavior changes.
- Keep golden workflows representative of real end-to-end usage.

## Contribution requirements

Every new plugin or major skill change should update, where applicable:

- plugin manifest;
- README;
- changelog;
- evals;
- routing matrix;
- architecture docs;
- golden workflow if orchestration changes.

## Stability priority

Before expanding the marketplace, verify:

1. routing boundaries;
2. eval coverage;
3. documentation;
4. cross-plugin behavior.
