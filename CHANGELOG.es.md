# Registro de cambios

Todos los cambios notables en este repositorio están documentados aquí.
El formato sigue [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [0.3.0] — 2026-05-24

### Añadido
- `canon/flawless-terminology.md` + `.es.md` — glosario canónico de todos los términos Flawless (restaurado; figuraba en v0.1.0 pero ausente del repositorio)
- `MIGRATION_LOG.md` + `.es.md` — registro estructurado de migraciones estructurales

### Corregido
- `canon/flawless-framework.md`: referencia rota a `agent-contracts.md` reemplazada por nota pendiente en `docs/reference/`
- `.github/workflows/validate-bilingual-parity.yml`: función muerta `check_parity()` eliminada; propagación de salida de subshell corregida con patrón `mapfile`
- `.github/workflows/audit-report.yml`: paso `ensure-label` añadido para proteger contra la ausencia del label `audit`

---

## [0.2.0] — 2026-05-24

### Añadido
- `canon/flawless-writing.md` + `.es.md` — estándar canónico de escritura Flawless
- `SECURITY.md` + `.es.md` — política de seguridad
- `CHANGELOG.md` + `.es.md` — este archivo
- `SUPPORT.md` + `.es.md` — guía de soporte
- `CODE_OF_CONDUCT.md` + `.es.md` — código de conducta del contribuidor
- `.github/PULL_REQUEST_TEMPLATE.md` + `.es.md` — plantilla de PR estructurada
- `.github/ISSUE_TEMPLATE/bug.yml`, `canon-revision.yml`, `improvement.yml`, `config.yml`
- `docs/decisions/ADR-0001-canonical-structure.md` + `.es.md`
- `docs/decisions/README.md` + `.es.md`
- `docs/explanation/`, `how-to/`, `reference/`, `runbooks/`, `tutorials/` — READMEs EN+ES
- `assets/README.md` + `.es.md`
- `registries/voice-ai/audits/README.md` + `.es.md`
- `registries/voice-ai/recipes/README.md` + `.es.md`

### Corregido
- `GOVERNANCE.md`: referencia rota a `agent-contracts.md` eliminada; consecuencia de push-to-main documentada
- `CANON.md`: columna Status añadida; instrucción de acción post-lectura añadida
- `SECURITY.md`: alcance ampliado al ecosistema completo; sección fuera de alcance ampliada
- `SUPPORT.md`: línea de criterio de éxito añadida
- `CODE_OF_CONDUCT.md`: regla de proceso eliminada (movida a `CONTRIBUTING.md`)
- `REPO_INDEX.md` + `.es.md`: clarificado como referencia rápida; enlace a `ecosystem/repo-index` añadido
- `ecosystem/map.md`: enlace ADR roto corregido; entrada duplicada `RAG-Anything` eliminada
- `ecosystem/repo-index.md` + `.es.md`: columna Visibility añadida; nota de alcance añadida
- `docs/decisions/README.md` + `.es.md`: tabla de índice ADR añadida

---

## [0.1.0] — 2026-05-01

### Añadido
- Estructura inicial del repositorio
- `canon/` con `flawless-framework`, `flawless-method`, `flawless-terminology` (EN + ES)
- `CANON.md`, `GOVERNANCE.md`, `REPO_INDEX.md` (EN + ES)
- `ecosystem/map.md`, `ecosystem/repo-index.md` (EN + ES)
- `registries/voice-ai/` con `registry.core.yaml` y `registry.watchlist.yaml`
- `assets/profile/` con avatar y banner (PNG + SVG)
- `.github/` con `CODEOWNERS`, `CONTRIBUTING.md`, `ISSUE_TEMPLATE/`, `workflows/`

---

[0.3.0]: https://github.com/flawlessstudio/flawlessstudio/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/flawlessstudio/flawlessstudio/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/flawlessstudio/flawlessstudio/releases/tag/v0.1.0
