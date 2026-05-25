# Arquetipo 09 — Implementación de Negocios

> **Par canónico EN:** `archetype_09_business_implementation.md`

---

## Identity

**Nombre:** Arquetipo 09 — Implementación de Negocios
**Versión:** 1.0.0
**Estado:** Activo
**Ámbito:** Proyectos de implementación de sistemas de negocio

---

## Scope

Define proyectos de implementación de sistemas: ERP, CRM, HRMS y otros sistemas empaquetados. Cubre desde selección de solución hasta configuración, migración de datos, pruebas, entrenamiento y cutover.

---

## Exclusions

Desarrollo de software a medida. Transformación organizacional sin solución conocida. Despliegue de infraestructura TI.

---

## Phase Structure

| Fase | Nombre | Objetivo |
|------|--------|----------|
| 1 | Selection | Baseline de requisitos y evaluación de vendor |
| 2 | Design | Diseño de solución y modelo de datos |
| 3 | Configuration | Sistema configurado e integraciones construidas |
| 4 | Data Migration | Estrategia de migración y dry run |
| 5 | Testing | SIT, UAT y pruebas de performance |
| 6 | Training | Materiales de entrenamiento y key user training |
| 7 | Cutover | Ejecución del plan de cutover y go-live |
| 8 | Hypercare | Soporte de hypercare y estabilización |

---

## Quality Controls

- Matriz de trazabilidad de requisitos (RTM) desde necesidad a UAT
- Umbral de precisión de migración definido y probado (≥ 99%)
- Sign-off de UAT requerido antes de cutover
- Checklist de cutover completado antes de go-live
- KPIs de hypercare definidos
- Tasa de finalización de entrenamiento ≥ 90% antes de cutover

---

## Validation Gates

| Puerta | Criterio de paso |
|--------|------------------|
| G1 | Diseño aprobado, integraciones alcanceadas |
| G2 | Dry run de migración pasado, precisión ≥ umbral |
| G3 | UAT completado, todos P0/P1 defectos resueltos |
| G4 | Checklist de cutover claro, plan de rollback listo |
| G5 | KPIs de hypercare cumplidos, estabilización confirmada |

---

## Resilience

Plan de rollback probado. Ejecución paralela para sistemas críticos donde sea viable. Ruta de escalada con vendor. Usuarios clave backup identificados. Backup de datos validado.

---

## International Validity

Este arquetipo sigue PRINCE2 7th Ed., PMBOK 7, BABOK v3, MSP 5th Ed., ISO/IEC 20000.

---

## Lock Condition

El arquetipo queda bloqueado cuando el sistema es estable en BAU, hypercare cerrado, vendor SLA activo, y propiedad operacional transferida.
