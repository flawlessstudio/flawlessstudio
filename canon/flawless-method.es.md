# Método Flawless

> El método de toma de decisiones de Flawless Studio. Cómo se aborda cada problema, se diseña cada sistema y se valida cada cambio.

## El Método

```
Entender → Acotar → Planificar → Ejecutar → Verificar → Documentar
```

### 1. Entender
- Enunciar el objetivo en una frase.
- Identificar restricciones, contexto y referencias canónicas.

### 2. Acotar
- Definir el alcance mínimo suficiente.
- Listar explícitamente lo que queda fuera del alcance.

### 3. Planificar
- Producir un plan de ejecución mínimo.
- Identificar riesgos antes de actuar.

### 4. Ejecutar
- Acciones controladas y atómicas.
- Un subobjetivo a la vez.

### 5. Verificar
- Auditar el resultado contra el objetivo.
- Aplicar el Filtro Flawless.

### 6. Documentar
- Registrar la decisión en `docs/decisions/`.
- Actualizar el documento canónico relevante si se ve afectado.

## Anti-patrones

| Anti-patrón | Consecuencia |
|---|---|
| Saltar el alcance | Desvío del alcance, esfuerzo desperdiciado |
| Actuar sin planificar | Fallos silenciosos, rollbacks costosos |
| Decisiones no documentadas | Pérdida de conocimiento, errores repetidos |
| Fuentes de verdad duplicadas | Contradicciones, confusión |

---

_Versión: 1.0 · Última revisión: Mayo 2026_
