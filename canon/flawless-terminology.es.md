# Terminología Flawless

> Glosario canónico de todos los términos utilizados en el ecosistema Flawless. Cada término definido aquí es la única definición autoritativa. Ningún sinónimo, paráfrasis o uso alternativo es válido salvo que se liste explícitamente.

---

## Términos centrales

**Canon**  
El conjunto de documentos inmutables que definen cómo Flawless Studio piensa, construye y opera. El canon es la referencia de mayor prioridad en cualquier conflicto. Los cambios requieren aprobación formal de gobernanza.

**Filtro Flawless**  
La puerta de calidad de cuatro preguntas aplicada a todo artefacto: ¿Es la solución correcta más simple? ¿Es bilingüe y está documentada? ¿Es trazable a una fuente canónica? ¿Está libre de redundancias?

**Framework Flawless**  
El framework operativo central de Flawless Studio. Define los siete principios, las cinco capas del sistema y el nivel de calidad que rigen todo el trabajo.

**Método Flawless**  
El bucle de toma de decisiones de seis pasos: Entender → Delimitar → Planificar → Ejecutar → Verificar → Documentar. Se aplica a cada problema, sistema y cambio.

**Escritura Flawless**  
El estándar de escritura que define el nivel óptimo de ocho dimensiones — Tono, Estructura, Audiencia, Densidad, Perspectiva temporal, Objetivo, Lenguaje y Éxito — calibrado por archivo, audiencia y propósito.

**Coherencia fractal**  
El principio de que cada capa del sistema (archivo, carpeta, repositorio, ecosistema) sigue la misma lógica estructural. Un archivo debe reconocerse como Flawless en cualquier nivel de zoom.

**Registro**  
Un catálogo estructurado y mantenido de herramientas, stacks o señales activos para un dominio específico. Los registros son documentos vivos: se actualizan, auditan y promueven mediante criterios definidos.

**Lista de seguimiento**  
El nivel previo al registro. Herramientas o señales que cumplen los criterios de interés pero aún no los de promoción. Las entradas se revisan en cada ciclo de auditoría.

---

## Capas del sistema

**Capa Canon**  
Verdad inmutable. Los documentos en `canon/` definen las reglas del sistema.

**Capa Registro**  
Estado activo de herramientas y stacks. Los documentos en `registries/` reflejan las decisiones operativas actuales.

**Capa Ecosistema**  
Mapa de todos los repositorios y sus relaciones. Los documentos en `ecosystem/` reflejan la estructura y el estado actuales del portfolio de Flawless Studio.

**Capa Docs**  
Conocimiento operativo: decisiones, runbooks, auditorías, explicaciones, tutoriales, referencias. Los documentos en `docs/` soportan la operación diaria.

**Capa Agentes**  
Sistemas automatizados que operan bajo contratos definidos. Los contratos de agente son documentos formales que especifican el alcance, la autoridad y las restricciones de cada agente.

---

## Términos de política bilingüe

**EN (autoritativo)**  
El inglés es el idioma autoritativo para todos los documentos canónicos. En cualquier conflicto entre versiones EN y ES, prevalece EN.

**ES (par de paridad)**  
Traducción al español mantenida en paralelo. Indicada por el sufijo `.es.md`. Requerida para todos los archivos canónicos, de gobernanza y raíz.

**Paridad bilingüe**  
El estado en que cada archivo EN requerido tiene un par `.es.md` correspondiente de contenido equivalente. Verificado automáticamente por `validate-bilingual-parity.yml`.

---

## Términos de gobernanza

**ADR (Registro de Decisión de Arquitectura)**  
Registro estructurado de una decisión arquitectónica u operativa significativa. Almacenado en `docs/decisions/`. Formato: contexto → decisión → justificación → consecuencias.

**Auditoría**  
Revisión programada o activada del árbol canónico para verificar exactitud, paridad e integridad estructural. Genera un informe fechado en `docs/audits/`.

**Push-to-main**  
La política de fusión actual: los commits directos a `main` están permitidos para operación en solitario. Esta política está documentada en `GOVERNANCE.md` y es revisable.

---

*Parte del [canon Flawless](../CANON.md).*
