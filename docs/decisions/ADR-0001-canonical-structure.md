# ADR-0001 — Canonical Repository Structure

| Field | Value |
|---|---|
| **Status** | accepted |
| **Date** | 2026-05-01 |
| **Author** | Flawless Studio |

## Context

The `flawlessstudio/flawlessstudio` repository serves as the organizational hub for the Flawless Studio ecosystem. It needed a structure that could:

- Hold immutable canonical standards applicable across all repos
- Organize operational documentation without ambiguity
- Scale as new registries and verticals are added
- Maintain bilingual parity (EN + ES) as a first-class constraint

## Options considered

**Option A — Flat structure**  
All documents at root level. Simple, but does not scale. No separation between canon, docs, and ecosystem artifacts.

**Option B — Docs-only structure**  
Everything under `docs/`. Standard for many repos, but conflates canonical standards with operational documentation.

**Option C — Layered structure with explicit canon tier (chosen)**  
Separate `canon/` as highest-authority tier. `docs/` for operational content. `ecosystem/` for cross-repo artifacts. `registries/` for domain-specific data. `assets/` for brand.

## Decision

Option C. The `canon/` directory holds immutable standards governed by `GOVERNANCE.md`. All other directories serve operational, navigational, or domain-specific roles. Bilingual parity (`.md` + `.es.md`) is enforced at all levels.

## Rationale

- Canon documents need a distinct authority tier that is visually and structurally separate from operational docs.
- Bilingual parity as a structural constraint prevents language drift over time.
- The layered model makes the purpose of each directory unambiguous without reading its contents.

## Consequences

- Every new canon document requires a bilingual counterpart before merging.
- `GOVERNANCE.md` must be consulted before modifying any file in `canon/`.
- New top-level directories require an ADR.

---

*See also: [`GOVERNANCE.md`](../../GOVERNANCE.md) · [`CANON.md`](../../CANON.md)*
