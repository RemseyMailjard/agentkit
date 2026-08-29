---
name: prepare-continuation
description: >
  Use when work must be paused or transferred and the user wants a clean continuation checkpoint for a future session or another AI.
---
# Prepare Continuation
Compose:
prepare-handoff → handoff-readiness-checker → commitment-tracker → unfinished-work-detector → next-action-finder.

Return goal, current state, decisions, completed work, open items, commitments, blockers and exact next action.
