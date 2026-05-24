# Registro de cambios

Todos los cambios relevantes en este repositorio se documentan aquí.
Formato basado en [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [0.2.0] — 2026-05-24

### Añadido
- `canon/flawless-writing.md` + `.es.md` — estándar canónico de escritura Flawless
- `SECURITY.md` + `.es.md` — política de seguridad
- `CHANGELOG.md` + `.es.md` — este archivo
- `SUPPORT.md` + `.es.md` — guía de soporte
- `CODE_OF_CONDUCT.md` + `.es.md` — código de conducta
- `.github/PULL_REQUEST_TEMPLATE.md` + `.es.md` — plantilla estructurada de PR
- `.github/ISSUE_TEMPLATE/bug.yml`, `canon-revision.yml`, `improvement.yml`, `config.yml`
- `docs/decisions/ADR-0001-canonical-structure.md` + `.es.md`
- `docs/decisions/README.md` + `.es.md`
- `docs/explanation/`, `how-to/`, `reference/`, `runbooks/`, `tutorials/` — READMEs EN+ES
- `assets/README.md` + `.es.md`
- `registries/voice-ai/audits/README.md` + `.es.md`
- `registries/voice-ai/recipes/README.md` + `.es.md`

### Corregido
- `GOVERNANCE.md`: eliminada referencia rota a `agent-contracts.md`; documentada consecuencia de push directo a `main`
- `CANON.md`: añadida columna Status; añadida instrucción de acción post-lectura
- `SECURITY.md`: alcance ampliado a todo el ecosistema; sección fuera de alcance expandida
- `SUPPORT.md`: añadida línea de criterio de éxito
- `CODE_OF_CONDUCT.md`: eliminada regla de proceso (movida a `CONTRIBUTING.md`)
- `REPO_INDEX.md` + `.es.md`: clarificado como referencia rápida; enlace a `ecosystem/repo-index`
- `ecosystem/map.md`: enlace ADR roto corregido; entrada duplicada `RAG-Anything` eliminada
- `ecosystem/repo-index.md` + `.es.md`: añadida columna Visibility; añadida nota de alcance
- `docs/decisions/README.md` + `.es.md`: añadida tabla de índice de ADRs

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

[0.2.0]: https://github.com/flawlessstudio/flawlessstudio/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/flawlessstudio/flawlessstudio/releases/tag/v0.1.0
