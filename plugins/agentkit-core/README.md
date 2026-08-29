# AgentKit Core v2.4.1

Skills solve user tasks. Micro-tools solve one narrow reasoning operation.
Shared context files hold personal/organizational operating principles so
Skills and micro-tools stay compact instead of duplicating instructions.

## Scale

- 119 Skills (see `evals/agentkit-core/cases.json` for the full routing set)
- 299 micro-tools under `micro-tools/`, each with a single responsibility,
  an output contract and an explicit boundary (see `micro-tools/README.md`)
- 24 shared context files under `context/` (engineering, consultancy,
  training, decision, delivery, product, sales and personal-os principles)

## Skill categories

- **review-*** (21) — assess an existing artifact (code, agent design,
  training content, security posture, ...) without changing it
- **design-*** (19) — architect a new solution, integration or rollout
- **prepare-*** (11) — package context, briefs or approvals for handoff
- **assess-*** (8) — score readiness or opportunity
- **build-*** (6) — construct a concrete deliverable (module, runbook,
  context, test plan)
- **plan-*** / **analyze-*** (4 each) — sequence work or interpret signals
  before deciding
- everything else — prioritize, audit, shape, run, qualify, optimize,
  manage, close and a handful of one-off workflows

## Core design rule

Micro-tools are internal and composable, not marketplace entry points
(see `docs/agentkit-core-microtools-v0.1.md`). A curated subset is also
published as standalone Agent Skills for ChatGPT Work — see
`docs/agentkit-core-chatgpt-skills-v0.1.md`.

## Registration

Registered in `.agents/plugins/marketplace.json` as `agentkit-core`.
