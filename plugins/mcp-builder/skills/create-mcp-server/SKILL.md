---
name: create-mcp-server
description: >
  Use when the user wants to design or implement a new MCP server from an API,
  repository or business domain. Prefer capability-first design over endpoint mirroring.
---

# Create MCP Server

Inspect the target first. Define user/agent tasks, then map the smallest useful MCP capabilities.

Core rules:
- capability-first, not endpoint-first;
- choose tools, resources and prompts deliberately;
- define schemas, errors, auth and side effects;
- follow the repository's stack and conventions;
- implement real behavior, tests and documentation;
- never claim execution or validation that did not occur.

For the full engineering checklist, read [references/engineering-guide.md](references/engineering-guide.md).
