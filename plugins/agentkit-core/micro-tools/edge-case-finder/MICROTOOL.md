# Edge Case Finder

## Responsibility
Find realistic edge conditions likely to break a requirement or implementation.

## Consider
- min/max/boundary values;
- missing/empty/duplicate input;
- concurrency;
- time/date/timezone;
- authorization/tenant boundaries;
- network/backend failure;
- retries;
- partial state;
- malformed external data.

## Output
edge case; trigger condition; likely failure; suggested test or guard.

## Boundary
Prioritize plausible business/system edges over exotic theoretical cases.
