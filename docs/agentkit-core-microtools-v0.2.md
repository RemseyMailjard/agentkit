# AgentKit Core — Micro-tools Batch 2

## Added micro-tools
- decision-extractor
- assumption-detector
- contradiction-detector
- claim-verifier
- priority-scorer
- scope-guard
- dependency-mapper
- handoff-builder
- change-impact-checker
- test-evidence-checker

## Added Skills
- analyze-decision
- prioritize-work
- validate-claims
- prepare-handoff

## Current Core architecture

AgentKit Core now contains two capability groups:

### Execution quality
- final-message-check
- find-next-action
- check-definition-of-done

### Decision and continuation
- analyze-decision
- prioritize-work
- validate-claims
- prepare-handoff

Micro-tools remain internal and composable. Skills remain the routing surface.
