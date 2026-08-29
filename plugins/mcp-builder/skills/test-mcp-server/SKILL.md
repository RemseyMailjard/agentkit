---
name: test-mcp-server
description: >
  Design and implement tests for an MCP server. Use when the user asks to verify
  MCP tools/resources, validate contracts, test negative paths, reproduce failures,
  or establish a reliable MCP test suite.
---

# Test MCP Server

Test observable MCP behavior, not only internal helper functions.

## Workflow

1. Inspect the implementation, capabilities and existing test conventions.
2. Build a capability inventory.
3. Identify critical happy paths and negative paths.
4. Separate:
   - unit tests;
   - backend adapter tests;
   - MCP/protocol-level tests;
   - end-to-end tests.
5. Define deterministic fixtures and mocks where appropriate.
6. Implement the smallest useful test pyramid.
7. Run tests when execution is available.
8. Report failures with reproduction evidence.
9. Do not hide failing tests by weakening assertions.
10. Recommend missing coverage and reliability checks.

## Minimum behavior matrix

For each important capability consider:

- valid invocation;
- missing required input;
- invalid input;
- empty result;
- not found;
- unauthenticated;
- unauthorized;
- backend timeout;
- rate limit;
- malformed backend response;
- safe retry behavior for writes;
- side-effect verification.

## Contract testing

Verify:
- tool/resource names;
- descriptions where routing depends on them;
- input schema;
- required vs optional properties;
- structured output shape;
- stable error behavior.

## Agent-usability tests

Where practical, include routing scenarios that verify that neighboring tools have
clear enough names and descriptions to be selected correctly.

## Output

Return:
1. test strategy;
2. coverage matrix;
3. implemented tests;
4. commands used to run them;
5. failures and evidence;
6. remaining coverage gaps.

Never claim that tests pass unless they were actually executed successfully.
