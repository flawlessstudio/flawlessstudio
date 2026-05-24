# Migration Log

> Chronological record of all structural migrations, refactors, and breaking changes.

## 2026-05-24 — Bilingual canonical tree

- **Before:** Flat `docs/en/` + `docs/es/` structure with 11 mixed files.
- **After:** Canonical bilingual tree with `canon/`, `registries/`, `ecosystem/`, `docs/` (Diátaxis), `.github/`.
- **Pattern:** `filename.md` (EN, authoritative) + `filename.es.md` (ES, localized).
- **Files migrated:** `docs/en/*` → `docs/reference/` · `docs/es/*` → `docs/runbooks/`
- **Rationale:** Eliminate structural redundancy, single source of truth per concept, Flawless Method compliance.

---

_Active log. Add new entries at the top._
