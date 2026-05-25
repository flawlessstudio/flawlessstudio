# Arquetipo 10 — Infraestructura TI

> **Par canónico EN:** `archetype_10_it_infrastructure.md`

---

## Identity

**Nombre:** Arquetipo 10 — Infraestructura TI
**Versión:** 1.0.0
**Estado:** Activo
**Ámbito:** Proyectos de plataforma de infraestructura TI

---

## Scope

Define proyectos de infraestructura: cloud, redes, identidad, compute, almacenamiento y seguridad. Cubre desde evaluación hasta diseño, procurement, despliegue, endurecimiento de seguridad y handover operacional.

---

## Exclusions

Desarrollo de productos de software usando la infraestructura. Implementación de sistemas empaquetados. Despliegue de plataformas de IA/ML.

---

## Phase Structure

| Fase | Nombre | Objetivo |
|------|--------|----------|
| 1 | Assessment | Inventario del estado actual y análisis de brechas |
| 2 | Architecture | Diseño de arquitectura y seguridad |
| 3 | Procurement | Selección de vendor y gestión de contratos |
| 4 | Deployment | Infrastructure as Code (IaC) y provisioning |
| 5 | Security Hardening | Controles de seguridad base y pruebas de penetración |
| 6 | Testing | Pruebas funcionales, carga y DR |
| 7 | Operational Handover | Runbooks, monitoreo, alertas y rotación on-call |

---

## Quality Controls

- Sign-off de Architecture Review Board (ARB) antes de despliegue
- Infrastructure as Code (IaC) usado para todos los recursos
- Postura de seguridad baseline documentada (CIS Benchmarks)
- Prueba de penetración completada antes de go-live
- Prueba de DR con RTO y RPO validados
- CAB activo desde fase de despliegue
- Gestión de secretos en vault (sin hardcoding)

---

## Validation Gates

| Puerta | Criterio de paso |
|--------|------------------|
| G1 | Diseño aprobado por ARB, arquitectura de seguridad firmada |
| G2 | IaC validado, ambientes consistentes |
| G3 | Prueba de penetración pasada, auditoría de secretos |
| G4 | RTO y RPO cumplidos en prueba de DR en vivo |
| G5 | Runbooks publicados, monitoreo en vivo, CAB activo |

---

## Resilience

Plan de DR (Disaster Recovery) con RTO ≤ 4h / RPO ≤ 1h. Plan de BC (Business Continuity) enlazado. N+1 redundancia mínimo. Backup automatizado con validación. Playbooks de incident response.

---

## International Validity

Este arquetipo sigue ITIL 4, ISO/IEC 20000-1:2018, ISO/IEC 27001:2022, TOGAF 10, NIST CSF 2.0.

---

## Lock Condition

El arquetipo queda bloqueado cuando la infraestructura está en vivo, monitoreo activo, runbooks publicados, prueba de DR pasada, y propiedad operacional transferida.
