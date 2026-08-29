# AI-HANDOFF-CONTEXT.md

## 1. Projectnaam

**AgentKit by Skills4-IT**

Repository:

`https://github.com/RemseyMailjard/agentkit`

Eigenaar:

**Skills4-IT / Remsey Mailjard**

Huidige fase:

**v0.2-alpha / MCP Builder baseline**

---

# 2. Hoofddoel

Bouw AgentKit uit tot een volwaardige, modulaire **Codex Plugin Marketplace** voor IT-professionals, developers, consultants en trainers.

AgentKit moet geen promptbibliotheek worden.

Het eindproduct moet een professioneel AI-capabilityplatform zijn met:

- gespecialiseerde Codex plugins;
- kleine, composable skills;
- duidelijke workflows;
- MCP-backed integraties;
- evaluaties;
- testbare routing;
- security;
- documentatie;
- herbruikbare engineeringstandaarden;
- uitbreidbaarheid richting andere AI-agentomgevingen.

De kernpositionering is:

> **AgentKit by Skills4-IT — Modular AI capabilities for Codex.**

Alternatieve positionering:

> **Turn Codex into your Microsoft engineering team.**

De architectuur moet waar mogelijk platformneutraal genoeg blijven zodat dezelfde skills later ook bruikbaar kunnen zijn voor andere agent-runtimes, MCP-clients of AI coding assistants.

---

# 3. Productvisie

AgentKit moet uiteindelijk bestaan uit vier hoofddomeinen.

```text
AgentKit
│
├── BUILD
│   ├── MCP Builder
│   ├── .NET Reviewer
│   ├── Azure
│   ├── Power Platform
│   └── M365 Copilot
│
├── LEARN
│   ├── Training Creator
│   ├── Lab Generator
│   └── Instructor Tools
│
├── KNOW
│   └── NoteBuddy
│       └── OneNote / AI Memory / Knowledge
│
└── CORE
    ├── Engineering Standards
    ├── Security
    ├── Testing
    ├── Documentation
    ├── Evaluation
    └── Definition of Done
```

Het conceptuele model is:

```text
Marketplace
    ↓
Plugin
    ↓
Workflow / Skill
    ↓
Micro-capability
```

Belangrijk:

- een **microtool** is een kleine gespecialiseerde denktaak;
- een **skill** is een herbruikbare taak;
- een **workflow** combineert meerdere skills;
- een **plugin** is een capability package;
- de **marketplace** is de distributielaag.

---

# 4. Doelgebruiker

AgentKit richt zich in eerste instantie op:

## Developers

Voorbeelden:

- C#/.NET developers;
- API developers;
- AI-agent developers;
- MCP developers;
- Azure developers;
- Power Platform developers.

## IT-professionals en consultants

Voorbeelden:

- Microsoft 365 consultants;
- Azure consultants;
- Power Platform consultants;
- AI consultants;
- solution architects.

## Trainers

Voorbeelden:

- IT-trainers;
- technical instructors;
- curriculum designers;
- hands-on lab creators.

---

# 5. Ontwerpprincipes

Deze principes zijn leidend en mogen niet zonder duidelijke reden worden losgelaten.

## 5.1 Capability-first, not endpoint-first

Voor MCP en integraties:

> Ontwerp eerst begrijpelijke business-capabilities voor een AI-agent.

Niet:

> Spiegel elke API-endpoint één-op-één naar een tool.

Voorbeeld:

Goed:

```text
customer.search
customer.get
customer.create
customer.notes.append
```

Niet:

```text
getCustomerApi
postCustomerRequest
executeEndpoint4
```

---

## 5.2 Kleine composable skills

Skills moeten:

- één duidelijke verantwoordelijkheid hebben;
- herkenbaar routeerbaar zijn;
- elkaar zo min mogelijk overlappen;
- samen workflows kunnen vormen.

---

## 5.3 Review vóór remediation

Een reviewskill hoort standaard eerst te analyseren.

