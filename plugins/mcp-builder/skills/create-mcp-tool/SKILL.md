---
name: create-mcp-tool
description: >
  Use when the user wants to add or redesign one MCP capability in an existing
  server, especially a new agent action, tool contract, schema or backend operation.
---

# Create MCP Tool

Inspect the existing server first. Model the business operation, not merely an endpoint.

Do:
- decide whether it should be a tool, resource, prompt or extension;
- use a clear, discriminative name;
- keep the input schema minimal;
- define structured success and failure outputs;
- handle auth, validation and side effects;
- add focused tests and docs.

Read [references/tool-design.md](references/tool-design.md) for the detailed checklist.
