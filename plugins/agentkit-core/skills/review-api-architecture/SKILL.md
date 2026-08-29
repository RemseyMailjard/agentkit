---
name: review-api-architecture
description: >
  Use when an existing API or integration architecture should be reviewed for boundaries, contracts, dependencies and operational risk.
---
# Review API Architecture
Compose:
service-boundary-checker → contract-quality-checker → dependency-risk-checker → resilience-pattern-selector → observability-gap-finder.

Return strengths, findings, operational risks, recommended changes and verification.
