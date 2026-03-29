---
name: abacus-skill-creator
description: >-
  Creates production-ready AI agent skills from workflow descriptions, code,
  API docs, or any raw input. Activates when user asks to create a skill,
  automate a workflow, build an agent, or turn a process into reusable software.
allowed-tools:
  - WebSearch
  - FileRead
  - FileWrite
  - Bash
  - CodeExecution
---

## Jezik komunikacije
- Sva komunikacija sa korisnikom: srpski jezik, latinica, ekavski dijalekt
- Isporuka svih rezultata i izveštaja: srpski jezik
- Bez reči bosanskog/hrvatskog porekla
- Interna dokumentacija i reference ostaju na engleskom

## Workflow: Kreiranje i održavanje Skills-a

Standardizovana procedura za kreiranje, isporuku i održavanje agent skills-a kroz GitHub integraciju.

### Koraci

1. **Definisanje zahteva (korisnik)**
   - Korisnik opisuje šta skill treba da radi — tekstom, kodom, linkom, dokumentom.
   - Agent postavlja dodatna pitanja ako je potrebno.

2. **Kreiranje strukture (agent, lokalno)**
   - Agent pokreće 5-fazni pipeline (Discovery → Design → Architecture → Detection → Implementation).
   - Rezultat: kompletna skill direktorijum struktura sa SKILL.md, skriptama, referencama i dokumentacijom.

3. **Push na GitHub (agent → `zalchemist/abacus-skills/skill-name/`)**
   - Agent push-uje gotov skill u centralni repozitorijum: **[zalchemist/abacus-skills](https://github.com/zalchemist/abacus-skills)**.
   - Svaki skill se čuva u zasebnom poddirektorijumu (`skill-name/`).
   - Primer putanje: `https://github.com/zalchemist/abacus-skills/tree/main/stock-analyzer/`

4. **Import u Abacus (korisnik, GitHub URL)**
   - Korisnik otvara Abacus AI → Agent Settings → Customize & Add Skills → **+ New Skill**.
   - Bira **GitHub** tab i unosi URL do skill direktorijuma.
   - Primer URL-a: `https://github.com/zalchemist/abacus-skills/tree/main/stock-analyzer/`
   - Klik na **Import from GitHub** — skill se automatski učitava.
   - **Privatni repozitorijum?** Pogledaj `references/private-repo-access.md` — objašnjava kako dozvoliti samo Abacus AI pristup bez javnog postavljanja repozitorijuma.

5. **Izmene i ažuriranje (agent menja → push → korisnik re-importuje)**
   - Korisnik prijavljuje problem ili traži izmenu.
   - Agent menja fajlove lokalno, push-uje na GitHub.
   - Korisnik ponovo importuje skill sa istog URL-a (ili briše stari i dodaje novi).

### Napomena: Centralni repozitorijum

Svi skills-i se čuvaju u jednom centralnom repozitorijumu:
- **Repo:** [zalchemist/abacus-skills](https://github.com/zalchemist/abacus-skills)
- **Struktura:** Svaki skill ima svoj poddirektorijum sa kompletnom strukturom (`SKILL.md`, `scripts/`, `references/`, `README.md`).
- **Prednosti:** Jednostavno upravljanje, verzionisanje, i brz import u Abacus platformu.
- **Privatni repozitorijum:** Ako je `abacus-skills` privatan, Abacus AI može pristupiti preko GitHub Deploy Key-a (samo za čitanje, vezan za jedan repozitorijum). Detaljna uputstva: `references/private-repo-access.md`.

# Abacus Skill Creator

Autonomous skill factory that transforms raw material — workflow descriptions, existing code, API documentation, PDFs, transcripts — into complete, validated, production-ready agent skills.

The user provides sources. The agent handles everything else: research, specification, architecture, implementation, validation, and delivery.

## Skill Description

This skill creates self-contained agent skills following the Abacus AI skill format. It accepts any form of input (natural language descriptions, code files, links, documents) and produces a fully structured skill directory with SKILL.md, scripts, references, and documentation.

**Key capabilities:**
- Converts vague workflow descriptions into precise skill specifications
- Researches and selects optimal APIs, libraries, and data sources
- Generates functional Python code (no placeholders or TODOs)
- Validates output with automated quality and security checks
- Supports simple skills and multi-agent suites

## Workflow

### Phase 1: Discovery
Read all provided material — follow links, parse files, study code. Research available APIs and data sources. Compare options by cost, rate limits, and quality. See `references/phase1-discovery.md`.

### Phase 2: Design
Define 4–6 priority use cases covering 80% of real usage. For each: name, objective, inputs, outputs, methodology. Uncover implicit requirements the user didn't articulate. See `references/phase2-design.md`.

### Phase 3: Architecture
Decide skill type (simple vs. complex suite). Structure the directory. Plan file organization and module boundaries. See `references/phase3-architecture.md`.

### Phase 4: Detection
Craft the SKILL.md frontmatter description with activation keywords. Target 95%+ activation reliability. See `references/phase4-detection.md`.

### Phase 5: Implementation
Write all files — SKILL.md, scripts, references, README. Run `scripts/validate.py` and `scripts/security_scan.py`. Fix issues and re-validate. See `references/phase5-implementation.md`.

## Tools & Capabilities

| Tool | Purpose |
|------|---------|
| `scripts/validate.py` | Validates skill structure and SKILL.md format |
| `scripts/security_scan.py` | Scans for hardcoded secrets and vulnerabilities |
| `scripts/export_utils.py` | Exports skills for different platforms |
| `scripts/skill_registry.py` | Manages skill registry and staleness checks |
| `scripts/staleness_check.py` | Detects stale skills needing review |

**Reference docs** in `references/`: architecture guide, pipeline phases, quality standards, cross-platform guide, multi-agent guide, interactive mode, export guide, templates guide.

## Quality Standards

**Production-Ready**: All generated code must work without modifications. No `TODO`, `pass`, or `NotImplementedError` allowed.

**Functional**: Complete error handling, input validation, and edge case coverage in every script.

**Specific**: Concrete implementations with real logic — not generic wrappers or placeholder functions.

**Validated**: Every skill passes `validate.py` (structure check) and `security_scan.py` (no secrets, no vulnerabilities) before delivery.

**Well-Documented**: Every skill includes SKILL.md (specification), README.md (user guide), and inline code comments.

See `references/quality-standards.md` for full standards.

## Examples

### Creating a skill from a description
```
User: Create a skill that analyzes stock prices using RSI and MACD indicators
Agent: [Runs 5-phase pipeline → produces stock-analyzer/ skill directory]
```
See `examples/stock-analyzer/` for a complete example output.

### Creating a skill from existing code
```
User: Turn scripts/invoice_processor.py into a reusable skill
Agent: [Reads code → extracts workflow → produces invoice-processor/ skill]
```

### Creating a skill from API docs
```
User: Make a skill for querying inventory using https://api.example.com/docs
Agent: [Fetches docs → designs use cases → produces inventory-query/ skill]
```