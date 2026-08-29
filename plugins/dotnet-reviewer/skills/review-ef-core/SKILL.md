---
name: review-ef-core
description: >
  Review Entity Framework Core usage for correctness, query efficiency, DbContext
  lifetime, tracking behavior, migrations, concurrency and data-access maintainability.
---

# Review Entity Framework Core

## Review dimensions

### DbContext
- correct lifetime;
- no accidental singleton capture;
- safe parallel usage;
- cancellation support;
- transaction boundaries.

### Queries
- N+1 risks;
- over-fetching;
- client-side evaluation risks;
- missing projections;
- inappropriate tracking;
- query composition;
- pagination.

### Data modeling
- relationships;
- required/optional boundaries;
- indexes;
- keys;
- owned/value objects where relevant.

### Writes
- concurrency handling;
- transaction consistency;
- SaveChanges usage;
- bulk operation implications;
- idempotency where relevant.

### Migrations
- destructive changes;
- rollout safety;
- seed-data concerns;
- backward compatibility.

## Output

Return:

1. data-access summary;
2. correctness findings;
3. performance findings;
4. migration risks;
5. recommended changes;
6. tests/benchmarks to add.

## Boundary

Do not turn every performance issue into an EF Core issue.
Use the general reviewer when the root cause is outside data access.
