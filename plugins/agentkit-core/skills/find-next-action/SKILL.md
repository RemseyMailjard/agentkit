---
name: find-next-action
description: >
  Use when a user provides an email, note, meeting outcome, project item or conversation and wants the next concrete action or waiting-for state.
---
# Find Next Action
Compose: intent-extractor → next-action-finder → waiting-for-detector → commitment-detector.

Decision:
- user can act now → NEXT ACTION;
- another party/system must act first → WAITING FOR;
- already complete → DONE;
- truly insufficient evidence → NEEDS CLARIFICATION.

Return status, one primary action, owner, timing, dependency and brief evidence.
