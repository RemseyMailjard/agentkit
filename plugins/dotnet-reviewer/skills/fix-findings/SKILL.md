---
name: fix-findings
description: >
  Remediate selected .NET review findings after a review has identified concrete
  issues. Use when the user asks to fix specific severities, finding IDs or review
  items rather than perform a fresh review.
---

# Fix .NET Review Findings

Only remediate findings that are in scope.

## Workflow

1. Read the existing review or explicit finding list.
2. Confirm the exact findings/severities requested.
3. Inspect affected code and tests.
4. Apply the smallest safe change that addresses the root cause.
5. Preserve public behavior unless the fix requires an intentional contract change.
6. Add or update regression tests.
7. Run relevant tests/builds when execution is available.
8. Report what changed and what remains.
9. Never claim success without execution evidence.

## Rules

- Do not silently fix Low/Improvement findings when the user asked for Critical/High.
- Do not refactor unrelated code.
- Do not weaken authorization, validation or tests to make failures disappear.
- If a finding is not reproducible or evidence is insufficient, report that instead of guessing.

## Output

Return:

1. findings fixed;
2. files changed;
3. tests added/updated;
4. execution results;
5. remaining findings;
6. risks or follow-up work.
