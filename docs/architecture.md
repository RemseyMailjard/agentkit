# Architecture

## Marketplace

The repository root contains `.agents/plugins/marketplace.json`, which lists the
plugins Codex can discover from this marketplace.

## Plugin layer

`plugins/mcp-builder` is the first Skills4-IT plugin. It packages reusable workflows
for MCP architecture and implementation.

## Skill layer

v0.1 contains four skills:

- `create-mcp-server` — end-to-end MCP server design and implementation;
- `create-mcp-tool` — focused addition or redesign of one MCP capability;
- `review-mcp-server` — architecture, quality and security review before remediation;
- `reverse-engineer-api` — API/integration analysis into an MCP capability model.

## Evaluation layer

`evals/mcp-builder/cases.json` provides initial routing and quality scenarios. The
next step is to integrate these cases with a repeatable Codex/plugin evaluation run.

## Planned plugins

- dotnet-reviewer
- lab-generator
- notebuddy
- training-creator
- azure
- power-platform
- m365-copilot
