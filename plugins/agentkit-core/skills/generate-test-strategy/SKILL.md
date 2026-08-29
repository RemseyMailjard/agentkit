---
name: generate-test-strategy
description: >
  Use when a user wants a practical test strategy derived from requirements, risks, changes or acceptance criteria.
---

# Generate Test Strategy

Use shared context:
- ../../context/engineering-principles.md

Compose:
1. test-case-generator
2. edge-case-finder
3. test-evidence-checker
4. verification-planner
5. risk-scanner

## Output
Return:
- test scope;
- prioritized test cases;
- failure/edge paths;
- environment/data needs;
- required evidence;
- what remains unverified.

Favor high-signal coverage over exhaustive test lists.
