---
name: final-message-check
description: >
  Use when a user wants a fast final check of an email, chat message or other outbound text before sending, focused only on material risks and clarity.
---
# Final Message Check
Compose: intent-extractor → risk-scanner → clarity-checker → tone-fit-checker → commitment-detector.

Return:
- SEND or ADJUST;
- maximum five material findings;
- exact fragment involved;
- smallest useful correction.

Do not rewrite everything by default. Ignore tiny style issues unless they create ambiguity or risk.
