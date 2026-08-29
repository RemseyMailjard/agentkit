# AgentKit by Skills4-IT

**Modular AI capabilities for Codex.**

Build · Review · Integrate · Learn · Remember

AgentKit is a modular Codex plugin marketplace for engineering, quality, training,
knowledge and agent workflows.

## Current platform

```text
AgentKit
│
├── BUILD
│   └── MCP Builder v0.2
│
├── QUALITY
│   └── .NET Reviewer v0.1
│
├── LEARN
│   ├── Lab Generator v0.1
│   └── Training Creator v0.1
│
└── KNOW
    └── OneNote v0.1 scaffold
```

## Core principle

AgentKit is not a prompt library.

It is a capability platform where:

```text
Marketplace
→ Plugin
→ Skill / Workflow
→ Concrete output
```

## Platform rules

1. Capability-first over endpoint-first.
2. Small, composable skills.
3. Review before remediation unless explicitly requested otherwise.
4. Security and testing are first-class capabilities.
5. Never claim execution success without evidence.
6. Technical plugins own technical correctness.
7. Training Creator owns learning design.
8. Lab Generator owns executable learner practice.
9. OneNote owns context and knowledge intent.
10. Cross-plugin routing must be testable.

## Golden workflow

The first reference workflow is:

`examples/golden-workflows/mcp-training/`

It demonstrates:

```text
Training Creator
→ MCP Builder
→ Lab Generator
→ Assessment
→ Instructor Brief
→ Delivery Readiness
```

## Current priorities

### v0.3 — Consolidation
- central architecture
- plugin routing matrix
- cross-plugin evals
- golden workflow registration
- shared platform rules

### v0.4
- harden MCP Builder
- grow plugin eval suites
- add CI validation
- add example implementations

### v0.5
- Azure or Power Platform plugin
- depending on routing maturity

## Repository structure

```text
.
├── .agents/plugins/marketplace.json
├── README.md
├── AGENTS.md
├── CHANGELOG.md
├── docs/
│   ├── architecture.md
│   ├── routing-matrix.md
│   └── plugin-contract.md
├── evals/
│   ├── mcp-builder/
│   ├── dotnet-reviewer/
│   ├── lab-generator/
│   ├── training-creator/
│   └── cross-plugin/
├── examples/
│   └── golden-workflows/
└── plugins/
    ├── mcp-builder/
    ├── dotnet-reviewer/
    ├── lab-generator/
    ├── training-creator/
    └── onenote/
```

## Status

AgentKit is in alpha.

The platform currently proves multiple specialist plugins and early orchestration,
but still needs automated eval execution, CI validation and production reference
implementations before a stable v1.0 release.
