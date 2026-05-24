# ADR-001 — Árbol Canónico Bilingüe

**Fecha:** 2026-05-24  
**Estado:** Aceptado  
**Autor:** Fundador de Flawless Studio  

---

## Contexto

El repositorio tenía una estructura plana y ad-hoc con `docs/en/` y `docs/es/` como silos paralelos. Esto generaba:

- Redundancia estructural (el mismo concepto en dos lugares)
- Sin fuente única de verdad por documento
- Sin marco para distinguir conocimiento operativo, de referencia o canónico
- Dificultad para incorporar agentes IA (sin puntos de entrada claros)

## Decisión

Adoptar un **árbol canónico bilingüe** como estándar estructural único para todos los repositorios de Flawless Studio.

### Patrón

- `filename.md` — Inglés, fuente autoritativa
- `filename.es.md` — Español, traducción localizada
- Un archivo por concepto, una ubicación por tipo de archivo

### Estructura del árbol

```
/
├── canon/           # Principios operativos inmutables (EN+ES)
├── registries/      # Registros de datos estructurados (YAML + MD)
├── ecosystem/       # Mapa e índice de repos (EN+ES)
├── docs/            # Base de conocimiento Diataxis
│   ├── tutorials/
│   ├── how-to/
│   ├── explanation/
│   ├── reference/   # Specs de agentes, contratos, manifiestos
│   ├── decisions/   # ADRs y registros de migración
│   ├── runbooks/    # Guías operativas
│   └── audits/      # Snapshots de calidad
└── .github/         # Configuración de contribuciones y automatización
```

## Consecuencias

### Positivas
- Fuente única de verdad por concepto
- Punto de entrada claro para agentes IA (`docs/reference/AI_AGENT_QUICKSTART.md`)
- Diataxis proporciona un marco para el crecimiento futuro de la documentación
- `CODEOWNERS` y `CONTRIBUTING.md` refuerzan la gobernanza

### Negativas
- 11 archivos legacy requirieron migración y eliminación manual
- Runbooks EN pendientes (4 archivos existen solo en ES)

---

_Próximo ADR: cuando se tome una segunda decisión estructural._
