# Recipes — voice-ai

> Composition recipes for the `voice-ai` registry.

Recipes define curated combinations of `voice-ai` registry entries for specific use cases. Each recipe is a named, versioned configuration that can be referenced directly in project setups.

## Naming convention

```
<use-case-slug>.recipe.yaml
```

Example: `conversational-assistant.recipe.yaml`

## Recipe structure

Each recipe file includes:
- `name` — human-readable label
- `version` — semver
- `use_case` — what problem this recipe solves
- `entries` — list of registry entry references
- `rationale` — why this combination was chosen

---

*See [`registries/README.md`](../../README.md) for the full registry governance model.*
