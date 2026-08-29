---
name: review-agent-design
description: >
  Use when an AI agent or agent workflow should be reviewed for responsibility boundaries, tool selection, side effects and human approval points.
---
# Review Agent Design
Compose:
agent-boundary-checker → tool-selection-auditor → agent-side-effect-classifier → approval-point-finder → human-escalation-designer.

Return boundary review, tool risks, approval points, escalation model and recommended changes.
