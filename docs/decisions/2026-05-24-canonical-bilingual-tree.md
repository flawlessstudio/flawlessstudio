# ADR-001 — Canonical Bilingual Tree

**Date:** 2026-05-24  
**Status:** Accepted  
**Author:** Flawless Studio Founder  

---

## Context

The repository had a flat, ad-hoc structure with `docs/en/` and `docs/es/` as parallel silos. This created:

- Structural redundancy (same concept in two places)
- No clear source of truth per document
- No framework for operational vs. reference vs. canonical knowledge
- Difficulty onboarding AI agents (no clear entry points)

## Decision

Adopt a **canonical bilingual tree** as the single structural standard for all Flawless Studio repositories.

### Pattern

- `filename.md` — English, authoritative source
- `filename.es.md` — Spanish, localized translation
- One file per concept, one location per file type

### Tree structure

```
/
├── canon/           # Immutable operating principles (EN+ES)
├── registries/      # Structured data registries (YAML + MD)
├── ecosystem/       # Repo map and index (EN+ES)
├── docs/            # Diataxis knowledge base
│   ├── tutorials/
│   ├── how-to/
│   ├── explanation/
│   ├── reference/   # Agent specs, contracts, manifests
│   ├── decisions/   # ADRs and migration logs
│   ├── runbooks/    # Operational guides
│   └── audits/      # Quality snapshots
└── .github/         # Contribution and automation config
```

### Knowledge framework

- **canon/** — truth that does not change without founder decision
- **docs/reference/** — specs and contracts for AI agents
- **docs/runbooks/** — operational knowledge (ES-first, EN pending)
- **docs/decisions/** — all ADRs live here

## Consequences

### Positive
- Single source of truth per concept
- Clear entry point for AI agents (`docs/reference/AI_AGENT_QUICKSTART.md`)
- Diataxis provides a principled framework for future documentation growth
- `CODEOWNERS` and `CONTRIBUTING.md` enforce governance

### Negative
- 11 legacy files required manual migration and deletion
- EN runbooks pending (4 files exist only in ES)

## Migration executed

| Action | Files | Commit |
|---|---|---|
| Scaffold canonical tree | 47 files | `954d54b` |
| Delete `docs/en/` | 7 files | `390ef49`–`fd78135` |
| Delete `docs/es/` | 4 files | `0e4fd18`–`29705b1` |
| Delete root duplicates | 2 files | `c4ca53e`, `908d8ab` |

---

_Next ADR: when a second structural decision is made._
