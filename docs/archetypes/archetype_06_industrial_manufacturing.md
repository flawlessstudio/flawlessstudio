# Archetype 06 — Industrial / Manufacturing

> **Flawless Method** | `docs/archetypes/` | v1.0.0 | 2026-05-24

---

## Identity

| Field | Value |
|---|---|
| **Output type** | Scaled production system, manufacturing line, or industrial process |
| **Novelty class** | Mark n — process type known; product, volume, and site variable |
| **Primary standard** | ISO 9001:2015, IATF 16949, APQP, Lean / Six Sigma, ISO 45001 |
| **Sector** | Automotive, FMCG, Electronics, Chemical, Food & Beverage, Industrial Equipment |

---

## Scope

All activities from production system design through tooling, pilot run, ramp-up, steady-state manufacturing operations, quality control, and continuous improvement. Covers discrete, process, and hybrid manufacturing models.

---

## Exclusions

| Out of scope | Redirect to |
|---|---|
| Hardware product development before manufacturing | Archetype 05 |
| Construction of the production facility | Archetype 03 |
| Regulatory compliance programme only | Archetype 11 |
| Supply chain design without production system | Archetype 19 |

---

## Primary Use Cases

- Launching a new manufacturing line for a product
- Scaling a product from pilot to mass production
- Lean / Six Sigma transformation of a factory floor
- Quality management system (QMS) implementation for a plant
- Introducing a new process technology or automation system

---

## Phase Structure

| # | Phase | Key outputs |
|---|---|---|
| 1 | **Process design** | Process FMEA, control plan, capacity model, layout design |
| 2 | **Tooling & setup** | Tooling specifications, machine procurement, facility readiness |
| 3 | **Pilot run** | First article inspection (FAI), process capability study (Cpk) |
| 4 | **Ramp-up** | Yield tracking, OEE baseline, line balancing, defect pareto |
| 5 | **Steady state** | SPC active, operator training, maintenance schedule, KPIs live |
| 6 | **Continuous improvement** | Kaizen events, waste reduction, cost-down roadmap, ECO process |

---

## Quality Controls

- Process FMEA (PFMEA) completed and maintained before production start
- Process capability index Cpk ≥ 1.33 for all critical characteristics
- OEE tracked from pilot run; target defined before ramp-up
- Statistical Process Control (SPC) charts active for critical parameters
- PPAP (Production Part Approval Process) completed where applicable
- Golden sample archived per production batch
- Operator qualification records maintained
- Corrective and Preventive Action (CAPA) process active

---

## Validation Gates

| Gate | Criteria | Who approves |
|---|---|---|
| **G1 — Process design** | PFMEA approved, control plan agreed, layout signed off | Process Engineer + QA |
| **G2 — Pilot run** | FAI passed, Cpk ≥ 1.33, no P0 defects unresolved | QA Lead + Plant Manager |
| **G3 — PPAP / Customer approval** | All PPAP elements submitted and approved | QA + Customer |
| **G4 — Ramp-up** | Yield ≥ target, OEE ≥ baseline, no critical CAPAs open | Operations + QA |
| **G5 — Steady state** | SPC active, maintenance schedule running, KPIs met for 30 days | Plant Manager |

---

## Resilience & Recovery

- Dual-sourcing for critical raw materials and components
- Preventive maintenance schedule with MTBF targets
- Inventory buffer policy for high-risk materials
- Engineering Change Order (ECO) process active from pilot
- Field failure / customer return analysis loop (8D / CAPA)
- Business continuity plan for single-point-of-failure equipment

---

## International Validity

| Standard | Scope |
|---|---|
| ISO 9001:2015 | Quality management system |
| IATF 16949:2016 | Automotive quality management |
| APQP / PPAP | Advanced product quality planning (AIAG) |
| Lean / Six Sigma | Waste reduction and process capability |
| ISO 45001:2018 | Occupational health and safety |
| ISO 14001:2015 | Environmental management |
| ISO 50001:2018 | Energy management |
| GMP (21 CFR / EU GMP) | Good manufacturing practice (pharma, food) |

---

## Lock Condition

**Locks when:** Production is stable, SPC active, OEE ≥ target, no critical CAPAs open, and 30-day steady-state review passed.

**Reopens when:** New product introduction, major process change, customer quality escalation, regulatory audit finding, or capacity expansion required.

---

*[← Back to Archetype Index](README.md) | [Flawless Method](../README.md)*
