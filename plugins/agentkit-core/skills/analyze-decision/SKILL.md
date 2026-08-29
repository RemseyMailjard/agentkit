---
name: analyze-decision
description: >
  Use when a user wants to identify what was decided, what remains an assumption,
  and whether notes, messages or requirements contain conflicting statements.
---

# Analyze Decision

Compose:
1. decision-extractor
2. assumption-detector
3. contradiction-detector
4. evidence-checker
5. decision-summary-builder

## Output
Return:
- DECISIONS;
- ASSUMPTIONS;
- CONTRADICTIONS;
- unresolved questions that materially affect execution.

Separate explicit decisions from inference. Do not convert recommendations into decisions.
