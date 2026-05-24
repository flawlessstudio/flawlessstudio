# GOVERNANCE

> Rules, roles, and processes that govern this repository and the Flawless ecosystem.

## Roles

| Role | Responsibility |
|---|---|
| **Founder** | Final decision authority on all canonical documents |
| **Contributor** | Proposes changes via PR; no direct push to `main` |
| **Agent** | Automated systems operating under strict contracts; contracts defined in `docs/reference/` when formalized |

## Change Process

1. Open an issue describing the proposed change.
2. Link to the affected canonical document.
3. Submit a PR with the change and a rationale in `docs/decisions/`.
4. Founder reviews and merges or rejects.

## Branch Strategy

- `main` — production-ready, protected. Direct pushes are blocked; all changes enter via PR.
- `draft/*` — work in progress, unreviewed
- `fix/*` — targeted corrections

## Language Policy

- All canonical documents exist in both EN (`.md`) and ES (`.es.md`).
- EN is the authoritative version. ES is the localized equivalent.
- Translations must be updated atomically with their EN source.

---

_Last reviewed: 2026-05-24_
