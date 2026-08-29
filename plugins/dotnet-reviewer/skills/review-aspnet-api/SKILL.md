---
name: review-aspnet-api
description: >
  Review an ASP.NET Core API for HTTP behavior, contracts, dependency injection,
  middleware, validation, authorization boundaries, error handling and API quality.
  Use when the request is specifically about controllers, minimal APIs or web APIs.
---

# Review ASP.NET Core API

Review observable API behavior and framework usage before editing.

## Review dimensions

### HTTP contracts
- correct status codes;
- consistent response shapes;
- route design;
- idempotency;
- pagination;
- validation;
- cancellation tokens.

### ASP.NET Core architecture
- middleware ordering;
- dependency injection lifetimes;
- options/configuration;
- filters/endpoints;
- model binding;
- exception handling.

### Authorization boundary
- endpoint protection;
- policy/role usage;
- resource-level checks;
- tenant/user boundary enforcement.

### Reliability
- timeout handling;
- external dependency failures;
- retries only where safe;
- request cancellation;
- logging/observability.

### API maintainability
- contract/domain separation;
- DTO usage;
- versioning concerns;
- duplicated endpoint logic.

## Output

Return:

1. API summary;
2. high-risk endpoints;
3. prioritized findings;
4. contract issues;
5. framework issues;
6. authorization concerns;
7. recommended fixes;
8. test scenarios.

## Boundaries

For broad repository review use `review-dotnet`.
For security-focused analysis use `review-security`.