Niet automatisch code aanpassen tenzij de gebruiker expliciet om fixes vraagt.

Voorbeeld:

```text
review-mcp-server
```

en daarna:

```text
fix findings
```

---

## 5.4 Security en testing zijn first-class capabilities

Security en testing zijn geen appendix.

Iedere serieuze plugin moet uiteindelijk:

- security-aandacht hebben;
- testbare output leveren;
- evals hebben;
- failure modes behandelen.

---

## 5.5 Bewijs boven claims

Nooit zeggen:

> tests pass

als tests niet werkelijk zijn uitgevoerd.

Nooit zeggen:

> implementation complete

wanneer kernfunctionaliteit nog TODO's, placeholders of fake production data bevat.

---

## 5.6 Praktische uitvoer

AgentKit moet echte output produceren:

- code;
- tests;
- architectuur;
- manifests;
- configuratie;
- labs;
- documentatie;
- evaluaties.

Geen generieke adviesmachine.

---

# 6. Huidige repositorystructuur

De repository gebruikt momenteel ongeveer deze structuur:

```text
agentkit/
│
├── README.md
├── AGENTS.md
├── CHANGELOG.md
├── LICENSE
│
├── .agents/
│   └── plugins/
│       └── marketplace.json
│
├── plugins/
│   └── mcp-builder/
│       ├── .codex-plugin/
│       │   └── plugin.json
│       │
│       └── skills/
│           ├── create-mcp-server/
│           │   └── SKILL.md
│           ├── create-mcp-tool/
│           │   └── SKILL.md
│           ├── review-mcp-server/
│           │   └── SKILL.md
│           ├── reverse-engineer-api/
│           │   └── SKILL.md
│           ├── secure-mcp-server/
│           │   └── SKILL.md
│           └── test-mcp-server/
│               └── SKILL.md
│
├── evals/
│   └── mcp-builder/
│       └── cases.json
│
└── docs/
    └── architecture.md
```

---

# 7. Huidige status MCP Builder

MCP Builder is de eerste flagship plugin.

Huidige versie:

**0.2.0**

Plugin:

```text
plugins/mcp-builder/
```

## Beschikbare skills

### 7.1 create-mcp-server

Doel:

Een complete MCP-server ontwerpen en implementeren.

Belangrijkste principes:

- capability-first;
- inspecteer eerst bestaande repo/stack;
- ontwerp tool/resource/prompt bewust;
- authentication en authorization behandelen;
- side effects classificeren;
- tests toevoegen;
- echte implementatie leveren;
- documentatie bijwerken.

---

### 7.2 create-mcp-tool

Doel:

Eén bestaande of nieuwe MCP capability ontwerpen.

Moet eerst bepalen:

- tool;
- resource;
- prompt;
- uitbreiding van bestaande capability.

Belangrijk:

Een endpoint is niet automatisch een MCP tool.

---

### 7.3 review-mcp-server

Doel:

MCP-server reviewen op:

- capability design;
- agent usability;
- contracts;
- architecture;
- reliability;
- security;
- testing.

Severity:

```text
Critical
High
Medium
Low
Improvement
```

Standaard eerst reviewen, niet wijzigen.

---

### 7.4 reverse-engineer-api

Doel:

Bestaande API / OpenAPI / integratie / plugin analyseren en omzetten naar een capability-oriented MCP-design.

Belangrijk:

Expliciet onderscheid maken tussen:

```text
Observed facts
vs
Inference
```

---

### 7.5 secure-mcp-server

Doel:

MCP security review en hardening.

Focus:

- trust boundaries;
- authentication;
- authorization;
- least privilege;
- secrets;
- destructive actions;
- untrusted input;
- prompt/tool injection;
- unsafe URLs;
- SSRF-risico;
- tenant isolation;
- data exposure;
- logging/privacy.

Severity:

```text
Critical
High
Medium
Low
Hardening
```

---

### 7.6 test-mcp-server

Doel:

MCP-server testbaar maken.

Testlagen:

