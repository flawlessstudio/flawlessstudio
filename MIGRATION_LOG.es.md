# Registro de Migraciones

> Registro estructurado de todas las migraciones estructurales aplicadas a este repositorio. Una migración es cualquier cambio que reorganiza, renombra, mueve o elimina archivos o carpetas de maneras que rompen referencias previas o alteran el árbol canónico.

---

## Formato

Cada entrada sigue esta estructura:

```
### [MIG-XXXX] — YYYY-MM-DD
**Tipo:** Renombrar | Mover | Eliminar | Reestructurar
**Alcance:** Archivos o carpetas afectados
**Motivo:** Por qué fue necesaria esta migración
**Cambios disruptivos:** Qué se rompe y cuál es el reemplazo
**Estado:** Aplicado | Revertido
```

---

## Registro

### [MIG-0001] — 2026-05-24

**Tipo:** Reestructurar  
**Alcance:** `docs/` — se añadieron subdirectorios `explanation/`, `how-to/`, `reference/`, `runbooks/`, `tutorials/` con READMEs bilingües  
**Motivo:** Alinear la estructura de `docs/` con el framework de documentación Diátaxis. La estructura plana anterior no distinguía entre material orientado al aprendizaje, a la tarea y de referencia.  
**Cambios disruptivos:** Cualquier enlace directo a la raíz de `docs/` que espere una lista plana de archivos es ahora incorrecto. Todo el contenido está organizado bajo subdirectorios tipificados.  
**Estado:** Aplicado

### [MIG-0002] — 2026-05-24

**Tipo:** Eliminar  
**Alcance:** `GOVERNANCE.md` — eliminada referencia a `docs/reference/agent-contracts.md`; `canon/flawless-framework.md` — referencia reemplazada por nota pendiente en `docs/reference/`  
**Motivo:** El archivo no existía. Las referencias rotas violan el Criterio de Salida 5 del estándar Flawless Writing.  
**Cambios disruptivos:** Cualquier agente que dependa de `docs/reference/agent-contracts.md` debe actualizarse para apuntar a `docs/reference/` hasta que el archivo se cree formalmente.  
**Estado:** Aplicado

---

_Última actualización: 2026-05-24_
