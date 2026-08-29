---
name: check-definition-of-done
description: >
  Use when a user wants to verify whether code, a document, workflow, project result or other artifact is genuinely complete rather than merely implemented.
---
# Check Definition of Done
Compose: acceptance-criteria-checker → evidence-checker → completion-detector → risk-scanner.

Return one status:
- DONE
- DONE WITH RISKS
- NOT DONE
- UNKNOWN

Then list criteria, evidence, unmet/unverified items and smallest actions required to reach DONE.
Never claim tests, deployment or validation passed without evidence.