```text
unit
adapter
protocol/capability
end-to-end
```

Minimum behavior matrix:

- valid invocation;
- missing input;
- invalid input;
- empty result;
- not found;
- unauthenticated;
- unauthorized;
- timeout;
- rate limit;
- malformed backend response;
- retry behavior;
- side-effect verification.

Nooit claimen dat tests slagen zonder uitvoering.

---

# 8. Huidige evaluaties

Er zijn momenteel ongeveer 15 MCP Builder eval-cases.

Deze testen onder andere:

- create server;
- review tool sprawl;
- add tool;
- reverse-engineer OpenAPI;
- security review;
- hardening;
- testing;
- auth failure reproduction;
- GET endpoint ambiguity;
- analysis only;
- review then fix;
- greenfield MCP server;
- schema redesign;
- security vs generic review;
- testing vs architecture review.

De eval-suite moet verder groeien.

---

# 9. Eerstvolgende technische stap

Voordat AgentKit sterk wordt verbreed moet MCP Builder eerst een aantoonbaar stabiele baseline worden.

## 9.1 Test MCP Builder daadwerkelijk in Codex

Gebruik minimaal deze routingtests.

### Test A

```text
Analyze this OpenAPI specification and propose a clean MCP capability model.
Do not implement anything.
```

Expected:

```text
reverse-engineer-api
```

---

### Test B

```text
This MCP server exposes 47 tools.
Review the architecture before changing anything.
```

Expected:

```text
review-mcp-server
```

---

### Test C

```text
Review this MCP implementation specifically for prompt injection,
unsafe URLs, secret leakage and tenant isolation.
```

Expected:

```text
secure-mcp-server
```

---

### Test D

```text
Don't review the architecture.
I only want tests for the current behavior,
including timeouts, malformed responses and authorization failures.
```

Expected:

```text
test-mcp-server
```

---

### Test E

```text
Expose this GET /customers/{id} endpoint through MCP.
```

Expected:

```text
create-mcp-tool
```

Maar de skill moet expliciet overwegen of dit beter een resource is.

---

# 10. Definition of Done voor MCP Builder v1.0

MCP Builder mag pas als v1.0 worden beschouwd als:

- alle skills duidelijk routeerbaar zijn;
- minimaal 30-50 sterke eval-cases bestaan;
- ambiguous routing getest is;
- multi-skill workflows getest zijn;
- security edge cases aanwezig zijn;
- testcases echte implementation scenarios bevatten;
- documentatie bruikbaar is voor externe gebruikers;
- skill naming stabiel is;
- pluginmanifest correct is;
- installatie via marketplace aantoonbaar werkt;
- minstens één echte MCP-server end-to-end met AgentKit is gebouwd;
- minstens één bestaande MCP-server succesvol door review/security/testing is gegaan;
- eval-resultaten gedocumenteerd zijn.

---

# 11. Volgende plugin: .NET Reviewer

Na stabilisatie van MCP Builder moet `.NET Reviewer` worden gebouwd.

Voorgestelde structuur:

```text
plugins/dotnet-reviewer/
│
├── .codex-plugin/
│   └── plugin.json
│
└── skills/
    ├── review-dotnet/
    ├── review-architecture/
    ├── review-aspnet-api/
    ├── review-ef-core/
    ├── review-security/
    ├── review-tests/
    ├── review-performance/
    └── fix-findings/
```

Belangrijkste ontwerpregel:

> Review en remediation blijven gescheiden.

## .NET Reviewer moet minimaal beoordelen op:

- correctness;
- architecture;
- security;
- maintainability;
- testability;
- async/await;
- dependency injection;
- configuration;
- ASP.NET Core;
- Entity Framework Core;
- API contracts;
- logging;
- exception handling;
- performance;
- testing strategy.

Severity:

```text
Critical
High
Medium
Low
Improvement
```

---

# 12. Daarna: Lab Generator

Lab Generator is belangrijk omdat dit eigen Skills4-IT trainings-IP kan bevatten.

Structuur:

