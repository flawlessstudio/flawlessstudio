# Archetype 01 — Software / Digital Product

> **Flawless Method** | `docs/archetypes/` | v1.0.0 | 2026-05-24

---

## Identity

| Field | Value |
|---|---|
| **Output type** | Shipped software product or digital service (web app, mobile app, API, SaaS platform, embedded software) |
| **Novelty class** | Mark n — product type known, requirements and architecture variable |
| **Primary standard** | ISO/IEC 25010:2023 (product quality), PMBOK 7, SAFe 6.0 |
| **Sector** | Technology, SaaS, Enterprise IT, Fintech, Healthtech, E-commerce |

---

## Scope

All activities from product discovery through design, development, testing, release, and post-launch iteration of a software product or digital service. Covers web, mobile, API, embedded, and hybrid delivery models.

---

## Exclusions

| Out of scope | Redirect to |
|---|---|
| AI/ML model development as the primary output | Archetype 02 |
| IT infrastructure deployment without product delivery | Archetype 10 |
| Internal tooling without external users | Archetype 09 |
| Hardware with embedded firmware as primary output | Archetype 05 |

---

## Primary Use Cases

- Launching a SaaS platform from zero to v1
- Building a mobile application (iOS, Android, cross-platform)
- Developing a public or partner-facing REST/GraphQL API
- Shipping a major version of an existing product
- Migrating a legacy system to a modern architecture

---

## Phase Structure

| # | Phase | Key outputs |
|---|---|---|
| 1 | **Discovery** | Problem statement, user research, opportunity sizing, product vision |
| 2 | **Definition** | PRD, user stories, acceptance criteria, technical feasibility |
| 3 | **Architecture** | System design, ADRs, tech stack decision, non-functional requirements |
| 4 | **Development** | Iterative build (sprints/cycles), code review, unit + integration tests |
| 5 | **Quality assurance** | E2E testing, performance, security scan, accessibility audit |
| 6 | **Release** | Staging deploy, UAT, release notes, rollout strategy |
| 7 | **Post-launch** | Monitoring, incident response, user feedback loop, iteration backlog |

---

## Quality Controls

- Definition of Done agreed and enforced for every user story
- Code review required before merge (min 1 peer reviewer)
- Automated test coverage ≥ 80% for critical paths
- Security scan (SAST/DAST) run on every release candidate
- Accessibility audit (WCAG 2.1 AA) before public release
- Performance baseline defined and regression-tested
- Dependency audit (SBOM) generated per release

---

## Validation Gates

| Gate | Criteria | Who approves |
|---|---|---|
| **G1 — Discovery** | Problem validated, scope bounded, stakeholder alignment | Product Owner + Sponsor |
| **G2 — Architecture** | ADRs signed, NFRs accepted, no unresolved blockers | Tech Lead + Architect |
| **G3 — Feature complete** | All P0/P1 stories done, test coverage met | QA Lead + Product Owner |
| **G4 — Release** | Staging passed, security cleared, rollback plan ready | Release Manager + CISO |
| **G5 — Post-launch** | Error rate < threshold, SLOs met for 7 days | Engineering Lead |

---

## Resilience & Recovery

- Feature flags for safe incremental rollout and instant rollback
- Canary / blue-green deployment strategy defined before release
- Incident runbook published and tested before go-live
- SLOs and SLAs defined with alerting thresholds
- Disaster recovery plan with RTO and RPO targets
- On-call rotation active from day of launch

---

## International Validity

| Standard | Scope |
|---|---|
| ISO/IEC 25010:2023 | Software product quality model |
| ISO/IEC 27001:2022 | Information security management |
| GDPR / CCPA | Data privacy (EU and US) |
| WCAG 2.1 AA | Web accessibility |
| OWASP Top 10 | Security vulnerability baseline |
| SOC 2 Type II | Trust services (US cloud products) |
| PMBOK 7th Ed. | Project management |
| SAFe 6.0 | Agile at scale |

---

## Lock Condition

**Locks when:** Product is live, SLOs met for 7 consecutive days, post-launch backlog triaged, and handoff to steady-state operations complete.

**Reopens when:** Major version planned, architecture change required, security incident triggers redesign, or compliance obligation forces rebuild.

---

*[← Back to Archetype Index](README.md) | [Flawless Method](../README.md)*
