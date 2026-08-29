---
name: create-challenge
description: >
  Create a challenge exercise that builds on an existing lab or lesson and requires
  the learner to apply the concept independently rather than repeat earlier steps.
---

# Create Challenge

A challenge must test transfer.

Do not simply restate the guided exercise with different names.

## Workflow

1. Identify the concept the learner has already practiced.
2. Remove some or all step-by-step guidance.
3. Introduce one meaningful variation or constraint.
4. State the target outcome clearly.
5. Provide success criteria.
6. Add optional hints separately.
7. Include an instructor solution or validation approach when appropriate.

## Good challenge patterns

- change the business requirement;
- add one extra validation rule;
- use a second environment/resource;
- troubleshoot a deliberately broken setup;
- optimize an existing solution;
- extend a workflow with one new capability.

## Output

Return:

1. scenario;
2. challenge brief;
3. constraints;
4. success criteria;
5. optional hints;
6. validation/solution notes.

## Boundary

If the user wants a full end-to-end lab, use `create-lab`.