```text
plugins/lab-generator/
│
├── .codex-plugin/
│   └── plugin.json
│
└── skills/
    ├── create-lab/
    ├── create-challenge/
    ├── review-lab/
    ├── test-lab/
    └── adapt-lab/
```

Didactisch model:

```text
explain
↓
demonstrate
↓
guide
↓
practice
↓
challenge
↓
reflect
```

Een lab moet standaard bevatten:

- scenario;
- learning objectives;
- estimated time;
- prerequisites;
- environment check;
- tasks;
- checkpoints;
- challenge;
- troubleshooting;
- expected result;
- cleanup;
- reflection.

Labs moeten realistisch en hands-on zijn.

---

# 13. Daarna: Training Creator

Training Creator bepaalt:

> Wat iemand moet leren en hoe de training wordt opgebouwd.

Lab Generator bepaalt:

> Hoe iemand dat daadwerkelijk oefent.

Voorgestelde structuur:

```text
plugins/training-creator/
│
└── skills/
    ├── needs-analysis/
    ├── audience-analysis/
    ├── learning-objectives/
    ├── course-designer/
    ├── lesson-designer/
    ├── demo-generator/
    ├── assessment-generator/
    └── instructor-brief/
```

Trainingsworkflow:

```text
Analyse
↓
Doelgroep
↓
Leerdoelen
↓
Didactische structuur
↓
Demo's
↓
Labs
↓
Challenges
↓
Assessment
↓
Instructor notes
```

---

# 14. NoteBuddy als MCP-backed plugin

NoteBuddy wordt de knowledge/memory layer.

Concept:

```text
Codex
│
├── NoteBuddy skills
│
└── NoteBuddy MCP
    ↓
Knowledge Gateway
    ↓
OneNote
```

Voorgestelde capabilities:

```text
knowledge.find
knowledge.get
knowledge.save
knowledge.upsert
knowledge.append

memory.find
memory.get
memory.save
```

Later mogelijk:

```text
project.context
person.context
training.context
company.context
```

Voorgestelde pluginstructuur:

```text
plugins/notebuddy/
│
├── .codex-plugin/
│   └── plugin.json
├── .mcp.json
└── skills/
    ├── recall-context/
    ├── capture-knowledge/
    ├── research-memory/
    └── project-context/
```

Architectuurscheiding:

```text
Skill
"When and why should knowledge be retrieved?"
↓
MCP
"Which capability should be called?"
↓
NoteBuddy backend
"How is OneNote accessed?"
```

---

# 15. Microsoft pluginfamilie

Na de developer/trainingbasis moet AgentKit uitbreiden met Microsoft-domeinen.

---

# 16. Azure plugin

Voorgestelde skills:

```text
azure/
├── azure-function-builder
├── app-service-builder
├── azure-storage
├── azure-sql
├── entra-auth
├── azure-openai
├── bicep-generator
├── architecture-review
├── cost-review
└── security-review
```

Doel:

Een Azure engineering expert voor echte repositorytaken.

---

# 17. Power Platform plugin

Voorgestelde skills:

```text
power-platform/
├── power-apps-builder
├── power-automate-builder
├── dataverse-designer
├── connector-builder
├── solution-reviewer
├── power-platform-alm
├── governance-review
└── testing
```

Doel:

Niet alleen advies geven maar daadwerkelijke oplossingen, ontwerpen, config en ALM guidance produceren.

---

# 18. M365 Copilot plugin

Voorgestelde scope:

```text
m365-copilot/
├── copilot-agent-builder
├── declarative-agent-builder
├── copilot-studio-builder
├── graph-integration
├── knowledge-source-designer
├── mcp-for-copilot
├── governance-review
└── security-review
```

Positioneer dit desnoods breder als:

> Microsoft AI Application Builder

---

# 19. Skills4-IT Core

AgentKit moet later gedeelde standaarden krijgen.

Voorgestelde structuur:

