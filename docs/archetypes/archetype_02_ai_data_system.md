# Archetype 02 — AI / Data System

> **Flawless Method** | `docs/archetypes/` | v1.0.0 | 2026-05-24

---

## Identity

| Field | Value |
|---|---|
| **Output type** | AI model, ML pipeline, data platform, analytics system, or AI-powered product feature |
| **Novelty class** | Mark 1 — target performance emergent; model behaviour non-deterministic |
| **Primary standard** | ISO/IEC 42001:2023 (AI management), NIST AI RMF 1.0, EU AI Act 2024 |
| **Sector** | AI/ML, Data Engineering, Analytics, Healthcare AI, Fintech AI, Autonomous Systems |

---

## Scope

All activities from problem framing and data discovery through data engineering, model development, evaluation, deployment, monitoring, and governance of AI/ML systems and data platforms. Covers supervised, unsupervised, reinforcement learning, generative AI, and classical analytics pipelines.

---

## Exclusions

| Out of scope | Redirect to |
|---|---|
| Software product where AI is a minor feature | Archetype 01 |
| Pure data warehouse with no model output | Archetype 10 |
| Research AI without deployment target | Archetype 07 |
| Regulatory compliance for AI system only | Archetype 11 |

---

## Primary Use Cases

- Building and deploying a machine learning model (classification, regression, generation)
- Designing and shipping an AI agent or multi-agent orchestration system
- Constructing a data platform (lakehouse, warehouse, streaming pipeline)
- Implementing a generative AI feature (LLM, RAG, fine-tuning)
- Establishing an MLOps platform for model lifecycle management

---

## Phase Structure

| # | Phase | Key outputs |
|---|---|---|
| 1 | **Problem framing** | AI use case definition, success criteria, risk classification (EU AI Act tier) |
| 2 | **Data discovery** | Data inventory, quality assessment, lineage map, PII audit |
| 3 | **Data engineering** | Pipelines, feature store, data contracts, data quality checks |
| 4 | **Model development** | Experimentation, training, evaluation (bias, fairness, performance) |
| 5 | **Validation** | Model card, independent evaluation, red-teaming, adversarial testing |
| 6 | **Deployment** | CI/CD for ML, shadow mode, canary rollout, inference infrastructure |
| 7 | **Monitoring & governance** | Drift detection, performance monitoring, human oversight, audit log |

---

## Quality Controls

- AI risk classification completed before development (EU AI Act Article 6–9)
- Data quality scorecard maintained (completeness, accuracy, freshness, consistency)
- Model evaluation includes fairness and bias metrics (demographic parity, equalised odds)
- Model card published for every model entering production
- SBOM and model provenance documented
- Human oversight mechanism active for high-risk AI systems
- Adversarial testing completed before production deployment

---

## Validation Gates

| Gate | Criteria | Who approves |
|---|---|---|
| **G1 — Problem framing** | Use case validated, risk tier confirmed, data feasibility assessed | Product Owner + AI Lead |
| **G2 — Data readiness** | Data quality score ≥ threshold, PII handled, lineage documented | Data Lead + DPO |
| **G3 — Model evaluation** | Performance targets met, bias within acceptable bounds | ML Lead + Ethics Reviewer |
| **G4 — Deployment** | Shadow mode passed, model card published, rollback mechanism tested | MLOps Lead + CISO |
| **G5 — Governance** | Drift monitoring active, audit log verified, human override tested | AI Governance Lead |

---

## Resilience & Recovery

- Model rollback to previous version within 15 minutes
- Shadow mode deployment for all high-risk model changes
- Fallback to rule-based system if model confidence below threshold
- Data pipeline failure alerting with auto-retry and dead-letter queue
- Continuous drift monitoring with automatic escalation
- Incident classification: model failure, data failure, bias event, security event

---

## International Validity

| Standard | Scope |
|---|---|
| ISO/IEC 42001:2023 | AI management system |
| EU AI Act 2024 | Risk classification and compliance (EU) |
| NIST AI RMF 1.0 | AI risk management (US) |
| ISO/IEC 27001:2022 | Information security |
| GDPR / CCPA | Data privacy |
| ISO/IEC 25010:2023 | Software quality (applied to AI systems) |
| IEEE 7000-2021 | Ethical AI design |
| OECD AI Principles | Trustworthy AI (international) |

---

## Lock Condition

**Locks when:** Model in production, monitoring active, drift baseline set, model card published, governance log running, and first 30-day performance review passed.

**Reopens when:** Model performance degrades below threshold, bias event detected, regulatory change affects system, or major data source change requires retraining.

---

*[← Back to Archetype Index](README.md) | [Flawless Method](../README.md)*
