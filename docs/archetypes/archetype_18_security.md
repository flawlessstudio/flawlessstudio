# Archetype 18 — Security

> **Flawless Method** | `docs/archetypes/` | v1.0.0 | 2026-05-25

---

## Identity

| Field | Value |
|---|---|
| **Output type** | Implemented security programme, hardened system, or security certification |
| **Novelty class** | Mark n — threat landscape known; attack surface, controls, and evidence variable |
| **Primary standard** | ISO 27001:2022, NIST CSF 2.0, OWASP, CIS Controls v8, SOC 2 |
| **Sector** | Any — Tech, Finance, Healthcare, Government, Critical Infrastructure |

---

## Scope

All activities from threat modelling and risk assessment through security architecture design, control implementation, penetration testing, certification, and ongoing security operations. Covers application security, infrastructure security, identity and access management, and security monitoring.

---

## Exclusions

| Out of scope | Redirect to |
|---|---|
| Regulatory compliance programme (non-security) | Archetype 11 |
| Infrastructure build without security focus | Archetype 19 |
| Data governance and privacy only | Archetype 16 |
| Physical security only | Facilities / specialist security team |

---

## Primary Use Cases

- ISO 27001 or SOC 2 Type II certification
- Application security programme (SAST, DAST, pentesting)
- Zero trust architecture implementation
- Cloud security posture management (CSPM)
- Incident response programme design and exercise

---

## Phase Structure

| # | Phase | Key outputs |
|---|---|---|
| 1 | **Risk assessment** | Asset inventory, threat model, risk register, attack surface map |
| 2 | **Security architecture** | Security design, controls selection, IAM design, network segmentation plan |
| 3 | **Implementation** | Controls deployed, hardening applied, security tooling configured |
| 4 | **Testing** | Vulnerability assessment, penetration test, red team exercise |
| 5 | **Certification** | External audit (ISO 27001 / SOC 2), findings remediated, certificate issued |
| 6 | **Operations** | SIEM active, incident response plan tested, vulnerability management cycle running |

---

## Quality Controls

- Threat model completed before architecture design
- All critical and high vulnerabilities from pentest remediated before certification
- MFA enforced for all privileged accounts before go-live
- Security baseline (CIS Benchmark or equivalent) applied to all systems
- Incident response plan tested with tabletop exercise before certification
- Vulnerability management cycle: scan → triage → remediate → verify, SLA defined
- Supply chain security: all third-party dependencies reviewed before production

---

## Validation Gates

| Gate | Criteria | Who approves |
|---|---|---|
| **G1 — Risk assessment** | Threat model complete, risk register signed off | CISO + Security Lead |
| **G2 — Architecture** | Security design approved, controls mapped to risks | CISO + Architecture Lead |
| **G3 — Implementation** | Controls operational, hardening verified, tooling live | Security Lead + Internal Audit |
| **G4 — Testing** | Pentest complete, critical/high findings remediated | CISO + Security Lead |
| **G5 — Certification** | External audit passed, certificate issued | CISO + Board/Exec |

---

## Resilience & Recovery

- Incident response playbooks for top 5 threat scenarios documented and tested
- Business continuity plan covering security incident scenarios
- Backup and recovery tested for all critical systems
- Breach notification procedure aligned to GDPR 72-hour requirement
- Threat intelligence feed active and integrated into SIEM

---

## International Validity

| Standard | Scope |
|---|---|
| ISO 27001:2022 | Information security management systems |
| NIST CSF 2.0 | Cybersecurity framework |
| CIS Controls v8 | Prioritised security controls |
| OWASP Top 10 / ASVS 5.0 | Application security |
| SOC 2 Type II | Service organisation controls (US) |
| NIS2 Directive | Critical infrastructure security (EU) |
| DORA | Financial sector digital resilience (EU) |

---

## Lock Condition

**Locks when:** Certification achieved, security operations running, no critical findings open, and vulnerability management cycle active.

**Reopens when:** Certification renewal, material change to attack surface, new threat, regulatory change, or security incident triggers re-assessment.

---

*[← Back to Archetype Index](README.md) | [Flawless Method](../README.md)*