```text
shared/
├── standards/
│   ├── engineering.md
│   ├── security.md
│   ├── testing.md
│   ├── documentation.md
│   ├── training-design.md
│   └── definition-of-done.md
│
└── templates/
```

Later kan dit eventueel een eigen internal/core plugin worden.

---

# 20. Plugin Builder meta-plugin

Later moet AgentKit zichzelf kunnen uitbreiden.

Voorgestelde plugin:

```text
skills4it-plugin-builder
```

Doel:

Nieuwe plugins automatisch genereren.

Voorbeeld:

```text
Build a Codex plugin for SQL Server performance tuning.

Capabilities:
- query review
- execution plan analysis
- index recommendations
- troubleshooting
```

De meta-plugin genereert:

- plugin manifest;
- skill folders;
- SKILL.md files;
- evals;
- README;
- architecture;
- changelog entry;
- marketplace registration.

Dit is belangrijk voor schaalbaarheid.

---

# 21. Evaluatieplatform

AgentKit moet uiteindelijk een eigen evalstrategie hebben.

Evals moeten minstens testen:

## Routing

Selecteert Codex de juiste skill?

## Boundary behavior

Selecteert Codex niet de verkeerde neighboring skill?

## Multi-skill workflows

Wordt de juiste volgorde gebruikt?

## Quality

Voldoet de output aan inhoudelijke checks?

## Safety

Worden security en side effects correct behandeld?

## Execution truthfulness

Wordt niet beweerd dat tests/commando's uitgevoerd zijn wanneer dat niet zo is?

## Regression

Veranderen bestaande skills niet onverwacht door nieuwe plugins?

---

# 22. Vereiste eval-categorieën

Elke plugin moet uiteindelijk minimaal deze soorten tests hebben:

```text
happy path
negative path
ambiguous request
neighboring-skill conflict
scope restriction
multi-step workflow
security-sensitive case
non-action / review-only case
execution-required case
failure handling
```

---

# 23. CI/CD

Later moet GitHub Actions worden toegevoegd.

Minimale toekomstige pipeline:

```text
Pull Request
↓
JSON validation
↓
Plugin manifest validation
↓
SKILL frontmatter validation
↓
Broken path check
↓
Eval schema validation
↓
Optional Codex/plugin eval
↓
Status report
```

Later:

- linting;
- marketplace validation;
- version consistency check;
- changelog validation;
- docs check;
- security scanning.

---

# 24. Releaseproces

Gebruik semver.

Voorbeeld:

```text
0.2.0
0.3.0
0.4.0
1.0.0
```

Per release:

- update plugin version;
- update changelog;
- update README;
- run evals;
- document known limitations;
- tag release;
- eventueel GitHub Release maken.

---

# 25. Roadmap

## Phase 1 — Stabilize MCP Builder

Status:

**in progress**

Taken:

- echte Codex routingtests uitvoeren;
- evals uitbreiden naar 30-50;
- ambiguous routing verbeteren;
- end-to-end MCP example toevoegen;
- docs verbeteren;
- v1.0 criteria halen.

---

## Phase 2 — Developer Quality

Bouw:

- .NET Reviewer.

Doel:

testen of AgentKit meerdere gespecialiseerde plugins correct kan routeren.

---

## Phase 3 — Training IP

Bouw:

- Lab Generator;
- Training Creator.

Doel:

Skills4-IT didactiek als herbruikbare AI capabilities codificeren.

---

## Phase 4 — Knowledge Layer

Bouw:

- NoteBuddy plugin;
- MCP configuration;
- OneNote knowledge/memory workflows.

Doel:

AgentKit persistent context geven.

---

## Phase 5 — Microsoft Engineering

Bouw:

- Azure;
- Power Platform;
- M365 Copilot.

---

## Phase 6 — Shared Core

Bouw:

- shared standards;
- common definitions;
- reusable templates;
- plugin quality rules.

---

## Phase 7 — Meta Platform

Bouw:

- Plugin Builder;
- automatic scaffolding;
- automatic eval generation;
- marketplace registration automation.

---

