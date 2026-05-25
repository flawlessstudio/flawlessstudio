# Archetype Index — Flawless Method

> **Flawless Method** | `docs/archetypes/` | v1.0.0 | 2026-05-25

A complete taxonomy of 20 project archetypes. Each archetype defines scope, phase structure, quality controls, validation gates, resilience patterns, and international standards for a distinct class of professional work.

Use this index to identify the correct archetype before initiating any project. If a project spans multiple archetypes, declare a **primary** and one or more **secondary** archetypes in the project brief.

---

## Archetypes

### Block 1 — Product & Engineering

| # | Archetype | Output type | Key standards |
|---|---|---|---|
| [01](archetype_01_software_product.md) | **Software Product** | Shipped, monitored software product | ISO 25010, DORA, IEEE 730 |
| [02](archetype_02_research_development.md) | **Research & Development** | Validated prototype or knowledge asset | ISO 9001, Stage-Gate, NASA TRL |
| [03](archetype_03_construction_engineering.md) | **Construction & Engineering** | Commissioned built asset or infrastructure | ISO 9001, RIBA, FIDIC, Eurocodes |
| [04](archetype_04_manufacturing.md) | **Manufacturing** | Production-ready product at certified scale | ISO 9001, APQP, IATF 16949, GMP |
| [05](archetype_05_hardware_product.md) | **Hardware Product** | Certified, manufactured hardware product | IEC 62368, CE/FCC, ISO 13485 |

### Block 2 — Operations & Organisation

| # | Archetype | Output type | Key standards |
|---|---|---|---|
| [06](archetype_06_operations_process.md) | **Operations & Process** | Optimised, stable operational process | ISO 9001, Lean Six Sigma, BPMN 2.0 |
| [07](archetype_07_supply_chain_logistics.md) | **Supply Chain & Logistics** | Resilient, end-to-end supply chain | ISO 28000, SCOR, Incoterms 2020 |
| [08](archetype_08_organisational_change.md) | **Organisational Change** | Adopted organisational change | ADKAR, Kotter, ISO 9001 |
| [09](archetype_09_strategy_consulting.md) | **Strategy & Consulting** | Strategic recommendation or transformation roadmap | McKinsey 7S, MECE, BCG frameworks |
| [10](archetype_10_legal_contracts.md) | **Legal & Contracts** | Executed legal instrument or resolved dispute | Common Law, Civil Law, ICC Rules |

### Block 3 — Governance & Experience

| # | Archetype | Output type | Key standards |
|---|---|---|---|
| [11](archetype_11_regulatory_compliance.md) | **Regulatory / Compliance** | Implemented compliance programme or certification | ISO 37301, GDPR, ISO 27001 |
| [12](archetype_12_service_design_delivery.md) | **Service Design / Delivery** | Designed, piloted, and scaled service | ITIL 4, Double Diamond, ISO 9241 |
| [13](archetype_13_design_brand_creative.md) | **Design / Brand / Creative** | Brand identity, design system, or creative asset | WCAG 2.2, ISO 9241, W3C Design Tokens |
| [14](archetype_14_content_media_publishing.md) | **Content / Media / Publishing** | Content programme or publishing operation | WCAG 2.2, GDPR, FTC/ASA guidelines |
| [15](archetype_15_event_management.md) | **Event Management** | Delivered event — conference, launch, or experience | ISO 20121, APEX/ANSI, H&S regulations |

### Block 4 — Data, Technology & Finance

| # | Archetype | Output type | Key standards |
|---|---|---|---|
| [16](archetype_16_data_analytics.md) | **Data / Analytics** | Operational data product or analytics capability | DAMA-DMBOK2, ISO 8000, GDPR |
| [17](archetype_17_ai_ml.md) | **AI / ML** | Trained, evaluated, and deployed ML or AI system | EU AI Act, ISO/IEC 42001, NIST AI RMF |
| [18](archetype_18_security.md) | **Security** | Implemented security programme or certification | ISO 27001, NIST CSF 2.0, OWASP ASVS 5.0 |
| [19](archetype_19_infrastructure.md) | **Infrastructure** | Deployed, monitored cloud or on-premise infrastructure | AWS/GCP/Azure WAF, Terraform, SRE |
| [20](archetype_20_finance_investment.md) | **Finance / Investment** | Financial model, investment decision, or financial product | IFRS, CFA, MiFID II, ISO 31000 |

---

## How to Use

1. **Identify** the primary output of your project.
2. **Match** it to the archetype whose output type most closely aligns.
3. **Declare** the archetype in your project brief (`archetype: XX`).
4. **Apply** the phase structure, quality controls, and validation gates from the archetype file.
5. **Escalate** to secondary archetypes for any scope that crosses into another domain.

---

## Selection Decision Tree

```
What is the primary output?
│
├── Software / app / API ──────────────────────────── 01 Software Product
├── Prototype / experiment / knowledge ────────────── 02 R&D
├── Built physical structure ──────────────────────── 03 Construction
├── Manufactured goods at scale ───────────────────── 04 Manufacturing
├── Hardware device / embedded system ─────────────── 05 Hardware Product
├── Optimised process / operational capability ─────── 06 Operations
├── End-to-end supply chain ────────────────────────── 07 Supply Chain
├── Adopted organisational change ──────────────────── 08 Org Change
├── Strategic recommendation / roadmap ─────────────── 09 Strategy
├── Legal instrument / dispute resolution ──────────── 10 Legal
├── Compliance programme / certification ───────────── 11 Regulatory
├── Designed and scaled service ────────────────────── 12 Service Design
├── Brand identity / design system / creative ──────── 13 Design & Brand
├── Content programme / publication ────────────────── 14 Content & Media
├── Live event / conference / launch ───────────────── 15 Event Management
├── Data product / analytics capability ────────────── 16 Data & Analytics
├── ML model / AI system ───────────────────────────── 17 AI / ML
├── Security programme / hardened system ───────────── 18 Security
├── Cloud or on-premise infrastructure ─────────────── 19 Infrastructure
└── Investment decision / financial product ─────────── 20 Finance
```

---

## Novelty Classes

| Class | Definition | Typical archetypes |
|---|---|---|
| **Mark 1** | Output type not previously built; form emergent | 02, 05, 13, 17 |
| **Mark n** | Output type known; parameters variable | 01, 03, 04, 06, 07, 08, 09, 10, 11, 12, 14, 15, 16, 18, 19, 20 |
| **Mark 1–n** | Output type partially known; some parameters emergent | 12, 17 |

---

## Governance

| Field | Value |
|---|---|
| **Owner** | Flawless Studio |
| **Version** | 1.0.0 |
| **Created** | 2026-05-25 |
| **Review trigger** | New archetype needed, existing archetype scope conflict, or annual review |
| **Source** | [Flawless Method](../README.md) |

---

*[Flawless Method](../README.md)*
