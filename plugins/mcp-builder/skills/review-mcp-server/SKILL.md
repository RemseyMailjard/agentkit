---
name: review-mcp-server
description: >
  Review an MCP server for capability design, agent usability, architecture,
  reliability, maintainability, testing and security. Review before modifying code.
---

# Review MCP Server

Do not modify code during the initial review unless the user explicitly asks for fixes.

## Review dimensions

### Capability design

- Are capabilities task-oriented rather than endpoint-oriented?
- Is naming consistent and domain-focused?
- Are there redundant or excessively granular tools?
- Are read-only resources incorrectly modeled as actions?

### Agent usability

- Can a model reliably select the correct capability?
- Are tool descriptions discriminative?
- Are parameters understandable and minimal?
- Are side effects clearly communicated?

### Contracts

- Strong schemas
- Correct required/optional boundaries
- Structured outputs
- Useful error contracts

### Architecture

- Separation of MCP surface, domain logic and backend adapters
- Configuration and dependency boundaries
- Reuse and testability

### Reliability

- timeouts
- retries where safe
- partial failures
- rate limiting
- backend error mapping

### Security

- authentication
- authorization
- secret management
- destructive operations
- untrusted input
- data exposure
- least privilege

### Testing

- unit coverage
- integration coverage
- protocol/capability behavior
- negative paths

## Severity

Classify findings as:

- Critical
- High
- Medium
- Low
- Improvement

## Output

Return:

1. executive summary;
2. strongest aspects;
3. top five issues;
4. detailed findings with evidence;
5. recommended fixes;
6. proposed target architecture where useful.
