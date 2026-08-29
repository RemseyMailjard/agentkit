---
name: create-mcp-server
description: >
  Design and implement a Model Context Protocol server. Use when the user asks
  to create an MCP server, expose an API through MCP, turn business capabilities
  into MCP tools or resources, or scaffold a new MCP integration.
---

# Create MCP Server

Build MCP servers capability-first rather than endpoint-first.

## Core principle

Do not simply expose every backend endpoint as an MCP tool. Translate the target
system into a small set of clear, task-oriented capabilities that an AI agent can
understand and use safely.

## Workflow

1. Inspect the repository and target system before editing.
2. Identify human and agent use cases.
3. Inventory available backend capabilities.
4. Design the MCP capability map.
5. Separate tools, resources and prompts deliberately.
6. Design input and output contracts.
7. Determine authentication and authorization requirements.
8. Identify write, destructive, privileged and sensitive operations.
9. Scaffold or extend the server using the repository's existing stack where possible.
10. Implement capabilities with validation and actionable errors.
11. Add configuration and secret handling.
12. Add logging/observability appropriate to the project.
13. Add automated tests.
14. Add example MCP interactions.
15. Review security and agent usability.
16. Update project documentation.

## Capability naming

Prefer domain-oriented task names.

Good examples:

- `customer.search`
- `customer.get`
- `customer.create`
- `customer.notes.append`

Avoid transport- or endpoint-shaped names such as `postCustomerRequest`,
`executeEndpoint4`, or `getCustomerApi`.

## Tool design

Each tool should:

- perform one understandable task;
- have an explicit schema;
- minimize required arguments;
- use descriptions that distinguish it from nearby tools;
- produce useful structured output;
- return actionable errors;
- avoid leaking unnecessary backend implementation details.

## Safety

Classify operations as read-only, write, destructive, privileged or sensitive.
Use explicit approval/confirmation patterns when the existing application or use
case warrants them. Never embed secrets or credentials in source code.

## Implementation preference

If the user did not select a language, inspect the existing repository first and
follow its technology stack when practical. For a greenfield server, choose a
well-supported MCP SDK and explain the language choice briefly before implementation.

## Minimum tests

Cover at least:

- valid invocation;
- invalid input;
- missing required input;
- empty result;
- backend failure;
- authentication/authorization failure when applicable;
- malformed or unexpected backend response.

## Required outcome

Produce a usable implementation, not only a scaffold. Include:

1. capability map;
2. architecture summary;
3. implementation;
4. configuration guidance;
5. tests;
6. example usage;
7. README/documentation updates;
8. unresolved decisions or risks.

Do not claim completion while core capabilities still contain placeholders,
TODO implementations or fake responses unless the user explicitly asked for a prototype.
