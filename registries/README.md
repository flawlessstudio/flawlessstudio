# Registries

> Versioned catalogs of active tools, stacks, and technologies used across the Flawless ecosystem.

## Structure

Each registry lives in its own subdirectory and follows this pattern:

```
registries/
└── {domain}/
    ├── README.md              ← purpose and scope
    ├── registry.core.yaml     ← active tools and configurations
    ├── registry.watchlist.yaml ← tools under evaluation
    ├── audits/                ← audit history
    └── recipes/               ← reusable configurations and patterns
```

## Active Registries

| Registry | Domain |
|---|---|
| [`voice-ai/`](./voice-ai/) | Voice AI tools and models |

---

_To add a new registry, copy the `voice-ai/` structure and adapt._
