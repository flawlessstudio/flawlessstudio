# Archetype 05 — Hardware / Physical Product

> **Flawless Method** | `docs/archetypes/` | v1.0.0 | 2026-05-24

---

## Identity

| Field | Value |
|---|---|
| **Output type** | Physical product ready for manufacture and market — electronics, IoT device, medical device, consumer hardware, industrial equipment |
| **Novelty class** | Mark n — product development process known; form, function, and compliance path variable |
| **Primary standard** | IEC 62443 (IoT/industrial security), ISO 13485:2016 (medical devices), PMBOK 7 |
| **Sector** | Electronics, IoT, MedTech, Consumer Hardware, Industrial Equipment |

---

## Scope

All activities from product concept through industrial design, electronics and mechanical engineering, prototyping, testing, regulatory certification, manufacturing ramp, and product launch. Covers hardware-only and hardware+firmware products.

---

## Exclusions

| Out of scope | Redirect to |
|---|---|
| Complex system-of-systems (multiple subsystems) | Archetype 04 |
| Mass production optimisation after product launch | Archetype 06 |
| Software product without physical component | Archetype 01 |
| Industrial installation and commissioning | Archetype 03 |

---

## Primary Use Cases

- Developing a consumer IoT device from concept to mass production
- Engineering a medical device from design to CE/FDA clearance
- Creating an industrial sensor or controller product
- Launching a consumer electronics product
- Building a hardware MVP for a startup

---

## Phase Structure

| # | Phase | Key outputs |
|---|---|---|
| 1 | **Concept** | Product brief, target user, key requirements, risk assessment |
| 2 | **Industrial design** | Form factor, UX, CMF (colour, material, finish), concept models |
| 3 | **Engineering design** | Electrical schematic, PCB layout, mechanical CAD, BOM v1 |
| 4 | **Prototyping** | EVT (Engineering Validation Test) builds, bench testing |
| 5 | **DVT — Design validation** | DVT builds, functional and reliability testing, DFM review |
| 6 | **PVT — Production validation** | PVT builds, line validation, yield targets, final BOM |
| 7 | **Certification** | Regulatory testing (CE, FCC, UL, FDA, etc.), certifications issued |
| 8 | **Mass production & launch** | MP ramp, incoming QC, packaging, launch readiness review |

---

## Quality Controls

- Design FMEA (DFMEA) completed before DVT
- DFM (Design for Manufacturability) review with CM partner before PVT
- Reliability testing plan: HALT, HASS, or equivalent defined at concept
- BOM cost and availability review at each prototype stage
- Regulatory compliance matrix maintained from concept
- Firmware security review (OWASP IoT Top 10 or IEC 62443) before certification
- Golden sample archived per production batch

---

## Validation Gates

| Gate | Criteria | Who approves |
|---|---|---|
| **G1 — Concept freeze** | Requirements signed, risk assessment accepted, budget committed | Product Lead + Sponsor |
| **G2 — EVT pass** | All critical functions verified, no P0 defects unresolved | HW Lead + QA |
| **G3 — DVT pass** | Reliability targets met, DFM approved, regulatory path confirmed | HW Lead + Regulatory |
| **G4 — PVT pass** | Yield ≥ target, line validated, final BOM locked | Manufacturing + QA |
| **G5 — Launch readiness** | All certifications issued, MP stock available, support ready | PM + Regulatory + Ops |

---

## Resilience & Recovery

- Component dual-sourcing for critical single-source parts
- Engineering Change Order (ECO) process active from DVT
- Field failure reporting and CAPA process defined before launch
- Recall procedure documented and rehearsed before mass production
- Lead time risk register for long-lead components maintained from concept
- Regulatory change monitoring for all target markets

---

## International Validity

| Standard | Scope |
|---|---|
| IEC 62443 | Industrial and IoT cybersecurity |
| ISO 13485:2016 | Medical device quality management |
| IEC 60601 | Medical electrical equipment (safety) |
| CE Marking (EU) | Product safety and market access |
| FCC Part 15 | Radio frequency (US) |
| UL 94 / UL 508 | Flammability / industrial control (US) |
| RoHS / WEEE | Hazardous substances / e-waste (EU) |
| ISO 9001:2015 | Quality management |

---

## Lock Condition

**Locks when:** Mass production validated, all certifications issued, product launched, and first 90-day field quality review passed with no critical CAPAs open.

**Reopens when:** Field failure rate exceeds threshold, certification renewal required, component EOL forces redesign, or new market entry requires re-certification.

---

*[← Back to Archetype Index](README.md) | [Flawless Method](../README.md)*
