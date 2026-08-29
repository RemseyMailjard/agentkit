---
name: review-fix-plan
description: >
  Use when a proposed technical fix should be assessed for regression risk, blast radius, rollback and verification before implementation.
---
# Review Fix Plan
Compose:
fix-risk-assessor → impact-estimator → rollback-checker → verification-planner → regression-detector.

Return risk, affected areas, required tests, rollout/rollback and recommendation.
