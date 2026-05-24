# Registro de Migraciones

> Registro cronológico de todas las migraciones estructurales, refactorizaciones y cambios disruptivos.

## 2026-05-24 — Árbol canónico bilingüe

- **Antes:** Estructura plana `docs/en/` + `docs/es/` con 11 archivos mixtos.
- **Después:** Árbol bilingüe canónico con `canon/`, `registries/`, `ecosystem/`, `docs/` (Diátaxis), `.github/`.
- **Patrón:** `filename.md` (EN, autoritativo) + `filename.es.md` (ES, localizado).
- **Archivos migrados:** `docs/en/*` → `docs/reference/` · `docs/es/*` → `docs/runbooks/`
- **Justificación:** Eliminar redundancia estructural, fuente única de verdad por concepto, cumplimiento del Método Flawless.

---

_Log activo. Añadir nuevas entradas al principio._
