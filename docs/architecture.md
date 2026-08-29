# AgentKit Architecture

## Layers

```text
Marketplace
  -> Plugin
     -> Skill / Workflow
        -> Micro-capability
```

MCP-backed plugins may additionally invoke a remote MCP capability layer.

## MCP Builder v0.2

```text
MCP Builder
├── create-mcp-server
├── create-mcp-tool
├── review-mcp-server
├── reverse-engineer-api
├── secure-mcp-server
└── test-mcp-server
```

The skills intentionally overlap only where a real workflow crosses boundaries.
Routing evaluations should make those boundaries observable.

## Planned platform areas

- Build: MCP Builder, .NET Reviewer, Azure, Power Platform
- Learn: Training Creator, Lab Generator
- Know: NoteBuddy and organization knowledge
