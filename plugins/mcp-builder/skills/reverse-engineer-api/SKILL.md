---
name: reverse-engineer-api
description: >
  Analyze an existing API, OpenAPI specification, integration or plugin and turn
  it into a capability-oriented MCP design. Use when the user asks to reverse
  engineer backend behavior, authentication, contracts or tool opportunities.
---

# Reverse Engineer API for MCP

## Goal

Understand the system before proposing MCP tools. Distinguish observed facts from
inference and clearly mark unknowns.

## Workflow

1. Inventory available evidence: code, OpenAPI, docs, manifests, examples and traffic traces supplied by the user.
2. Identify domains and primary entities.
3. Map endpoints/actions to underlying business capabilities.
4. Document authentication, authorization and credential flow.
5. Document request/response schemas and error behavior.
6. Identify read, write, destructive, privileged and asynchronous operations.
7. Group low-level endpoints into agent-meaningful tasks.
8. Decide which capabilities should be tools, resources or prompts.
9. Propose names, descriptions, schemas and output contracts.
10. Identify gaps, risks and questions that block implementation.
11. Produce an implementation plan or scaffold when requested.

## Output model

### System summary
### Observed architecture
### Authentication and authorization
### Data/contracts
### Capability map

| Capability | Type | Backend source | Side effect | Risk |
| --- | --- | --- | --- | --- |

### Proposed MCP surface

For each capability include:
- name;
- purpose;
- input;
- output;
- side effects;
- relevant authorization;
- likely failure modes.

### Evidence vs inference

Explicitly separate facts found in source material from conclusions inferred from
naming or behavior.

### Implementation plan
