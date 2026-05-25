# Arquetipo 02 — Sistema de IA / Datos

> **Par canónico EN:** `archetype_02_ai_data_system.md`

---

## Identity

**Nombre:** Arquetipo 02 — Sistema de IA / Datos
**Versión:** 1.0.0
**Estado:** Activo
**Ámbito:** Proyectos de tipo Sistema de IA y Datos

---

## Scope

Define los proyectos incluidos en este arquetipo: modelos de IA, pipelines de datos, plataformas analíticas y sistemas de inteligencia artificial. Cubre desarrollo, entrenamiento, validación e implementación.

---

## Exclusions

Productos de software donde la IA es una característica menor. Almacenes de datos sin modelos. Investigación en IA sin objetivo de implementación.

---

## Phase Structure

| Fase | Nombre | Objetivo |
|------|--------|----------|
| 0 | Formulación del problema | Definición del caso de uso y métricas de éxito |
| 1 | Descubrimiento de datos | Inventario, calidad y evaluación de viabilidad |
| 2 | Ingeniería de datos | Pipelines, feature store y garantía de calidad |
| 3 | Desarrollo del modelo | Experimentación, entrenamiento y evaluación |
| 4 | Validación | Card del modelo, pruebas de sesgo y adversariales |
| 5 | Despliegue | CI/CD para ML, canary rollout e infraestructura |
| 6 | Monitoreo y gobernanza | Detección de drift, auditoría y supervisión humana |

---

## Quality Controls

- Clasificación de riesgo de IA completada (EU AI Act)
- Scorecard de calidad de datos mantenida
- Evaluación de sesgo y equidad en cada modelo
- Model card publicada para producción
- SBOM y trazabilidad del modelo documentadas
- Pruebas adversariales completadas antes del despliegue

---

## Validation Gates

| Puerta | Criterio de paso |
|--------|------------------|
| G1 | Formulación validada y viabilidad de datos confirmada |
| G2 | Calidad de datos ≥ umbral, PII manejado |
| G3 | Rendimiento del modelo y sesgo dentro de límites |
| G4 | Modo sombra pasado, model card publicada |
| G5 | Monitoreo de drift activo, auditoría verificada |

---

## Resilience

Rollback de modelo en < 15 min. Despliegue en modo sombra para cambios de alto riesgo. Sistema de fallback basado en reglas. Alertas de fallo de pipeline con reintentos automáticos.

---

## International Validity

Este arquetipo sigue ISO/IEC 42001:2023, NIST AI RMF 1.0, EU AI Act 2024 y GDPR.

---

## Lock Condition

El arquetipo queda bloqueado cuando el modelo está en producción, monitoreo activo, baseline de drift establecido, y review de 30 días completado.
