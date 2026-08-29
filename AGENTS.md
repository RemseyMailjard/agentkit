# AGENTS.md

## Repository purpose

AgentKit is the Skills4-IT Codex plugin marketplace.

## Contribution rules

- Keep skills small and task-focused.
- Prefer capability-first design over endpoint mirroring.
- Add or update eval cases whenever routing behavior changes.
- Separate review from remediation unless a workflow explicitly requires both.
- Do not weaken security controls or tests to make generated code appear successful.
- Do not claim commands/tests were executed unless execution evidence exists.
- Keep plugin manifests and repository URLs current.

## MCP Builder quality bar

Every new MCP Builder skill should define:

1. when it should be used;
2. when it should not be used or what neighboring skill is preferable;
3. a repeatable workflow;
4. safety or side-effect considerations;
5. a concrete output contract;
6. at least one eval case.
