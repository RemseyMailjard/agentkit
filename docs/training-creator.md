# Training Creator Architecture

## Purpose

Turn a vague training request into a deliverable, audience-aware learning experience.

## Flow

```text
analyze-training-need
        ↓
analyze-audience
        ↓
define-learning-objectives
        ↓
design-training
        ├── create-assessment
        └── Lab Generator / technical plugins
        ↓
create-instructor-brief
        ↓
review-training-readiness
```

`adapt-training` may be used at any point after the original objectives are understood.

## Cross-plugin orchestration

Training Creator is intentionally orchestration-heavy.

Examples:

```text
Training Creator
→ MCP Builder
→ Lab Generator
```

```text
Training Creator
→ .NET Reviewer
→ Lab Generator
```

Future:

```text
Training Creator
→ Azure / Power Platform / M365 Copilot
→ Lab Generator
```

## Core distinction

Training Creator owns:

- audience;
- objectives;
- sequencing;
- training narrative;
- pacing;
- assessment;
- instructor preparation;
- delivery readiness.

Technical plugins own:

- technical correctness;
- implementation;
- platform-specific constraints.

Lab Generator owns:

- executable learner practice.
