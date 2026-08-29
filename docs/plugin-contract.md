# AgentKit Plugin Contract

Every AgentKit plugin should satisfy this contract.

## Plugin requirements

Each plugin must define:

1. a narrow primary responsibility;
2. a valid plugin manifest;
3. skill folders;
4. explicit routing descriptions;
5. clear boundaries with neighboring skills/plugins;
6. practical output expectations;
7. at least one eval per skill;
8. version and changelog.

## Skill requirements

Each skill should define:

- when to use it;
- when not to use it;
- workflow;
- safety/side effects where relevant;
- output contract;
- evidence/execution rules where relevant.

## Eval requirements

Each mature plugin should test:

- happy path;
- negative path;
- ambiguity;
- neighboring-skill conflict;
- scope restriction;
- multi-step workflow;
- failure handling;
- security-sensitive behavior where relevant.

## Cross-plugin requirements

Cross-plugin workflows must define:

- ownership per layer;
- expected order;
- duplication avoidance;
- handoff artifact or context;
- final acceptance criteria.

## Stability rule

Do not add a new plugin merely because a domain is interesting.

Add it when:

- current routing is understandable;
- plugin boundaries are stable enough;
- the new plugin adds a distinct responsibility.
