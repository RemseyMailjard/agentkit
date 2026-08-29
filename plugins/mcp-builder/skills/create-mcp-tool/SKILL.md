---
name: create-mcp-tool
description: >
  Add or redesign a single MCP tool in an existing MCP server. Use for requests
  involving a new agent action, tool contract, schema or backend operation.
---

# Create MCP Tool

## Workflow

1. Inspect the existing MCP server and conventions.
2. Understand the business operation behind the requested action.
3. Decide whether the capability should be a tool, resource, prompt or an extension of an existing capability.
4. Choose a clear capability name.
5. Design the smallest useful input schema.
6. Define structured output and error behavior.
7. Implement the backend adapter.
8. Add validation, authorization checks and safe error handling.
9. Add focused automated tests.
10. Add or update a usage example and documentation.

## Agent usability test

Before implementing, verify that a model can infer:

- when to use the tool;
- when not to use it;
- what each parameter means;
- whether the operation changes state;
- what success and failure look like.

If those answers are ambiguous, improve the contract before adding code.
