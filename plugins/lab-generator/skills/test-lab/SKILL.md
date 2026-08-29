---
name: test-lab
description: >
  Validate whether a technical lab is actually executable, complete and internally
  consistent. Use when the user wants a dry run, dependency check, step validation
  or delivery-readiness assessment.
---

# Test Technical Lab

Test the lab as if you were a participant.

## Validation workflow

1. Inventory all prerequisites.
2. Verify each dependency and permission requirement.
3. Trace the lab from start to finish.
4. Check that every step has enough information to execute.
5. Check that referenced resources/files/names exist or are created earlier.
6. Verify checkpoints against the preceding steps.
7. Verify challenge prerequisites.
8. Identify hidden assumptions.
9. Identify likely participant blockers.
10. Validate cleanup.
11. If execution is available, run the lab or its automatable parts.
12. Separate observed failures from inferred risks.

## Output

Return:

1. readiness status;
2. blocker list;
3. prerequisite matrix;
4. step-by-step validation findings;
5. likely participant failure points;
6. estimated timing risks;
7. fixes required before delivery.

Never claim a lab was executed when it was only reviewed statically.
