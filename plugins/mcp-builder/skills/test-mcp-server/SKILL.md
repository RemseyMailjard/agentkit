---
name: test-mcp-server
description: >
  Use when the user wants behavioral tests or validation for an MCP server,
  including protocol, backend, auth, failure-path or agent-routing behavior.
---

# Test MCP Server

Test behavior, not implementation trivia.

Cover valid, missing, invalid, empty, not-found, unauthenticated, unauthorized, timeout, rate-limit and malformed-response paths where relevant.

Include side-effect safety and retry behavior for writes. Separate observed failures from inferred risks.

Never claim tests passed unless they were actually executed.

Read [references/test-matrix.md](references/test-matrix.md) for the complete matrix.