## Phase 8 — Professional Product

Doel:

AgentKit geschikt maken voor:

- publiek gebruik;
- private organizations;
- consultancy;
- training;
- enterprise private marketplaces.

---

# 26. Mogelijk businessmodel

Nog niet leidend voor de code, maar architectuur moet dit later ondersteunen.

## Community

Voorbeelden:

- MCP Builder basic;
- .NET Reviewer;
- basic Lab Generator.

## Pro

Voorbeelden:

- advanced MCP workflows;
- Training Creator;
- Azure Architect;
- Power Platform Architect.

## Enterprise

Voorbeelden:

- private marketplace;
- organization standards;
- company knowledge;
- custom MCP integrations;
- governance packs;
- custom skills;
- evaluations;
- managed updates.

---

# 27. Definition of Done eindproduct

Het project is pas echt volwassen wanneer:

- AgentKit eenvoudig als marketplace geïnstalleerd kan worden;
- alle plugins valide manifests hebben;
- skills voorspelbaar routeerbaar zijn;
- evals automatisch kunnen draaien;
- CI basiskwaliteit controleert;
- minimaal 6-8 sterke plugins bestaan;
- MCP-backed NoteBuddy functioneert;
- documentatie externe gebruikers zelfstandig op weg helpt;
- voorbeelden bestaan;
- security review ingebouwd is;
- versies/releases georganiseerd zijn;
- plugin creation grotendeels geautomatiseerd is;
- AgentKit als product herkenbare branding heeft.

---

# 28. Werkinstructie voor de volgende AI-agent

Je taak is niet alleen adviseren.

Je taak is om AgentKit zelfstandig verder te bouwen richting het eindproduct.

Werk iteratief.

Gebruik bij voorkeur deze cyclus:

```text
Inspect
↓
Plan
↓
Implement
↓
Validate
↓
Evaluate
↓
Document
↓
Commit / prepare commit
↓
Next capability
```

Vraag niet steeds om bevestiging als de volgende stap logisch voortvloeit uit deze roadmap.

Neem zelfstandig redelijke technische beslissingen.

Stop alleen wanneer:

- een echte blocker bestaat;
- credentials of expliciete toestemming nodig zijn;
- er een fundamentele productkeuze is die niet verantwoord kan worden afgeleid;
- een externe handeling noodzakelijk is die niet beschikbaar is.

---

# 29. Prioriteringsregels

Bij twijfel:

1. correctness;
2. security;
3. testability;
4. maintainability;
5. developer usability;
6. agent usability;
7. extensibility;
8. polish.

Geen nieuwe plugin toevoegen wanneer een bestaande kernplugin fundamenteel instabiel is.

Maar voorkom ook eindeloze perfectionering.

Werk in kleine releases.

---

# 30. Eerstvolgende concrete backlog

## P0

- valideer AgentKit marketplace daadwerkelijk in Codex;
- voer de vijf kernroutingtests uit;
- documenteer resultaten;
- los routingproblemen op;
- voeg 15-20 extra MCP evals toe.

## P1

- voeg een voorbeeld-MCP-project toe onder `examples/`;
- gebruik AgentKit om dit voorbeeld te bouwen;
- gebruik review/security/testing skills op hetzelfde voorbeeld;
- documenteer before/after.

## P2

- start `.NET Reviewer`;
- maak plugin manifest;
- maak 5-8 eerste skills;
- voeg evals toe.

## P3

- bouw Lab Generator;
- definieer Skills4-IT didactische standaard;
- voeg realistische Microsoft labs als tests toe.

## P4

- bouw NoteBuddy plugin;
- definieer `.mcp.json`;
- koppel bestaande NoteBuddy MCP gateway;
- test recall/capture workflows.

---

# 31. Aanbevolen eerste voorbeeldproject

Maak een kleine realistische MCP-server als reference implementation.

Bijvoorbeeld:

```text
Customer Support MCP
```

Capabilities:

```text
customer.search
customer.get
ticket.search
ticket.get
ticket.comment.append
```

