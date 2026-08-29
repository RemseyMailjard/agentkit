# AgentKit Core + Micro-tools v0.1
Architecture: Marketplace → Plugin → Skill → Micro-tool.

Micro-tools remain internal to avoid routing ambiguity and unnecessary trigger cost.

First composed Skills:
1. final-message-check
2. find-next-action
3. check-definition-of-done

Next planned micro-tool batch:
- decision extractor
- assumption detector
- contradiction detector
- claim verifier
- priority scorer
- scope guard
- dependency mapper
- handoff builder
- change impact checker
- test evidence checker

Marketplace integration: add `agentkit-core` as a local plugin in `.agents/plugins/marketplace.json`.
