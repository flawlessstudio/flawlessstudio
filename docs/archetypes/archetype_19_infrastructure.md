# Archetype 19 — Infrastructure

> **Flawless Method** | `docs/archetypes/` | v1.0.0 | 2026-05-25

---

## Identity

| Field | Value |
|---|---|
| **Output type** | Deployed, monitored, and operationalised infrastructure — cloud, on-premise, or hybrid |
| **Novelty class** | Mark n — target state known; topology, tooling, and migration path variable |
| **Primary standard** | AWS/GCP/Azure Well-Architected Framework, IaC (Terraform, Pulumi), SRE practices |
| **Sector** | Any — Tech, Finance, Healthcare, Government, Media, Retail |

---

## Scope

All activities from infrastructure assessment and design through provisioning, configuration, migration, hardening, and handover to operations. Covers cloud infrastructure, networking, compute, storage, CI/CD platforms, Kubernetes, and observability stacks.

---

## Exclusions

| Out of scope | Redirect to |
|---|---|
| Application software development | Archetype 01 |
| Security programme (not infra-scoped) | Archetype 18 |
| Data platform build | Archetype 16 |
| Physical construction of data centre | Archetype 03 |

---

## Primary Use Cases

- Cloud migration (lift-and-shift, re-platform, or re-architect)
- Kubernetes platform build and rollout
- IaC adoption and infrastructure modernisation
- CI/CD pipeline design and implementation
- Observability stack build (metrics, logs, traces)

---

## Phase Structure

| # | Phase | Key outputs |
|---|---|---|
| 1 | **Assessment** | Current state inventory, dependency map, target state architecture, migration risk register |
| 2 | **Design** | Reference architecture, IaC module design, network topology, cost model |
| 3 | **Build** | Infrastructure provisioned via IaC, environments created, CI/CD configured |
| 4 | **Migration** | Workloads migrated, data transferred, cutover executed, rollback tested |
| 5 | **Hardening** | Security baseline applied, patching policy active, access controls enforced |
| 6 | **Operationalisation** | Monitoring and alerting live, runbooks written, on-call rotation defined, SLOs set |

---

## Quality Controls

- All infrastructure defined as code (IaC) from day 1 — no manual provisioning
- IaC peer-reviewed and tested in non-production before production apply
- Cost model reviewed and budget alerts configured before build
- Rollback procedure documented and tested before any migration cutover
- SLOs defined for all production services before go-live
- Disaster recovery test completed before production handover
- Secrets management via vault — no hardcoded credentials anywhere

---

## Validation Gates

| Gate | Criteria | Who approves |
|---|---|---|
| **G1 — Assessment** | Current state documented, target architecture agreed | Infra Lead + CTO |
| **G2 — Design** | Reference architecture approved, cost model signed off | Infra Lead + Finance + CTO |
| **G3 — Build** | All environments provisioned via IaC, CI/CD running | Infra Lead + Engineering Lead |
| **G4 — Migration** | Cutover complete, rollback tested, no critical incidents | Infra Lead + Operations |
| **G5 — Operationalisation** | Monitoring live, SLOs met, runbooks published, DR tested | Infra Lead + Sponsor |

---

## Resilience & Recovery

- Multi-region or multi-AZ deployment for services with RTO < 1 hour
- Automated backup and tested restore for all stateful systems
- Chaos engineering practice defined for critical services
- Incident runbooks for top 10 failure scenarios
- Cost anomaly detection active from day 1 of production

---

## International Validity

| Standard | Scope |
|---|---|
| AWS / GCP / Azure Well-Architected | Cloud infrastructure best practices |
| Terraform / Pulumi | IaC tooling standards |
| CNCF / Kubernetes | Container orchestration standards |
| SRE (Google SRE Book) | Site reliability engineering practices |
| ISO 22301 | Business continuity management |
| NIST SP 800-53 | Security controls for federal systems |

---

## Lock Condition

**Locks when:** Infrastructure in production, monitoring and SLOs active, DR tested, and operational ownership transferred to SRE/platform team.

**Reopens when:** Major architecture change, cloud provider migration, capacity planning trigger, cost optimisation initiative, or security re-assessment.

---

*[← Back to Archetype Index](README.md) | [Flawless Method](../README.md)*
