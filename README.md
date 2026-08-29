# Skills4-IT Codex Marketplace

A modular Codex plugin marketplace for Microsoft engineering, AI integrations,
developer quality workflows and hands-on training creation.

## v0.1 alpha

The first plugin is **MCP Builder**.

It includes skills for:

- creating MCP servers;
- creating focused MCP tools;
- reviewing MCP server architecture and quality;
- reverse-engineering APIs into capability-oriented MCP designs.

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
            └── reverse-engineer-api/SKILL.md
```

## Marketplace manifest

Codex discovers the plugin through `.agents/plugins/marketplace.json`.

## Roadmap

### v0.1

- MCP Builder
- initial skill eval cases

### v0.2

- .NET Reviewer
- Lab Generator
- NoteBuddy MCP-backed plugin

### v0.3

- Training Creator
- Azure
- Power Platform
- Microsoft 365 Copilot

## Design principles

1. Capability-first, not endpoint-first.
2. Small composable skills.
3. Review before remediation.
4. Security and testing built into workflows.
5. Evaluation cases alongside skills.
6. Practical outputs that can be used in real repositories.

## Status

Alpha. The structure follows the current Codex plugin marketplace pattern and is
intended to evolve through hands-on evaluation in Codex.

## License

MIT
