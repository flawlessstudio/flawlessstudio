# Archetype 16 — Data / Analytics

> **Flawless Method** | `docs/archetypes/` | v1.0.0 | 2026-05-25

---

## Identity

| Field | Value |
|---|---|
| **Output type** | Operational data product, analytics capability, or insight programme |
| **Novelty class** | Mark n — data sources known; schema, pipeline, and insight model variable |
| **Primary standard** | DAMA-DMBOK2, ISO 8000, DCAM, dbt best practices |
| **Sector** | Any — Tech, Finance, Healthcare, Retail, Government, Media |

---

## Scope

All activities from data discovery and profiling through pipeline design, modelling, visualisation, and operationalisation of data products. Covers batch and streaming pipelines, data warehouses, data lakes, BI reporting, and self-service analytics.

---

## Exclusions

| Out of scope | Redirect to |
|---|---|
| Machine learning model development | Archetype 17 |
| Data security and privacy controls only | Archetype 18 |
| Software product with data as a feature | Archetype 01 |
| Regulatory reporting as primary output | Archetype 11 |

---

## Primary Use Cases

- Data warehouse or lakehouse design and build
- BI dashboard and reporting programme
- Real-time streaming analytics pipeline
- Data quality and governance programme
- Self-service analytics platform rollout

---

## Phase Structure

| # | Phase | Key outputs |
|---|---|---|
| 1 | **Discovery** | Data inventory, source profiling, use case prioritisation, data contract draft |
| 2 | **Architecture** | Data model, pipeline design, tool selection, governance framework |
| 3 | **Build** | Pipelines implemented, models built, tests written, orchestration configured |
| 4 | **Quality & governance** | DQ rules active, lineage documented, data dictionary published |
| 5 | **Visualisation** | Dashboards and reports delivered, user acceptance testing complete |
| 6 | **Operationalisation** | Monitoring active, SLAs defined, ownership transferred to data team |

---

## Quality Controls

- Data contracts defined and signed off for all source systems before build
- Pipeline tests cover null checks, row counts, schema drift, and business logic
- Data lineage documented end-to-end for all critical data products
- Data dictionary published and owner-assigned before go-live
- Dashboard UAT completed with ≥ 3 representative end users
- Data quality SLA defined and monitored from day 1 of production
- PII identified, classified, and access-controlled before any data product goes live

---

## Validation Gates

| Gate | Criteria | Who approves |
|---|---|---|
| **G1 — Discovery** | Use cases prioritised, data contracts drafted | Data Lead + Business Owner |
| **G2 — Architecture** | Data model approved, tools confirmed, governance agreed | Data Architect + CTO/CDO |
| **G3 — Build** | Pipelines passing all tests, models peer-reviewed | Data Engineer + Data Lead |
| **G4 — Quality** | DQ rules active, lineage complete, dictionary published | Data Lead + Data Governance |
| **G5 — Operationalisation** | Monitoring live, SLAs agreed, ownership transferred | Data Lead + Sponsor |

---

## Resilience & Recovery

- Pipeline failure alerting and on-call rotation defined
- Data backfill procedure documented and tested
- Rollback plan for breaking schema changes
- Disaster recovery plan for data warehouse / lakehouse
- Data retention and deletion policy aligned to GDPR / regulatory requirements

---

## International Validity

| Standard | Scope |
|---|---|
| DAMA-DMBOK2 | Data management body of knowledge |
| ISO 8000 | Data quality |
| DCAM | Data management capability assessment |
| GDPR / CCPA | Personal data handling in pipelines |
| dbt best practices | SQL transformation and testing |
| Apache Iceberg / Delta Lake | Open table format standards |

---

## Lock Condition

**Locks when:** Data product is in production, monitoring active, SLAs met for 30 days, and ownership transferred to BAU data team.

**Reopens when:** New source system, schema change, use case expansion, data quality SLA breach, or regulatory change.

---

*[← Back to Archetype Index](README.md) | [Flawless Method](../README.md)*
