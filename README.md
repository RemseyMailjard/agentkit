# AgentKit by Skills4-IT

Modular AI capabilities for Codex.

**Build · Review · Integrate · Learn**

AgentKit is a Codex plugin marketplace for Microsoft engineering, AI integrations,
developer-quality workflows, knowledge, and hands-on training creation.

## Plugins

The flagship plugin is **MCP Builder** (Developer Tools). It includes six focused
skills:

- `create-mcp-server`
- `create-mcp-tool`
- `review-mcp-server`
- `reverse-engineer-api`
- `secure-mcp-server`
- `test-mcp-server`

Three more plugins are included:

- **.NET Reviewer** (Developer Tools) — `review-dotnet`, `review-aspnet-api`,
  `review-ef-core`, `review-security`, `fix-findings`.
- **Lab Generator** (Education) — `create-lab`, `create-challenge`, `review-lab`,
  `test-lab`, `adapt-lab`.
- **Training Creator** (Education) — `analyze-training-need`, `analyze-audience`,
  `define-learning-objectives`, `design-training`, `create-assessment`,
  `create-instructor-brief`, `review-training-readiness`, `adapt-training`.

Each plugin has its own behavioral evaluation suite for routing, quality, safety, and
ambiguous requests under `evals/<plugin-name>/cases.json`.

## Installing via Codex

See [docs/codex-installation.md](./docs/codex-installation.md) for adding this
repository as a Codex CLI marketplace and installing a plugin.

## Repository structure

```text
.
├── .agents/plugins/marketplace.json
├── AGENTS.md
├── docs/
│   ├── architecture.md
│   ├── codex-installation.md
│   ├── dotnet-reviewer.md
│   ├── lab-generator.md
│   ├── training-creator.md
│   └── skills4it-training-methodology.md
├── evals/
│   ├── mcp-builder/cases.json
│   ├── dotnet-reviewer/cases.json
│   ├── lab-generator/cases.json
│   └── training-creator/cases.json
└── plugins/
    ├── mcp-builder/
    │   ├── .codex-plugin/plugin.json
    │   └── skills/
    │       ├── create-mcp-server/SKILL.md
    │       ├── create-mcp-tool/SKILL.md
    │       ├── review-mcp-server/SKILL.md
    │       ├── reverse-engineer-api/SKILL.md
    │       ├── secure-mcp-server/SKILL.md
    │       └── test-mcp-server/SKILL.md
    ├── dotnet-reviewer/
    │   ├── .codex-plugin/plugin.json
    │   └── skills/
    │       ├── review-dotnet/SKILL.md
    │       ├── review-aspnet-api/SKILL.md
    │       ├── review-ef-core/SKILL.md
    │       ├── review-security/SKILL.md
    │       └── fix-findings/SKILL.md
    ├── lab-generator/
    │   ├── .codex-plugin/plugin.json
    │   └── skills/
    │       ├── create-lab/SKILL.md
    │       ├── create-challenge/SKILL.md
    │       ├── review-lab/SKILL.md
    │       ├── test-lab/SKILL.md
    │       └── adapt-lab/SKILL.md
    └── training-creator/
        ├── .codex-plugin/plugin.json
        └── skills/
            ├── analyze-training-need/SKILL.md
            ├── analyze-audience/SKILL.md
            ├── define-learning-objectives/SKILL.md
            ├── design-training/SKILL.md
            ├── create-assessment/SKILL.md
            ├── create-instructor-brief/SKILL.md
            ├── review-training-readiness/SKILL.md
            └── adapt-training/SKILL.md
```

## Design principles

1. Capability-first, not endpoint-first.
2. Small composable skills.
3. Review before remediation.
4. Security and testing are explicit workflows.
5. Evaluations live alongside the capabilities they verify.
6. Practical outputs must work in real repositories.
7. Never claim execution success without evidence.

## Roadmap

### Done
- MCP Builder v0.2 (security and testing skills, routing/quality eval cases)
- .NET Reviewer v0.1
- Lab Generator v0.1
- Training Creator v0.1

### Next
- NoteBuddy MCP-backed plugin
- Azure
- Power Platform
- Microsoft 365 Copilot

## License

MIT
