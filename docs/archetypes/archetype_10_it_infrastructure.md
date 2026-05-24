# Archetype 10 — IT Infrastructure

> **Flawless Method** | `docs/archetypes/` | v1.0.0 | 2026-05-24

---

## Identity

| Field | Value |
|---|---|
| **Output type** | IT infrastructure platform — cloud, network, identity, compute, storage, or security |
| **Novelty class** | Mark n — infrastructure type known; scale, security posture, and integration variable |
| **Primary standard** | ITIL 4, ISO/IEC 20000-1:2018, ISO/IEC 27001:2022, TOGAF 10 |
| **Sector** | IT, Cloud, Enterprise, Telecom, Cybersecurity, Financial Services |

---

## Scope

All activities from infrastructure assessment through design, procurement, deployment, security hardening, testing, and operational handover. Covers on-premise, cloud (IaaS/PaaS), hybrid, and multi-cloud environments.

---

## Exclusions

| Out of scope | Redirect to |
|---|---|
| Software product development using the infrastructure | Archetype 01 |
| Packaged system implementation on top of infrastructure | Archetype 09 |
| AI/ML platform deployment | Archetype 02 |
| Physical data centre construction | Archetype 03 |

---

## Primary Use Cases

- Cloud landing zone design and deployment (AWS, Azure, GCP)
- Enterprise network upgrade or SD-WAN rollout
- Identity and Access Management (IAM) platform deployment
- Data centre modernisation or migration
- Security Operations Centre (SOC) infrastructure build

---

## Phase Structure

| # | Phase | Key outputs |
|---|---|---|
| 1 | **Assessment** | Current state inventory, gap analysis, risk register, requirements |
| 2 | **Architecture design** | Reference architecture, security architecture, ADRs |
| 3 | **Procurement** | Vendor selection, contracts, licensing, lead time plan |
| 4 | **Deployment** | Infrastructure as Code (IaC), automated provisioning, configuration |
| 5 | **Security hardening** | Baseline security controls, pen test, vulnerability scan |
| 6 | **Testing** | Functional test, load test, DR test, failover validation |
| 7 | **Operational handover** | Runbooks, monitoring, alerting, on-call rotation, CAB active |

---

## Quality Controls

- Architecture Review Board (ARB) sign-off before deployment
- Infrastructure as Code (IaC) used for all provisioned resources
- Security posture baseline documented and validated (CIS Benchmarks or equivalent)
- Penetration test completed before go-live for internet-facing infrastructure
- DR test performed with RTO and RPO validated against targets
- Change Advisory Board (CAB) active from deployment phase
- All credentials and secrets managed via a secrets management system (no hardcoding)

---

## Validation Gates

| Gate | Criteria | Who approves |
|---|---|---|
| **G1 — Architecture** | Design approved by ARB, security architecture signed off | Architect + CISO |
| **G2 — Deployment** | IaC validated, no critical config errors, environments consistent | DevOps Lead + QA |
| **G3 — Security** | Pen test passed, vulnerability scan clean, secrets audit done | CISO + Security Lead |
| **G4 — DR test** | RTO and RPO targets met in live DR test | Operations Lead + CTO |
| **G5 — Handover** | Runbooks published, monitoring live, on-call active, CAB active | Operations Lead |

---

## Resilience & Recovery

- Disaster Recovery Plan (DRP) with RTO ≤ 4h / RPO ≤ 1h for critical systems (adapt per context)
- Business Continuity Plan (BCP) linked to DRP
- Redundancy on all single points of failure (N+1 minimum)
- Automated backup with restore validation
- Incident response playbooks for outage, breach, and ransomware
- Vendor SLA with financial penalty for critical breaches

---

## International Validity

| Standard | Scope |
|---|---|
| ITIL 4 | IT service management |
| ISO/IEC 20000-1:2018 | IT service management system |
| ISO/IEC 27001:2022 | Information security management |
| TOGAF 10 | Enterprise architecture |
| CIS Controls v8 | Security baseline |
| NIST CSF 2.0 | Cybersecurity framework (US, internationally adopted) |
| SOC 2 Type II | Trust services (cloud) |
| PCI DSS v4 | Payment card data security |

---

## Lock Condition

**Locks when:** Infrastructure live, monitoring active, runbooks published, DR test passed, and operational ownership formally transferred to IT Ops.

**Reopens when:** Major capacity event, security incident, cloud provider change, compliance audit finding, or end-of-life of a key component.

---

*[← Back to Archetype Index](README.md) | [Flawless Method](../README.md)*
