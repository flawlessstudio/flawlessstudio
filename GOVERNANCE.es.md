# GOBERNANZA

> Reglas, roles y procesos que gobiernan este repositorio y el ecosistema Flawless.

## Roles

| Rol | Responsabilidad |
|---|---|
| **Fundador** | Autoridad final sobre todos los documentos canónicos |
| **Colaborador** | Propone cambios vía PR; sin push directo a `main` |
| **Agente** | Sistemas automatizados que operan bajo contratos estrictos definidos en `docs/reference/agent-contracts.md` |

## Proceso de Cambio

1. Abre un issue describiendo el cambio propuesto.
2. Enlaza al documento canónico afectado.
3. Envía un PR con el cambio y una justificación en `docs/decisions/`.
4. El fundador revisa y fusiona o rechaza.

## Estrategia de Ramas

- `main` — listo para producción, protegido
- `draft/*` — trabajo en progreso, sin revisar
- `fix/*` — correcciones puntuales

## Política de Idioma

- Todos los documentos canónicos existen en EN (`.md`) y ES (`.es.md`).
- EN es la versión autoritativa. ES es el equivalente localizado.
- Las traducciones deben actualizarse de forma atómica con su fuente EN.

---

_Última revisión: Mayo 2026_
