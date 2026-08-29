---
name: design-event-driven-flow
description: >
  Use when a workflow may benefit from events, queues, asynchronous processing or decoupled integration.
---
# Design Event Driven Flow
Compose:
integration-pattern-selector → event-contract-checker → data-boundary-mapper → resilience-pattern-selector → dependency-mapper.

Return event model, producers/consumers, contracts, retry/idempotency, dead-lettering and observability.
