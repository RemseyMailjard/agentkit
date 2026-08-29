---
name: analyze-training-need
description: >
  Analyze a client or internal request for IT training before designing the course.
  Use when the user has a brief, email, agenda item, topic request, certification
  target or vague training need that must first be translated into a practical
  training problem and delivery brief.
---

# Analyze Training Need

Do not jump directly into slides, modules or labs.

First determine what problem the training must solve.

## Skills4-IT principle

A useful training need is not just a topic.

Translate:

topic
→ target behavior
→ real work context
→ constraints
→ evidence of success

## Workflow

1. Identify the requested topic or technology.
2. Identify the business or work context.
3. Determine what participants must be able to do afterwards.
4. Separate:
   - awareness;
   - adoption/productivity;
   - technical implementation;
   - troubleshooting;
   - certification/exam preparation.
5. Identify audience assumptions.
6. Identify delivery format and duration.
7. Identify environment, account, tenant, license and permission dependencies.
8. Identify likely blockers.
9. Identify missing decisions.
10. Propose the minimum useful training scope.

## Special attention for technical training

Check for:

- required cloud tenant or sandbox;
- developer tooling;
- repository access;
- Azure/M365/Power Platform permissions;
- local admin limitations;
- network restrictions/proxies;
- MFA/account-expiry risks;
- lab reset/recovery options;
- fallback demos when participant access fails.

## Output

Return:

1. training need summary;
2. target behavior;
3. audience hypothesis;
4. practical use cases;
5. constraints/dependencies;
6. likely blockers;
7. open decisions;
8. recommended scope;
9. recommended next skill.

## Boundary

Do not design the complete course yet. Route to `design-training` once the need is sufficiently clear.
