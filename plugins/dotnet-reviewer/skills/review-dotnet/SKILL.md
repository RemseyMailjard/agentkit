---
name: review-dotnet
description: >
  Perform a broad .NET repository review focused on correctness, maintainability,
  testability, reliability and idiomatic C#/.NET usage. Use for general code review
  requests that are not specifically limited to ASP.NET Core, EF Core or security.
---

# Review .NET Repository

Review before modifying code unless the user explicitly requests remediation.

## Scope

Inspect the repository for:

- correctness;
- nullability and defensive coding;
- async/await usage;
- dependency injection;
- configuration;
- error handling;
- logging;
- maintainability;
- testability;
- duplicated logic;
- API and domain boundaries;
- resource disposal;
- concurrency risks;
- package/dependency concerns;
- obvious performance issues.

## Workflow

1. Inspect solution/project structure.
2. Identify application type and major boundaries.
3. Review representative high-risk code paths first.
4. Record concrete findings with file/line evidence where available.
5. Classify severity.
6. Separate defects from stylistic improvements.
7. Recommend the smallest useful remediation.
8. Do not edit code unless explicitly requested.

## Severity

- Critical
- High
- Medium
- Low
- Improvement

## Output

Return:

1. executive summary;
2. strongest aspects;
3. top findings;
4. detailed findings with evidence;
5. recommended fixes;
6. testing gaps;
7. unresolved risks.

## Boundaries

Prefer a more specialized skill when the request is specifically about:

- ASP.NET Core API behavior -> `review-aspnet-api`
- Entity Framework Core -> `review-ef-core`
- security -> `review-security`

Do not route every specialized review through this general skill.
