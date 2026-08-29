# Training Creator v0.1

Training Creator is the Skills4-IT training-design plugin for AgentKit.

It captures a practical training methodology built around real IT delivery:

```text
training need
→ audience
→ measurable objectives
→ training design
→ demos + labs
→ assessment
→ instructor brief
→ delivery readiness
```

## Skills

- `analyze-training-need`
- `analyze-audience`
- `define-learning-objectives`
- `design-training`
- `create-assessment`
- `create-instructor-brief`
- `review-training-readiness`
- `adapt-training`

## Skills4-IT teaching model

```text
relevance / hook
→ simple explanation
→ concrete example
→ deeper explanation
→ demo
→ guided practice
→ independent practice
→ challenge
→ reflection
```

For technical audiences, bias toward hands-on implementation, troubleshooting and real constraints.

For end users, bias toward confidence, adoption, productivity and recognizable work scenarios.

## Training Creator vs Lab Generator

Training Creator decides:

> what should be learned, in what order, and why.

Lab Generator decides:

> how the learner practices one concrete objective.

## Example prompts

> Maak een nieuwe MCP-training voor klant X.
> Gebruik wat we al weten over eerdere trainingen,
> de doelgroep en eerdere problemen.

This is the kind of prompt Training Creator should route well: it names a concrete
client and topic, and expects the skill to pull in prior context (past trainings,
audience profile, known delivery issues) rather than starting from a blank template.
It typically enters at `analyze-training-need`, and — because the topic is MCP —
orchestrates with MCP Builder for the technical content and Lab Generator for the
hands-on labs.

## Delivery philosophy

A training is not ready merely because the slides are finished.

Accounts, licenses, permissions, tenant access, network restrictions, labs, fallback
routes and instructor decisions are part of training quality.
