# AgentKit by Skills4-IT

Modular AI capabilities for Codex.

**Build · Review · Integrate · Learn**

AgentKit is a Codex plugin marketplace for Microsoft engineering, AI integrations,
developer-quality workflows, knowledge, and hands-on training creation.

## v0.2 alpha

The flagship plugin is **MCP Builder**.

It includes six focused skills:

- `create-mcp-server`
- `create-mcp-tool`
- `review-mcp-server`
- `reverse-engineer-api`
- `secure-mcp-server`
- `test-mcp-server`

The repository also includes a growing behavioral evaluation suite for routing,
quality, safety, and ambiguous requests.

## Installing via Codex

See [docs/codex-installation.md](./docs/codex-installation.md) for adding this
repository as a Codex CLI marketplace and installing a plugin.

## Repository structure

```text
.
├── .agents/plugins/marketplace.json
├── AGENTS.md
├── docs/
│   └── architecture.md
├── evals/
│   └── mcp-builder/cases.json
└── plugins/
    └── mcp-builder/
        ├── .codex-plugin/plugin.json
        └── skills/
            ├── create-mcp-server/SKILL.md
            ├── create-mcp-tool/SKILL.md
            ├── review-mcp-server/SKILL.md
            ├── reverse-engineer-api/SKILL.md
            ├── secure-mcp-server/SKILL.md
            └── test-mcp-server/SKILL.md
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

### v0.2
- Harden MCP Builder
- 15+ routing and quality eval cases
- security and testing skills

### v0.3
- .NET Reviewer
- Lab Generator
- NoteBuddy MCP-backed plugin

### v0.4
- Training Creator
- Azure
- Power Platform
- Microsoft 365 Copilot

## License

MIT
