# Ingeniería de Contexto para IA en CLI

> Runbook operativo. Cómo construir y gestionar contexto efectivo para agentes IA en entornos CLI.

---

## Qué es la ingeniería de contexto

La ingeniería de contexto es la disciplina de **diseñar el contexto que recibe un agente IA** para maximizar la calidad de su output. No es prompt engineering (aunque lo incluye). Es arquitectura de información para agentes.

## Principios

1. **Contexto mínimo suficiente** — Más contexto no es mejor. El contexto relevante es mejor.
2. **Jerarquía de relevancia** — Lo más importante va primero. Los LLMs son sensibles a la posición.
3. **Contratos explícitos** — El agente debe saber exactamente qué se espera de él.
4. **Trazabilidad** — El contexto debe ser reproducible y versionado.

## Técnicas en CLI

### Context injection via files
```bash
# Inyectar contexto desde archivos
cat CANON.md | claude "Aplica el marco Flawless a este problema: {problema}"
```

### MCP Servers como fuente de contexto
```bash
# El servidor MCP provee contexto estructurado al agente
mcp-server --config ./mcp.config.json
```

### CLAUDE.md / AGENT.md como contexto persistente
- Colocar instrucciones del agente en archivos específicos.
- El agente los lee automáticamente al iniciar.
- Ver `docs/reference/AGENT.md` para el formato estándar.

### Ventanas de contexto y chunking
```bash
# Dividir documentos grandes en chunks antes de enviar
split -l 100 large-doc.md chunk-
# Procesar cada chunk con contexto acumulativo
```

## Arquitectura de contexto Flawless

```
Canon (verdad inmutable)
    ↓
Contratos de agente (alcance y restricciones)
    ↓
Contexto de tarea (objetivo y parámetros)
    ↓
Ejecución del agente
    ↓
Output trazable
```

---

_Última revisión: Mayo 2026_
