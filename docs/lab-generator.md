# Lab Generator Architecture

## Purpose

Convert technical learning objectives into executable hands-on experiences.

## Skill boundaries

```text
create-lab
├── full lab
├── create-challenge
│   └── independent transfer task
├── review-lab
│   └── instructional quality review
├── test-lab
│   └── executability/readiness validation
└── adapt-lab
    └── audience/environment adaptation
```

## Cross-plugin pattern

Lab Generator is an orchestration-friendly plugin.

It may consume outputs from:

- MCP Builder
- .NET Reviewer
- future Azure / Power Platform / M365 Copilot plugins

The technical plugin defines what is technically correct.
Lab Generator defines how a learner should practice it.
