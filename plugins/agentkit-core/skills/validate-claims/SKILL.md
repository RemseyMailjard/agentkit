---
name: validate-claims
description: >
  Use when a user wants to check whether statements in a document, proposal,
  report, message or deliverable are actually supported by evidence.
---

# Validate Claims

Compose:
1. claim-verifier
2. contradiction-detector
3. evidence-checker
4. risk-scanner

## Output
For material claims return:
- VERIFIED;
- PARTIALLY SUPPORTED;
- UNVERIFIED;
- CONTRADICTED.

Include evidence, consequence and the smallest verification step still required.
Do not browse or invent evidence unless the parent task explicitly provides or requests sources.
