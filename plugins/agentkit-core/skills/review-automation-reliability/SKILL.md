---
name: review-automation-reliability
description: >
  Use when an automation should be reviewed for trigger quality, retries, idempotency, exception handling and fallback.
---
# Review Automation Reliability
Compose:
trigger-quality-checker → idempotency-checker → retry-policy-checker → automation-exception-router → manual-fallback-builder.
