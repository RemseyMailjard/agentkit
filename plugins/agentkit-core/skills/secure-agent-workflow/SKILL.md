---
name: secure-agent-workflow
description: >
  Use when an AI agent workflow needs a security review focused on untrusted content, memory, tool side effects and permission boundaries.
---
# Secure Agent Workflow
Compose:
prompt-injection-surface-finder → agent-memory-risk-checker → agent-side-effect-classifier → approval-point-finder → control-mapper.

Return trust boundaries, attack surfaces, memory risks, controls, residual risk and priorities.
