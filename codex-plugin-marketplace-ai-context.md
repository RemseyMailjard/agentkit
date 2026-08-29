Codex Plugin Marketplace — AI 
Context
DEFINITIE
Een Codex Plugin Marketplace is een GitHub-gebaseerde catalogus met herbruikbare plugins die door Codex gebruikt 
kunnen worden. Een Marketplace is dus niet één plugin, maar een verzameling plugins. Elke plugin bundelt één of 
meer AI-capabilities, bijvoorbeeld: skills; instructies; workflows; tools; apps; MCP-integraties; configuratie; 
domeinkennis. Het doel is om gespecialiseerde AI-capabilities op een gestandaardiseerde manier beschikbaar te 
maken.
CONCEPTUEEL MODEL
Marketplace → Plugin → Skills → Instructions / tools / workflows. De Marketplace fungeert als een soort: App Store 
voor gespecialiseerde AI-capabilities.
MARKETPLACE-MANIFEST
Centrale Marketplace-definitie staat typisch in .agents/plugins/marketplace.json en beschrijft welke plugins 
beschikbaar zijn en waar Codex deze kan vinden. De Marketplace kan vanuit een publieke of private GitHub-
repository beschikbaar worden gemaakt.
WAT IS EEN PLUGIN?
Een plugin is een zelfstandig pakket van AI-functionaliteit rond één duidelijk doel of domein. Voorbeelden: dotnet-
reviewer, power-platform, azure, m365-copilot, mcp-builder, lab-generator, training-creator, notebuddy. Een plugin 
kan meerdere onderdelen bevatten, zoals instructions, skills en references.
SKILLS VERSUS PLUGINS
Een skill is meestal één gespecialiseerde taak of workflow. Een plugin is het pakket waarin meerdere gerelateerde 
skills en andere capabilities kunnen worden gecombineerd.
MOGELIJKE PLUGINONDERDELEN
Skills: herbruikbare instructies voor specifieke taken. Instructions: gedragsregels en domeinspecifieke instructies voor 
de AI. Workflows: meerdere AI-stappen gecombineerd tot één proces. Tools: GitHub, Azure, Microsoft Graph, Power 
Platform, SharePoint, OneNote, REST APIs, databases. MCP-integraties: toegang tot externe tools, resources, prompts, 
data en systemen.
SKILLS4-IT AGENTKIT MARKETPLACE
Binnen Skills4-IT kan de repository agentkit fungeren als centrale Marketplace voor AI-capabilities met plugins zoals 
power-platform, azure, m365-copilot, mcp-builder, training-creator, lab-generator, dotnet-reviewer en notebuddy.
PLUGIN: POWER-PLATFORM
Doel: AI ondersteunen bij het ontwerpen, bouwen en beoordelen van Power Platform-oplossingen. Mogelijke 
capabilities: Power Apps, Power Automate, Dataverse, Copilot Studio, Power Platform ALM, governance, solution 
architecture. Mogelijke skills: power-apps-review, power-automate-builder, dataverse-designer, copilot-studio-agent-
builder, power-platform-architecture-review.
PLUGIN: AZURE
Doel: Azure-oplossingen ontwerpen, bouwen, reviewen en troubleshooten. Mogelijke skills: azure-architecture, azure-
functions-builder, azure-security-review, azure-cost-review, azure-deployment, azure-troubleshooter.
PLUGIN: M365-COPILOT
Doel: Microsoft 365 Copilot en AI-agentoplossingen ondersteunen. Mogelijke onderwerpen: Microsoft 365 Copilot, 
Copilot Studio, agents, declarative agents, Microsoft Graph, connectors, MCP, enterprise knowledge, governance.
PLUGIN: MCP-BUILDER
Doel: MCP-servers ontwerpen en implementeren. Mogelijke skills: mcp-design, mcp-tool-design, mcp-resource-
design, mcp-prompt-design, mcp-security-review, mcp-server-builder, mcp-debugger. Mogelijke technologieën: 
Python, FastMCP, TypeScript, C#, .NET, HTTP MCP, Cloudflare Workers, Azure Functions.
PLUGIN: TRAINING-CREATOR
Doel: AI gebruiken om professioneel trainingsmateriaal te ontwikkelen met Skills4-IT-didactiek: eerst eenvoudig 
uitleggen; daarna verdiepen; praktijkvoorbeelden gebruiken; hands-on oefeningen toevoegen; realistische 
businesscases gebruiken; duidelijk en stapsgewijs werken. Mogelijke skills: training-outline-generator, course-
designer, slide-content-generator, exercise-generator, assessment-generator, trainer-guide-generator.
PLUGIN: LAB-GENERATOR
Doel: hands-on technische labs genereren. Gewenste workflow: Onderwerp → Leerdoelen → Vereisten → Setup → 
Stapsgewijze oefeningen → Expected results → Troubleshooting → Challenge → Clean-up. Mogelijke skills: lab-
generator, lab-validator, lab-debugger, lab-difficulty-adjuster, lab-solution-generator.
PLUGIN: DOTNET-REVIEWER
Doel: C#/.NET-code en repositories systematisch reviewen. Mogelijke reviewgebieden: architecture, code quality, 
security, performance, dependency management, testing, maintainability, ASP.NET Core, Entity Framework Core, 
cloud readiness. Mogelijke workflow: Repository inspecteren → Architectuur analyseren → Code smells detecteren → 
Security review → Performance review → Tests beoordelen → Concrete verbeteringen voorstellen. Geschikt als eerste 
reference implementation voor de Marketplace.
PLUGIN: NOTEBUDDY
NoteBuddy kan een MCP-backed plugin worden met architectuur: Codex/ChatGPT → NoteBuddy Plugin → 
NoteBuddy MCP Server → Microsoft Graph → OneNote. Doel: OneNote gebruiken als AI-kennisbank en 
memorylaag. Mogelijke capabilities: onenote.knowledge.find, onenote.knowledge.get, onenote.knowledge.save, 
onenote.knowledge.upsert, onenote.knowledge.append, onenote.knowledge.findOrCreateSection.
AGENTKIT ALS AI CAPABILITY PLATFORM
Strategisch doel: een centraal Skills4-IT AI Capability Platform bouwen; niet uitsluitend een verzameling prompts.
STRATEGISCHE VOORDELEN
Herbruikbaarheid, consistentie, specialisatie en compositie van plugins en skills.
MULTI-AGENT MOGELIJKHEDEN
