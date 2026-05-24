# ADR-0001 — Estructura Canónica del Repositorio

| Campo | Valor |
|---|---|
| **Estado** | aceptado |
| **Fecha** | 2026-05-01 |
| **Autor** | Flawless Studio |

## Contexto

El repositorio `flawlessstudio/flawlessstudio` actua como hub organizacional del ecosistema Flawless Studio. Necesitaba una estructura que pudiera:

- Albergar estándares canónicos inmutables aplicables a todos los repositorios
- Organizar la documentación operativa sin ambigüedad
- Escalar a medida que se añadan nuevos registros y verticales
- Mantener la paridad bilingüe (EN + ES) como restricción de primer nivel

## Opciones consideradas

**Opción A — Estructura plana**  
Todos los documentos en la raíz. Simple, pero no escala. Sin separación entre canon, docs y artefactos del ecosistema.

**Opción B — Estructura solo con docs/**  
Todo bajo `docs/`. Estándar en muchos repositorios, pero mezcla estándares canónicos con documentación operativa.

**Opción C — Estructura por capas con nivel canon explícito (elegida)**  
`canon/` separado como nivel de máxima autoridad. `docs/` para contenido operativo. `ecosystem/` para artefactos inter-repositorio. `registries/` para datos de dominio. `assets/` para marca.

## Decisión

Opción C. El directorio `canon/` alberga estándares inmutables regulados por `GOVERNANCE.md`. El resto de directorios tienen roles operativos, de navegación o de dominio. La paridad bilingüe (`.md` + `.es.md`) se aplica en todos los niveles.

## Justificación

- Los documentos del canon necesitan un nivel de autoridad diferenciado, visualmente y estructuralmente separado de los docs operativos.
- La paridad bilingüe como restricción estructural previene la deriva lingüística con el tiempo.
- El modelo por capas hace que el propósito de cada directorio sea inequívoco sin necesidad de leer su contenido.

## Consecuencias

- Todo nuevo documento de canon requiere su par bilingüe antes de hacer merge.
- Se debe consultar `GOVERNANCE.md` antes de modificar cualquier archivo en `canon/`.
- Los nuevos directorios en la raíz requieren un ADR.

---

*Ver también: [`GOVERNANCE.es.md`](../../GOVERNANCE.es.md) · [`CANON.es.md`](../../CANON.es.md)*
