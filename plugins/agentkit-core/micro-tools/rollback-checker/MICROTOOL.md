# Rollback Checker

## Responsibility
Assess whether a change can be safely reversed.

## Check
- code/config rollback;
- schema/data reversibility;
- external side effects;
- compatibility;
- migrations;
- secrets/identity changes;
- deployment sequencing;
- operational recovery.

## Output
Reversible / partially reversible / difficult to reverse, with required precautions.

## Boundary
Do not call a change reversible if data or external side effects cannot be restored.
