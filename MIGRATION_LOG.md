# Migration Log

> Structured record of all structural migrations applied to this repository. A migration is any change that reorganizes, renames, moves, or removes files or folders in ways that break prior references or alter the canonical tree.

---

## Format

Each entry follows this structure:

```
### [MIG-XXXX] — YYYY-MM-DD
**Type:** Rename | Move | Remove | Restructure
**Scope:** Files or folders affected
**Reason:** Why this migration was necessary
**Breaking changes:** What breaks and what the replacement is
**Status:** Applied | Rolled back
```

---

## Log

### [MIG-0001] — 2026-05-24

**Type:** Restructure  
**Scope:** `docs/` — added `explanation/`, `how-to/`, `reference/`, `runbooks/`, `tutorials/` subdirectories with bilingual READMEs  
**Reason:** Align `docs/` structure with Diátaxis documentation framework. Prior flat structure did not distinguish between learning-oriented, task-oriented, and reference material.  
**Breaking changes:** Any direct links to `docs/` root expecting a flat file list are now incorrect. All content is organized under typed subdirectories.  
**Status:** Applied

### [MIG-0002] — 2026-05-24

**Type:** Remove  
**Scope:** `GOVERNANCE.md` — removed reference to `docs/reference/agent-contracts.md`; `canon/flawless-framework.md` — replaced reference to `docs/reference/agent-contracts.md` with `docs/reference/` pending note  
**Reason:** File did not exist. Broken references violate Exit Criterion 5 of the Flawless Writing standard.  
**Breaking changes:** Any agent relying on `docs/reference/agent-contracts.md` must be updated to point to `docs/reference/` until the file is formally created.  
**Status:** Applied

---

_Last updated: 2026-05-24_
