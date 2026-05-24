# Archetype 04 — Engineering / Systems

> **Flawless Method** | `docs/archetypes/` | v1.0.0 | 2026-05-24

---

## Identity

| Field | Value |
|---|---|
| **Output type** | Engineered system — complex product, system-of-systems, or integrated technical solution |
| **Novelty class** | Mark 1 — system behaviour and integration emergent; requirements partially defined |
| **Primary standard** | ISO/IEC/IEEE 15288:2023 (systems engineering), INCOSE SE Handbook v4, EIA-632 |
| **Sector** | Aerospace, Defence, Rail, Automotive, Nuclear, Industrial Automation, Space |

---

## Scope

All activities from mission/concept definition through requirements engineering, system architecture, subsystem design, integration, verification, validation, and deployment of a complex engineered system. Covers hardware, software, firmware, and human factors as integrated system elements.

---

## Exclusions

| Out of scope | Redirect to |
|---|---|
| Pure software product without physical integration | Archetype 01 |
| Physical product without system-of-systems complexity | Archetype 05 |
| Construction of the facility housing the system | Archetype 03 |
| Manufacturing at scale after system is validated | Archetype 06 |

---

## Primary Use Cases

- Developing an aerospace or defence system (aircraft, satellite, weapon system)
- Engineering an autonomous vehicle or robotics system
- Designing a nuclear plant control system
- Integrating a rail signalling and control system
- Delivering a complex industrial automation system

---

## Phase Structure

| # | Phase (ISO 15288 aligned) | Key outputs |
|---|---|---|
| 1 | **Concept** | Mission statement, stakeholder needs, feasibility, ConOps |
| 2 | **System requirements** | System Requirements Specification (SyRS), use cases, CONOPS |
| 3 | **Architecture** | System architecture, interface control documents (ICD), FMEA |
| 4 | **Detailed design** | Subsystem design, hardware/software specifications, DFM/DFT |
| 5 | **Integration** | Assembly, subsystem integration, integration test plan |
| 6 | **Verification** | Test and evaluation (T&E), verification matrix, qualification |
| 7 | **Validation** | System-level testing, operational trial, V&V report |
| 8 | **Deployment & operations** | Fielding, training, maintenance plan, ILS |

---

## Quality Controls

- Requirements traceability matrix (RTM) maintained from stakeholder need to test
- Failure Mode and Effects Analysis (FMEA) completed at system and subsystem level
- Interface Control Documents (ICDs) baselined and change-controlled
- Independent technical review at each phase gate (Preliminary Design Review, Critical Design Review)
- Verification and Validation (V&V) plan agreed before detailed design
- Safety case maintained and updated through all phases
- Configuration management system active from architecture phase

---

## Validation Gates

| Gate | Criteria | Who approves |
|---|---|---|
| **SRR** — System Requirements Review | SyRS complete, no unresolved TBDs on critical requirements | Chief Engineer + Customer |
| **PDR** — Preliminary Design Review | Architecture frozen, FMEA complete, design-to-cost feasible | Program Manager + IPT |
| **CDR** — Critical Design Review | Detailed design complete, all ICDs baselined, build authorised | Chief Engineer + Customer |
| **TRR** — Test Readiness Review | Test plan approved, facilities ready, test articles available | QA Lead + T&E Lead |
| **FRR** — Flight/Field Readiness Review | All tests passed, safety case closed, deployment authorised | Program Manager + Safety |

---

## Resilience & Recovery

- Formal change control board (CCB) for all baseline changes
- Risk register with probability × consequence scoring, reviewed monthly
- Technology Readiness Level (TRL) gate: minimum TRL 6 before CDR
- Regression test suite for software changes post-CDR
- Contingency design margins (mass, power, thermal) maintained until CDR
- Fallback subsystem design identified for high-risk elements

---

## International Validity

| Standard | Scope |
|---|---|
| ISO/IEC/IEEE 15288:2023 | Systems engineering processes |
| INCOSE SE Handbook v4 | Systems engineering best practice |
| MIL-STD-882E | System safety (US DoD, internationally adopted) |
| ARP 4754A | Civil aircraft system development (FAA/EASA) |
| IEC 61508 | Functional safety (SIL) |
| ISO 26262 | Functional safety — automotive |
| ECSS | European space standards |
| EIA-632 | Processes for engineering a system |

---

## Lock Condition

**Locks when:** System deployed, V&V report accepted, safety case closed, ILS baseline established, and first operational review passed.

**Reopens when:** Operational failure, safety finding, regulatory change, capability upgrade required, or end-of-life assessment triggers.

---

*[← Back to Archetype Index](README.md) | [Flawless Method](../README.md)*
