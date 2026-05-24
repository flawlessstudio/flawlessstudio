# MIGRATION LOG

> Chronological record of all structural migrations, refactors, and breaking changes in this repository.

## 2026-05-24 — Bilingual tree scaffold

- **Action:** Restructured repo from flat `docs/en` + `docs/es` to canonical bilingual tree.
- **Pattern adopted:** `filename.md` (EN, authoritative) + `filename.es.md` (ES, localized).
- **Files moved:** `docs/en/*` → `docs/runbooks/` · `docs/es/*` → `docs/runbooks/*.es.md`
- **New layers added:** `canon/`, `registries/`, `ecosystem/`, `docs/` (Diátaxis), `.github/`
- **Rationale:** Eliminate structural redundancy, enforce single source of truth per concept.

---

_Active log. Add entries chronologically. Oldest entries at bottom._
