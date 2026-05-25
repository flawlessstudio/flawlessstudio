# Arquetipo 05 — Hardware / Producto Físico

> **Par canónico EN:** `archetype_05_hardware_physical_product.md`

---

## Identity

**Nombre:** Arquetipo 05 — Hardware / Producto Físico
**Versión:** 1.0.0
**Estado:** Activo
**Ámbito:** Proyectos de desarrollo de productos físicos

---

## Scope

Define proyectos de desarrollo de hardware: dispositivos IoT, dispositivos médicos, electrónica de consumo y equipos industriales. Cubre desde concepto hasta diseño industrial, ingeniería, prototipado, certificación y lanzamiento.

---

## Exclusions

Sistemas complejos de múltiples subsistemas. Optimización de manufactura masiva. Productos de software puro.

---

## Phase Structure

| Fase | Nombre | Objetivo |
|------|--------|----------|
| 1 | Concept | Brief del producto y requisitos clave |
| 2 | Design Industrial | Forma, UX y materiales |
| 3 | Engineering | Esquema eléctrico, PCB y diseño mecánico |
| 4 | Prototyping | EVT (Engineering Validation Test) builds |
| 5 | DVT | Design Validation Test builds y testing |
| 6 | PVT | Production Validation Test builds |
| 7 | Certification | Pruebas regulatorias (CE, FCC, FDA, etc.) |
| 8 | Mass Production | Ramp de manufactura y lanzamiento |

---

## Quality Controls

- Design FMEA (DFMEA) completado antes de DVT
- DFM (Design for Manufacturability) review antes de PVT
- Plan de pruebas de confiabilidad: HALT, HASS
- BOM (Bill of Materials) revisado en cada etapa
- Matriz de cumplimiento regulatorio mantenida
- Revisión de seguridad de firmware

---

## Validation Gates

| Puerta | Criterio de paso |
|--------|------------------|
| G1 | Concepto congelado, requisitos firmados |
| G2 | EVT pasado, funciones críticas verificadas |
| G3 | DVT pasado, DFM aprobado |
| G4 | PVT pasado, yield ≥ objetivo |
| G5 | Certificaciones emitidas, stock disponible |

---

## Resilience

Dual-sourcing de componentes críticos. Proceso de Engineering Change Order (ECO). Procedimiento de recall documentado. Monitoreo de cambios regulatorios.

---

## International Validity

Este arquetipo sigue IEC 62443, ISO 13485:2016, CE Marking, FCC Part 15, RoHS/WEEE.

---

## Lock Condition

El arquetipo queda bloqueado cuando la manufactura masiva es validada, todas las certificaciones emitidas, producto lanzado.
