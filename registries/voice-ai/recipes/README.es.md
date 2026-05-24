# Recetas — voice-ai

> Recetas de composición para el registro `voice-ai`.

Las recetas definen combinaciones seleccionadas de entradas del registro `voice-ai` para casos de uso específicos. Cada receta es una configuración con nombre y versión que puede referenciarse directamente en configuraciones de proyectos.

## Convención de nombres

```
<slug-caso-de-uso>.recipe.yaml
```

Ejemplo: `conversational-assistant.recipe.yaml`

## Estructura de una receta

Cada archivo de receta incluye:
- `name` — etiqueta legible
- `version` — semver
- `use_case` — qué problema resuelve esta receta
- `entries` — lista de referencias a entradas del registro
- `rationale` — por qué se eligió esta combinación

---

*Ver [`registries/README.md`](../../README.md) para el modelo completo de gobernanza de registros.*
