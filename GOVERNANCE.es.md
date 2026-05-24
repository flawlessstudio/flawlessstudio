# GOVERNANCE

> Reglas, roles y procesos que regulan este repositorio y el ecosistema Flawless.

## Roles

| Rol | Responsabilidad |
|---|---|
| **Founder** | Autoridad final sobre todos los documentos canónicos |
| **Contributor** | Propone cambios mediante PR; sin push directo a `main` |
| **Agent** | Sistemas automatizados bajo contratos estrictos; contratos definidos en `docs/reference/` cuando estén formalizados |

## Proceso de cambio

1. Abrir un issue describiendo el cambio propuesto.
2. Enlazar al documento canónico afectado.
3. Enviar un PR con el cambio y una justificación en `docs/decisions/`.
4. El Founder revisa y hace merge o rechaza.

## Estrategia de ramas

- `main` — producción, protegida. Los pushes directos están bloqueados; todos los cambios entran mediante PR.
- `draft/*` — trabajo en progreso, sin revisar
- `fix/*` — correcciones específicas

## Política de idioma

- Todos los documentos canónicos existen en EN (`.md`) y ES (`.es.md`).
- EN es la versión autoritativa. ES es el equivalente localizado.
- Las traducciones deben actualizarse de forma atómica con su fuente EN.

---

_Última revisión: 2026-05-24_
