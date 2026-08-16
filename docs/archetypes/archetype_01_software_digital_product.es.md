# Arquetipo 01 — Software / Producto Digital

> **Flawless Method** | `docs/archetypes/` | v1.0.0 | 2026-05-24

---

## Identity

| Campo | Valor |
|---|---|
| **Tipo de entregable** | Producto de software o servicio digital (aplicación web, app móvil, API, plataforma SaaS, software embebido) |
| **Clase de novedad** | Mark n — tipo de producto conocido, requisitos y arquitectura variables |
| **Estándar principal** | ISO/IEC 25010:2023 (calidad de producto), PMBOK 7, SAFe 6.0 |
| **Sector** | Tecnología, SaaS, IT empresarial, Fintech, Healthtech, E-commerce |

---

## Alcance

Todas las actividades desde el descubrimiento del producto hasta el diseño, desarrollo, pruebas, lanzamiento e iteración post-lanzamiento de un producto de software o servicio digital. Cubre modelos de entrega web, móvil, API, embebido e híbrido.

---

## Exclusiones

| Fuera de alcance | Redirigir a |
|---|---|
| Desarrollo de modelos de IA/ML como entregable principal | Arquetipo 02 |
| Despliegue de infraestructura IT sin entrega de producto | Arquetipo 10 |
| Herramientas internas sin usuarios externos | Arquetipo 09 |
| Hardware con firmware embebido como entregable principal | Arquetipo 05 |

---

## Casos de Uso Principales

- Lanzamiento de una plataforma SaaS desde cero hasta v1
- Construcción de una aplicación móvil (iOS, Android, multiplataforma)
- Desarrollo de una API REST/GraphQL pública o para socios
- Entrega de una versión mayor de un producto existente
- Migración de un sistema legacy a una arquitectura moderna

---

## Estructura de Fases

| # | Fase | Entregables clave |
|---|---|---|
| 1 | **Descubrimiento** | Declaración del problema, investigación de usuarios, dimensionamiento de oportunidad, visión del producto |
| 2 | **Definición** | PRD, historias de usuario, criterios de aceptación, viabilidad técnica |
| 3 | **Arquitectura** | Diseño del sistema, ADRs, decisión de stack tecnológico, requisitos no funcionales |
| 4 | **Desarrollo** | Construcción iterativa (sprints/ciclos), revisión de código, pruebas unitarias e integración |
| 5 | **Aseguramiento de calidad** | Pruebas E2E, rendimiento, análisis de seguridad, auditoría de accesibilidad |
| 6 | **Lanzamiento** | Despliegue en staging, UAT, notas de versión, estrategia de rollout |
| 7 | **Post-lanzamiento** | Monitoreo, respuesta a incidentes, ciclo de retroalimentación de usuarios, backlog de iteración |

---

## Controles de Calidad

- Definición de Terminado acordada y aplicada para cada historia de usuario
- Revisión de código requerida antes de merge (mínimo 1 revisor par)
- Cobertura de pruebas automatizadas ≥ 80% para rutas críticas
- Análisis de seguridad (SAST/DAST) ejecutado en cada candidato de lanzamiento
- Auditoría de accesibilidad (WCAG 2.1 AA) antes del lanzamiento público
- Línea base de rendimiento definida y probada ante regresiones
- Auditoría de dependencias (SBOM) generada por versión

---

## Puertas de Validación

| Puerta | Criterios | Quién aprueba |
|---|---|---|
| **G1 — Descubrimiento** | Problema validado, alcance acotado, alineación de stakeholders | Product Owner + Sponsor |
| **G2 — Arquitectura** | ADRs firmados, NFRs aceptados, sin bloqueadores sin resolver | Tech Lead + Arquitecto |
| **G3 — Feature complete** | Todas las historias P0/P1 completadas, cobertura de pruebas cumplida | QA Lead + Product Owner |
| **G4 — Lanzamiento** | Staging aprobado, seguridad verificada, plan de rollback listo | Release Manager + CISO |
| **G5 — Post-lanzamiento** | Tasa de errores < umbral, SLOs cumplidos por 7 días | Engineering Lead |

---

## Resiliencia y Recuperación

- Feature flags para rollout incremental seguro y rollback instantáneo
- Estrategia de despliegue canary / blue-green definida antes del lanzamiento
- Runbook de incidentes publicado y probado antes del go-live
- SLOs y SLAs definidos con umbrales de alerta
- Plan de recuperación ante desastres con objetivos RTO y RPO
- Rotación de guardia activa desde el día del lanzamiento

---

## Validez Internacional

| Estándar | Alcance |
|---|---|
| ISO/IEC 25010:2023 | Modelo de calidad de producto software |
| ISO/IEC 27001:2022 | Gestión de seguridad de la información |
| GDPR / CCPA | Privacidad de datos (UE y EE.UU.) |
| WCAG 2.1 AA | Accesibilidad web |
| OWASP Top 10 | Línea base de vulnerabilidades de seguridad |
| SOC 2 Type II | Servicios de confianza (productos cloud en EE.UU.) |
| PMBOK 7.ª Ed. | Gestión de proyectos |
| SAFe 6.0 | Ágil a escala |

---

## Condición de Cierre

**Se cierra cuando:** El producto está en producción, SLOs cumplidos durante 7 días consecutivos, backlog post-lanzamiento priorizado y traspaso a operaciones en estado estable completo.

**Se reabre cuando:** Se planifica una versión mayor, se requiere cambio de arquitectura, un incidente de seguridad obliga a rediseño, o una obligación de cumplimiento normativo fuerza una reconstrucción.

---

*[← Volver al Índice de Arquetipos](README.md) | [Flawless Method](../README.md)*
