# Mapa del Ecosistema

> Mapa estructural y relacional de todos los sistemas de Flawless Studio.

## Visión General de la Arquitectura

```
┌─────────────────────────────────────────────────┐
│                 FLAWLESS STUDIO                 │
│        Fundador en solitario · AI-nativo        │
└──────────────────────┬──────────────────────────┘
                       │
       ┌───────────────┼───────────────┐
       ▼               ▼               ▼
  ┌─────────┐    ┌──────────┐    ┌──────────┐
  │  Canon  │    │Registros │    │Ecosistema│
  │ (verdad)│    │ (estado) │    │  (mapa)  │
  └─────────┘    └──────────┘    └──────────┘
       │
  ┌────┴─────────────────────────┐
  ▼                              ▼
┌─────────────┐         ┌─────────────────┐
│  INUI OS    │         │ Flawless Engine │
│  FDIS OS    │         │ Flawless Agents │
│  NorthStar  │         │ Repo Analyst    │
└─────────────┘         └─────────────────┘
```

## Relaciones entre Sistemas

| Sistema | Depende de | Alimenta a |
|---|---|---|
| Canon | — | Todos los sistemas |
| INUI OS | Canon, FDIS OS | AionUI |
| FDIS OS | Canon | INUI OS, Flawless Engine |
| Flawless Engine | Canon, Registros | Agentes, Productos |
| Flawless Agents | Canon, Engine | Productos, QMS |
| QMS | Canon | Todos los sistemas |

---

_Última revisión: Mayo 2026_
