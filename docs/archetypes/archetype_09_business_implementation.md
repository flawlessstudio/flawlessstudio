# Archetype 09 — Business Implementation

> **Flawless Method** | `docs/archetypes/` | v1.0.0 | 2026-05-24

---

## Identity

| Field | Value |
|---|---|
| **Output type** | Implemented internal business capability, process, or packaged system |
| **Novelty class** | Mark n — solution type known; integration, configuration, and migration variable |
| **Primary standard** | PRINCE2 7th Ed., PMBOK 7, BABOK v3, MSP 5th Ed. |
| **Sector** | Corporate, Public Sector, Finance, Consulting, Operations, Healthcare |

---

## Scope

All activities from solution selection through configuration, data migration, integration, testing, training, cutover, hypercare, and handover to BAU. Covers ERP, CRM, HRMS, and other packaged or configured business solutions.

---

## Exclusions

| Out of scope | Redirect to |
|---|---|
| Bespoke software product development | Archetype 01 |
| Organisational transformation without known solution | Archetype 08 |
| IT infrastructure deployment | Archetype 10 |
| Regulatory compliance programme only | Archetype 11 |

---

## Primary Use Cases

- ERP or CRM rollout (SAP, Salesforce, Dynamics 365)
- HRMS or Finance system implementation
- Internal process automation deployment
- Capability deployment across business units
- Vendor product rollout with configuration and migration

---

## Phase Structure

| # | Phase | Key outputs |
|---|---|---|
| 1 | **Solution selection** | Requirements baseline, vendor evaluation, business case, contract |
| 2 | **Design** | Solution design, data model, integration design, process maps |
| 3 | **Configuration & build** | System configured, integrations built, unit tested |
| 4 | **Data migration** | Migration strategy, cleansing, dry run, sign-off |
| 5 | **Testing** | SIT, UAT, performance test, defect resolution |
| 6 | **Training** | Training materials, key user training, end user training |
| 7 | **Cutover** | Cutover plan executed, go/no-go decision, go-live |
| 8 | **Hypercare & closure** | Hypercare support, stabilisation KPIs, BAU handover |

---

## Quality Controls

- Requirements traceability matrix (RTM) from business need to UAT
- Migration accuracy threshold defined and tested in dry run (≥ 99% for critical data)
- UAT sign-off required from business owners before cutover decision
- Cutover checklist completed and verified before go-live
- Hypercare KPIs defined (ticket volume, resolution time, system availability)
- Vendor SLA active from go-live
- Training completion rate ≥ 90% before cutover

---

## Validation Gates

| Gate | Criteria | Who approves |
|---|---|---|
| **G1 — Solution design** | Design approved, integrations scoped, data model agreed | Business Owner + IT Lead |
| **G2 — Migration dry run** | Data accuracy ≥ threshold, no critical failures | Data Lead + Business Owner |
| **G3 — UAT complete** | All P0/P1 defects resolved, UAT signed off | Business Owner + PM |
| **G4 — Go/no-go** | Cutover checklist clear, rollback plan ready, support resourced | Steering Committee |
| **G5 — BAU handover** | Hypercare KPIs met, stabilisation confirmed | PM + Operations Lead |

---

## Resilience & Recovery

- Rollback plan tested and rehearsed before cutover
- Parallel run for critical financial or operational systems where feasible
- Vendor escalation path and SLA breach process documented
- Backup key users identified and trained before go-live
- Data backup validated immediately before cutover

---

## International Validity

| Standard | Scope |
|---|---|
| PRINCE2 7th Ed. | Project governance and delivery |
| PMBOK 7th Ed. | Project management principles |
| BABOK v3 | Business analysis and requirements |
| MSP 5th Ed. | Programme management |
| ISO/IEC 20000 | IT service management (post go-live) |
| GDPR / CCPA | Data protection during migration |
| ISO 27001:2022 | Information security |

---

## Lock Condition

**Locks when:** System stable in BAU, hypercare closed, vendor SLA active, and operational ownership formally transferred.

**Reopens when:** Major upgrade cycle, process redesign, merger requiring system consolidation, or compliance change forces configuration update.

---

*[← Back to Archetype Index](README.md) | [Flawless Method](../README.md)*
