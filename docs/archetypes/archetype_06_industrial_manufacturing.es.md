# Arquetipo 06 — Industrial / Manufactura

> **Par canónico EN:** `archetype_06_industrial_manufacturing.md`

---

## Identity

**Nombre:** Arquetipo 06 — Industrial / Manufactura
**Versión:** 1.0.0
**Estado:** Activo
**Ámbito:** Proyectos de sistemas de manufactura escalada

---

## Scope

Define proyectos de manufacturales: sistemas de producción, líneas de manufactura y procesos industriales escalados. Cubre desde diseño de procesos, herramientas, piloto, ramp-up y operaciones de estado estable.

---

## Exclusions

Desarrollo de productos de hardware antes de manufactura. Construcción de instalaciones de producción. Programas de cumplimiento regulatorio solamente.

---

## Phase Structure

| Fase | Nombre | Objetivo |
|------|--------|----------|
| 1 | Process Design | PFMEA, control plan y diseño de layout |
| 2 | Tooling & Setup | Especificaciones de herramientas y procurement |
| 3 | Pilot Run | FAI (First Article Inspection) y Cpk |
| 4 | Ramp-up | Yield tracking y balance de línea |
| 5 | Steady State | SPC activo y KPIs en vivo |
| 6 | Continuous Improvement | Kaizen events y reducción de costo |

---

## Quality Controls

- Process FMEA (PFMEA) completado antes del inicio
- Cpk ≥ 1.33 para características críticas
- OEE tracked desde piloto
- Gráficos SPC (Statistical Process Control) activos
- PPAP (Production Part Approval Process) completado
- Golden sample archivado por lote
- CAPA process activo

---

## Validation Gates

| Puerta | Criterio de paso |
|--------|------------------|
| G1 | PFMEA aprobado, control plan acordado |
| G2 | FAI pasado, Cpk ≥ 1.33 |
| G3 | PPAP aprobado |
| G4 | Yield ≥ objetivo, OEE ≥ baseline |
| G5 | SPC activo, estado estable confirmado |

---

## Resilience

Dual-sourcing de materias primas críticas. Programa de mantenimiento preventivo. Política de inventario buffer. Proceso de ECO activo desde piloto.

---

## International Validity

Este arquetipo sigue ISO 9001:2015, IATF 16949, APQP, Lean/Six Sigma, ISO 45001.

---

## Lock Condition

El arquetipo queda bloqueado cuando la producción es estable, SPC activo, OEE ≥ objetivo, 30 días de estado estable completados.
