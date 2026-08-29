# MCP Review Checklist

## Capability design
Task-oriented naming, appropriate granularity, no redundant tools, correct tool/resource distinction.

## Agent usability
Discriminative descriptions, minimal understandable parameters, explicit side effects.

## Contracts
Strong schemas, required/optional boundaries, structured outputs and useful errors.

## Architecture
Thin MCP surface, separated domain logic/backend adapters, testable dependencies.

## Reliability
Timeouts, safe retries, partial failures, rate limiting and backend error mapping.

## Security
Authentication, authorization, secrets, destructive operations, untrusted input, data exposure and least privilege.

## Testing
Unit, integration, protocol behavior and negative-path coverage.
