# Plan: Eval-suite van MCP Builder uitbreiden

## Context

`AI-HANDOFF-CONTEXT.md` beschrijft een grote meerjarige roadmap voor AgentKit
(nieuwe plugins, NoteBuddy, Azure, Power Platform, CI/CD, etc.) met de instructie
om zelfstandig door te bouwen. In plaats van die hele roadmap te volgen, is
gekozen om te beginnen bij de eigen "P0"-actie uit sectie 30 van dat document:
de MCP Builder eval-suite is nog te dun (15 cases, doel v1.0 is 30-50) om nieuwe
plugins bovenop een instabiele/onbewezen baseline te bouwen. Dit sluit aan bij de
eigen prioriteringsregel in het document ("geen nieuwe plugin toevoegen wanneer
een bestaande kernplugin fundamenteel instabiel is").

Doel van deze stap: `evals/mcp-builder/cases.json` uitbreiden met 15-20 nieuwe,
sterke cases die de categorieën uit sectie 22 dekken (happy path, negative path,
ambiguous request, neighboring-skill conflict, scope restriction, multi-step
workflow, security-sensitive case, non-action/review-only case,
execution-required case, failure handling) — voor elk van de 6 skills, met focus
op gaten die de huidige 15 cases nog niet dekken.

Belangrijk: er worden geen echte Codex-routingtests uitgevoerd (dat vereist een
externe Codex-sessie) en dat wordt ook niet geclaimd. Deze stap levert alléén
goed gestructureerde, geloofwaardige eval-cases op die later door een
Codex-sessie of de gebruiker tegen de marketplace gedraaid kunnen worden.

## Aanpak

1. **Analyseer dekking van de huidige 15 cases** per skill en per categorie uit
   sectie 22, om precies te zien welke combinaties (skill × categorie) ontbreken.
   Observatie uit het lezen van `evals/mcp-builder/cases.json`:
   - `create-mcp-server`: heeft happy path (2x) en scope-vraag, mist een
     ambiguous/negative case en een failure-handling case.
   - `create-mcp-tool`: heeft ambiguity, redesign, side-effect; mist een
     negative-path en een neighboring-skill-conflict case.
   - `review-mcp-server`: alleen 1 solo-case + 1 multi-skill case; mist
     ambiguous-routing en scope-restriction cases.
   - `reverse-engineer-api`: 2 cases (analysis-only, capability model); mist
     negative-path (bv. geen OpenAPI spec beschikbaar) en neighboring-conflict
     met create-mcp-server.
   - `secure-mcp-server`: 3 cases; mist execution-required case (bv. "voer de
     hardening tests ook echt uit") en failure-handling (bv. onduidelijke
     scope tussen review vs secure).
   - `test-mcp-server`: 3 cases; mist multi-step-workflow (test dan fix) en
     een zuivere happy-path zonder complicatie.

2. **Nieuwe cases schrijven** (16-18 stuks) die dezelfde JSON-vorm volgen als
   bestaande entries in [cases.json](../../evals/mcp-builder/cases.json):
   `id`, `prompt`, `expected_skill` (of `expected_skills` voor multi-skill),
   `quality_checks`. IDs blijven kebab-case en beschrijvend, geen duplicaten met
   bestaande IDs. Elke nieuwe case moet een reëel, plausibel gebruikersverzoek
   zijn (geen kunstmatige test-only taal) en minstens één van de categorieën uit
   sectie 22 dekken die nu ontbreekt voor die skill.

3. **Valideer het JSON-bestand** na het schrijven (bv. `node -e "JSON.parse(...)"`
   of Python's `json.load`) om syntaxfouten uit te sluiten — dit is de enige
   "uitvoering" die hier eerlijk geclaimd kan worden.

4. **`docs/architecture.md` of `AGENTS.md` blijven ongewijzigd** tenzij het
   aantal eval-categorieën wijzigt — dit is puur een eval-data-uitbreiding, geen
   architectuurwijziging.

5. **Rapporteer aan het eind**: hoeveel cases zijn toegevoegd, welke
   categorieën nu gedekt zijn per skill, en wat nog open staat richting de
   30-50 doelstelling (bijv. multi-skill workflows met 3+ skills, of
   cross-plugin scenario's zodra er een tweede plugin is).

## Bestanden

- `evals/mcp-builder/cases.json` — enige bestand dat wijzigt.

## Verificatie

- JSON-validatie slaagt (`node -e "require('./evals/mcp-builder/cases.json')"` of
  gelijkwaardig) — bevestigt geen syntaxfouten.
- Handmatige telling: totaal aantal cases (huidige 15 + nieuwe) en een korte
  tabel welke skill/categorie-combinaties nu gedekt zijn, in de eindsamenvatting
  aan de gebruiker — geen claim dat de cases al "geslaagd" zijn in een echte
  Codex-run, want dat is niet uitgevoerd.
