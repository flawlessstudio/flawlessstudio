# Flawless Terminology

> Canonical glossary of all terms used across the Flawless ecosystem. Every term defined here is the single authoritative definition. No synonym, paraphrase, or alternative usage is valid unless explicitly listed.

---

## Core terms

**Canon**  
The set of immutable documents that define how Flawless Studio thinks, builds, and operates. Canon is the highest-priority reference in any conflict. Changes require formal governance approval.

**Flawless Filter**  
The four-question quality gate applied to every artifact: Is it the simplest correct solution? Is it bilingual and documented? Is it traceable to a canonical source? Is it free of redundancy?

**Flawless Framework**  
The core operating framework of Flawless Studio. Defines the seven principles, five system layers, and quality bar that govern all work.

**Flawless Method**  
The six-step decision-making loop: Understand → Scope → Plan → Execute → Verify → Document. Applied to every problem, system, and change.

**Flawless Writing**  
The writing standard that defines the optimal level of eight dimensions — Tone, Structure, Audience, Density, Temporal perspective, Objective, Language, and Success — calibrated per file, audience, and purpose.

**Fractal coherence**  
The principle that every layer of the system (file, folder, repo, ecosystem) follows the same structural logic. A file should be recognizable as Flawless at any level of zoom.

**Registry**  
A structured, maintained catalog of active tools, stacks, or signals for a specific domain. Registries are living documents — they are updated, audited, and promoted through defined criteria.

**Watchlist**  
The pre-registry tier. Tools or signals that meet interest criteria but not yet promotion criteria. Watchlist entries are reviewed at each audit cycle.

---

## System layers

**Canon layer**  
Immutable truth. Documents in `canon/` define the rules of the system itself.

**Registry layer**  
Active state of tools and stacks. Documents in `registries/` reflect current operational choices.

**Ecosystem layer**  
Map of all repos and their relationships. Documents in `ecosystem/` reflect the current structure and status of the full Flawless Studio portfolio.

**Docs layer**  
Operational knowledge: decisions, runbooks, audits, explanations, tutorials, references. Documents in `docs/` support day-to-day operation.

**Agents layer**  
Automated systems operating under defined contracts. Agent contracts are formal documents specifying scope, authority, and constraints for each agent.

---

## Bilingual policy terms

**EN (authoritative)**  
English is the authoritative language for all canonical documents. In any conflict between EN and ES versions, EN prevails.

**ES (parity pair)**  
Spanish translation maintained in parallel. Denoted by the `.es.md` suffix. Required for all canon, governance, and root-level canonical files.

**Bilingual parity**  
The state in which every required EN file has a corresponding `.es.md` pair of equivalent content. Verified automatically by `validate-bilingual-parity.yml`.

---

## Governance terms

**ADR (Architecture Decision Record)**  
A structured record of a significant architectural or operational decision. Stored in `docs/decisions/`. Format: context → decision → rationale → consequences.

**Audit**  
A scheduled or triggered review of the canonical tree for accuracy, parity, and structural integrity. Outputs a dated report in `docs/audits/`.

**Push-to-main**  
The current merge policy: direct commits to `main` are permitted for solo operation. This policy is documented in `GOVERNANCE.md` and subject to revision.

---

*Part of the [Flawless canon](../CANON.md).*
