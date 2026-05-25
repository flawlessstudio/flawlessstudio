# Archetype 17 — AI / ML

> **Flawless Method** | `docs/archetypes/` | v1.0.0 | 2026-05-25

---

## Identity

| Field | Value |
|---|---|
| **Output type** | Trained, evaluated, and deployed ML model or AI-powered system |
| **Novelty class** | Mark 1–n — problem defined; data, architecture, and performance threshold variable |
| **Primary standard** | ML Ops (Google, Microsoft), EU AI Act, IEEE 7010, ISO/IEC 42001:2023 |
| **Sector** | Any — Tech, Finance, Healthcare, Retail, Manufacturing, Government |

---

## Scope

All activities from problem framing and data preparation through model development, evaluation, deployment, monitoring, and governance. Covers supervised/unsupervised ML, deep learning, LLM fine-tuning, RAG systems, and AI agent architectures.

---

## Exclusions

| Out of scope | Redirect to |
|---|---|
| Data pipeline without ML component | Archetype 16 |
| Software product using an ML model as a feature | Archetype 01 |
| AI compliance / regulatory programme only | Archetype 11 |
| Research without production deployment | Mark this as prototype; use Archetype 02 |

---

## Primary Use Cases

- Classification or regression model for business decision support
- LLM fine-tuning or RAG system for enterprise knowledge
- Computer vision system for quality inspection or recognition
- Recommendation engine for product or content
- AI agent system with tool use and orchestration

---

## Phase Structure

| # | Phase | Key outputs |
|---|---|---|
| 1 | **Problem framing** | ML problem statement, success metrics, baseline, feasibility assessment |
| 2 | **Data preparation** | Training/validation/test splits, feature engineering, data quality audit |
| 3 | **Model development** | Experiments tracked, model selected, hyperparameters tuned |
| 4 | **Evaluation** | Performance report, bias audit, explainability analysis, threshold decision |
| 5 | **Deployment** | Model served (batch or real-time), API documented, integration tested |
| 6 | **Monitoring** | Data drift detection, model performance tracking, retraining pipeline |
| 7 | **Governance** | Model card published, risk register updated, EU AI Act classification confirmed |

---

## Quality Controls

- Success metrics and acceptance threshold defined before model development begins
- Experiment tracking active from first training run (MLflow, W&B, or equivalent)
- Test set held out and never used during development
- Bias and fairness audit completed before production deployment
- Model card published covering intended use, limitations, and performance
- Data drift and model degradation monitoring active from day 1 of production
- EU AI Act risk classification documented and compliance path confirmed

---

## Validation Gates

| Gate | Criteria | Who approves |
|---|---|---|
| **G1 — Problem framing** | Success metrics agreed, baseline established, data feasibility confirmed | ML Lead + Business Owner |
| **G2 — Data ready** | Training data quality audited, splits defined, features documented | ML Lead + Data Lead |
| **G3 — Model selected** | Best model meets acceptance threshold on validation set | ML Lead + Technical Lead |
| **G4 — Evaluation** | Bias audit passed, explainability reviewed, no critical failures | ML Lead + Ethics/Legal |
| **G5 — Production** | Monitoring live, model card published, retraining pipeline tested | ML Lead + Sponsor |

---

## Resilience & Recovery

- Model rollback procedure documented and tested before go-live
- Shadow mode deployment for high-risk models before full cutover
- Retraining trigger defined (drift threshold, time-based, or event-based)
- Human-in-the-loop escalation path for low-confidence predictions
- Incident response plan for model failure or adversarial attack

---

## International Validity

| Standard | Scope |
|---|---|
| EU AI Act (2024) | Risk classification and compliance requirements |
| ISO/IEC 42001:2023 | AI management systems |
| IEEE 7010 | Wellbeing metrics for AI systems |
| NIST AI RMF | AI risk management framework (US) |
| ISO/IEC 23053 | Framework for AI systems using ML |
| Google / Microsoft MLOps | Production ML best practices |

---

## Lock Condition

**Locks when:** Model in production, monitoring active, model card published, and performance stable for 30 days.

**Reopens when:** Data drift exceeds threshold, performance degrades below acceptance, regulatory change, or new use case requires retraining.

---

*[← Back to Archetype Index](README.md) | [Flawless Method](../README.md)*