Gebruik dit project vervolgens voor:

- create-mcp-server;
- create-mcp-tool;
- review-mcp-server;
- secure-mcp-server;
- test-mcp-server.

Zo ontstaat één golden reference waarmee evals en documentatie kunnen worden verbeterd.

---

# 32. Belangrijke niet-doelen

AgentKit moet niet veranderen in:

- honderden generieke prompts;
- endpoint wrappers zonder capability design;
- één enorme monolithische skill;
- een marketingrepo zonder werkende capability;
- een verzameling voorbeelden zonder evaluaties;
- AI-output die tests of succes verzint.

---

# 33. Branding

Naam:

**AgentKit**

Subbrand:

**by Skills4-IT**

Voorkeur tagline:

> **Modular AI capabilities for Codex**

Alternatief:

> **Build · Review · Integrate · Learn**

Repo mag Skills4-IT duidelijk noemen, maar houd AgentKit als zelfstandige productnaam.

---

# 34. Repositoryregels

Elke nieuwe plugin moet minimaal bevatten:

```text
plugin-name/
├── .codex-plugin/
│   └── plugin.json
└── skills/
```

Iedere nieuwe skill moet minimaal definiëren:

1. naam;
2. description / routing intent;
3. workflow;
4. grenzen / wanneer niet gebruiken;
5. safety of side-effect considerations;
6. output expectations;
7. minimaal één eval-case.

---

# 35. Kwaliteitsvraag bij iedere toevoeging

Stel altijd deze vragen:

- Is dit een plugin, workflow, skill of micro-capability?
- Is deze verantwoordelijkheid al ergens anders aanwezig?
- Kan Codex betrouwbaar herkennen wanneer deze skill nodig is?
- Kan Codex herkennen wanneer deze skill juist niet nodig is?
- Is het gedrag testbaar?
- Is failure behavior beschreven?
- Zijn security en side effects duidelijk?
- Kan de output echt gebruikt worden?
- Hebben we een eval toegevoegd?

---

# 36. Gewenste eindtoestand

De gewenste eindtoestand is:

```text
AgentKit by Skills4-IT
│
├── betrouwbare Codex marketplace
├── meerdere professionele plugins
├── MCP-backed memory
├── Microsoft engineering expertise
├── developer quality tooling
├── training generation tooling
├── shared standards
├── automated evaluations
├── CI/CD
├── plugin generator
├── examples
├── documentation
└── releaseproces
```

Het systeem moet uiteindelijk voldoende zelfstandig zijn dat een gebruiker bijvoorbeeld kan zeggen:

```text
Build a production-ready MCP integration for this API.
```

of:

```text
Review this .NET repository and fix only Critical and High findings.
```

of:

```text
Create a 45-minute hands-on Azure lab for intermediate developers.
```

of:

```text
Use my NoteBuddy knowledge to create a new client training.
```

en AgentKit vervolgens automatisch de juiste plugin, skills, workflow en tools inzet.

---

# 37. Eindopdracht aan de AI

**Ga vanaf deze context zelfstandig verder met het bouwen van AgentKit tot een professioneel eindproduct.**

Werk van binnen naar buiten:

1. maak MCP Builder robuust;
2. bewijs routing en evalkwaliteit;
3. voeg .NET Reviewer toe;
4. voeg Lab Generator en Training Creator toe;
5. integreer NoteBuddy;
6. voeg Microsoft plugins toe;
7. bouw shared core;
8. automatiseer plugin creation en evaluations;
9. voeg CI/CD en releases toe;
10. maak documentatie en voorbeelden productwaardig.

Maak steeds concrete bestanden en code wanneer dat mogelijk is.

Vermijd alleen advies als daadwerkelijke implementatie mogelijk is.

Houd de roadmap bij.

Werk iteratief naar aantoonbare kwaliteit.

Het project is klaar wanneer AgentKit als een coherent, testbaar en professioneel AI-capabilityplatform zelfstandig bruikbaar is.
