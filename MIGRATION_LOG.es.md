# REGISTRO DE MIGRACIONES

> Registro cronológico de todas las migraciones estructurales, refactorizaciones y cambios disruptivos en este repositorio.

## 2026-05-24 — Árbol bilingüe scaffoldeado

- **Acción:** Reestructurado el repo de `docs/en` + `docs/es` planos al árbol bilingüe canónico.
- **Patrón adoptado:** `filename.md` (EN, autoritativo) + `filename.es.md` (ES, localizado).
- **Archivos movidos:** `docs/en/*` → `docs/runbooks/` · `docs/es/*` → `docs/runbooks/*.es.md`
- **Nuevas capas añadidas:** `canon/`, `registries/`, `ecosystem/`, `docs/` (Diátaxis), `.github/`
- **Justificación:** Eliminar redundancia estructural, garantizar fuente única de verdad por concepto.

---

_Log activo. Añadir entradas cronológicamente. Las más antiguas al final._
