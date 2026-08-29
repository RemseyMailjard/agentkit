---
name: assess-agent-readiness
description: >
  Use when an AI agent should be assessed for pilot or production readiness.
---
# Assess Agent Readiness
Compose:
agent-readiness-scorer → governance-gap-finder → agent-failure-mode-finder → observability-gap-finder → verification-planner.

Return READY / PILOT WITH RISKS / NOT READY, blockers, controls, eval gaps and next action.
