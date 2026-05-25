# Arquetipo 04 — Ingeniería / Sistemas

> **Par canónico EN:** `archetype_04_engineering_systems.md`

---

## Identity

**Nombre:** Arquetipo 04 — Ingeniería / Sistemas
**Versión:** 1.0.0
**Estado:** Activo
**Ámbito:** Proyectos de sistemas complejos integrados

---

## Scope

Define proyectos de ingeniería de sistemas: productos complejos, sistemas de sistemas y soluciones técnicas integradas. Cubre desde concepto hasta requeri­mientos, arquitectura, diseño, integración, verificación y validación.

---

## Exclusions

Productos de software puro. Productos físicos simples. Construcción de instalaciones. Manufactura a escala después de validación.

---

## Phase Structure

| Fase | ISO 15288 | Objetivo |
|------|-----------|----------|
| 1 | Concept | Declaración de misión y necesidades de stakeholders |
| 2 | Requirements | System Requirements Specification (SyRS) |
| 3 | Architecture | Arquitectura del sistema e Interface Control Documents |
| 4 | Design | Diseño detallado y especificaciones |
| 5 | Integration | Integración de subsistemas |
| 6 | Verification | Pruebas y evaluación, matriz de verificación |
| 7 | Validation | Pruebas de nivel de sistema y V&V |
| 8 | Deployment | Despliegue, entrenamiento y plan de mantenimiento |

---

## Quality Controls

- Matriz de trazabilidad de requisitos (RTM) mantenida
- Análisis de Modo de Falla y Efectos (FMEA) completado
- Interface Control Documents (ICDs) baselineados
- Revisiones técnicas independientes en cada fase
- Plan de Verificación y Validación (V&V) acordado
- Safety case mantenido y actualizado
- Sistema de gestión de configuración activo

---

## Validation Gates

| Puerta | Criterio de paso |
|--------|------------------|
| SRR | SyRS completo, requisitos críticos sin TBDs |
| PDR | Arquitectura congelada, FMEA completado |
| CDR | Diseño detallado completo, ICDs baselineados |
| TRR | Plan de pruebas aprobado, instalaciones listas |
| FRR | Todas las pruebas pasadas, caso de seguridad cerrado |

---

## Resilience

Junta de Control de Cambios (CCB) formal. Registro de riesgos con puntuación. Nivel de Madurez Tecnológica (TRL) mínimo TRL 6. Suite de regresión. Márgenes de diseño contingente.

---

## International Validity

Este arquetipo sigue ISO/IEC/IEEE 15288:2023, INCOSE SE Handbook v4, MIL-STD-882E.

---

## Lock Condition

El arquetipo queda bloqueado cuando el sistema está desplegado, V&V aceptado, caso de seguridad cerrado, y primer review operacional pasado.
