# Agent Memory Risk Checker
## Responsibility
Assess what should and should not be stored as durable AI memory.
## Check
PII, secrets, temporary state, permissions, staleness, provenance, user intent.
## Output
store / do not store / store with controls; reason; retention/provenance need.
## Boundary
Do not perform broader analysis, rewriting, or decisions outside this responsibility; return findings for the parent Skill to act on.
