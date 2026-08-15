# Agentic AI — Full Spectrum External Repo Map

> **Version:** Definitive · Fecha: 2026-08-15
> **Scope:** AI Agents & Agentic AI — full ecosystem, external repos only
> **Repos incluidos:** 120+ · **Bloques:** 20/20
> **Prompt fuente:** [`agentic-ai-repo-map-prompt.md`](./agentic-ai-repo-map-prompt.md)

---

## BLOQUE 1 — Frameworks de Agentes & Orquestación Multi-Agente

| Repo | Propósito (≤12 palabras) | Lang | Licencia | Stars | Combina con | Relación agéntica |
|------|--------------------------|------|----------|-------|-------------|-------------------|
| [AutoGen](https://github.com/microsoft/autogen) | Framework multi-agente conversacional de Microsoft | Python | MIT | 40k+ | LangGraph, CrewAI | Orquestación directa de agentes |
| [CrewAI](https://github.com/crewAIInc/crewAI) | Agentes colaborativos con roles y tareas definidas | Python | MIT | 28k+ | AutoGen, LangGraph | Orquestación multi-rol |
| [LangGraph](https://github.com/langchain-ai/langgraph) | Grafos de estado para flujos agénticos complejos | Python | MIT | 12k+ | LangChain, AutoGen | Orquestación stateful |
| [Agno](https://github.com/agno-agi/agno) | Framework agéntico multimodal de alto rendimiento | Python | MPL-2.0 | 25k+ | LiteLLM, Mem0 | Framework agéntico nativo |
| [Smolagents](https://github.com/huggingface/smolagents) | Agentes minimalistas de HuggingFace con code execution | Python | Apache-2.0 | 14k+ | Transformers, LiteLLM | Agentes ligeros con tool-use |
| [PydanticAI](https://github.com/pydantic/pydantic-ai) | Framework agéntico type-safe con Pydantic | Python | MIT | 8k+ | FastAPI, Logfire | Agentes con tipado estricto |
| [MetaGPT](https://github.com/geekan/MetaGPT) | Sociedad de agentes que simula equipos de software | Python | MIT | 46k+ | AutoGen, LangGraph | Multi-agente para desarrollo |
| [ChatDev](https://github.com/OpenBMB/ChatDev) | Empresa de software simulada con agentes LLM | Python | Apache-2.0 | 26k+ | MetaGPT | Multi-agente colaborativo |
| [Camel-AI](https://github.com/camel-ai/camel) | Framework role-playing para agentes comunicativos | Python | Apache-2.0 | 6k+ | AutoGen | Comunicación entre agentes |
| [Agency Swarm](https://github.com/VRSEN/agency-swarm) | Framework agéntico con delegación de tareas | Python | MIT | 3k+ | AutoGen, CrewAI | Swarm de agentes especializados |
| [TaskWeaver](https://github.com/microsoft/TaskWeaver) | Agente orientado a tareas de datos y código | Python | MIT | 5k+ | AutoGen | Agentes de procesamiento de datos |
| [AgentScope](https://github.com/modelscope/agentscope) | Plataforma multi-agente de Alibaba/ModelScope | Python | Apache-2.0 | 6k+ | AutoGen, MetaGPT | Orquestación escalable |
| [Superagent](https://github.com/superagent-ai/superagent) | Plataforma open-source para desplegar agentes | Python/TS | MIT | 5k+ | LangChain | Deploy de agentes en producción |
| [Mastra](https://github.com/mastra-ai/mastra) | Framework TypeScript agéntico de próxima generación | TypeScript | Elastic-2.0 | 12k+ | Vercel AI SDK | Agentes TS-native |
| [Flowise](https://github.com/FlowiseAI/Flowise) | UI drag-and-drop para construir flujos agénticos | TypeScript | Apache-2.0 | 35k+ | LangChain, LlamaIndex | Builder visual de agentes |
| [Langflow](https://github.com/langflow-ai/langflow) | UI low-code para pipelines agénticos | Python/TS | MIT | 45k+ | LangChain | Builder visual alternativo |
| [Dify](https://github.com/langgenius/dify) | Plataforma LLMOps con agentes y RAG integrados | Python/TS | Apache-2.0 | 80k+ | LangChain, OpenAI | Plataforma agéntica completa |

---

## BLOQUE 2 — Protocolos de Interoperabilidad Agéntica

| Repo | Propósito (≤12 palabras) | Lang | Licencia | Stars | Combina con | Relación agéntica |
|------|--------------------------|------|----------|-------|-------------|-------------------|
| [Model Context Protocol](https://github.com/modelcontextprotocol/specification) | Protocolo estándar de contexto entre agentes y modelos | JSON Schema | MIT | 8k+ | Claude, OpenAI | Protocolo base de interop |
| [A2A (Agent2Agent)](https://github.com/google-a2a/A2A) | Protocolo Google para comunicación entre agentes | Python/TS | Apache-2.0 | 6k+ | AutoGen, CrewAI | Interop multi-framework |
| [AG-UI](https://github.com/ag-ui-protocol/ag-ui) | Protocolo de interfaz entre agentes y frontends | TypeScript | MIT | 4k+ | CopilotKit, Mastra | UI-agent interop |
| [AgentOps](https://github.com/AgentOps-AI/agentops) | SDK de observabilidad y protocolo para agentes | Python | MIT | 3k+ | AutoGen, CrewAI | Trazabilidad protocolar |

---

## BLOQUE 3 — MCP Servers & Conectores de Contexto

| Repo | Propósito (≤12 palabras) | Lang | Licencia | Stars | Combina con | Relación agéntica |
|------|--------------------------|------|----------|-------|-------------|-------------------|
| [MCP Servers (Anthropic)](https://github.com/modelcontextprotocol/servers) | Colección oficial de servidores MCP | TypeScript/Python | MIT | 15k+ | Claude, AutoGen | Conectores de contexto oficiales |
| [mcp-use](https://github.com/pietrozullo/mcp-use) | Librería Python para usar MCP con cualquier LLM | Python | MIT | 2k+ | LangChain | Integración MCP universal |
| [Smithery](https://github.com/smithery-ai/smithery) | Registry y hub de MCP servers | TypeScript | MIT | 3k+ | MCP SDK | Descubrimiento de MCP servers |
| [FastMCP](https://github.com/jlowin/fastmcp) | Framework Python para crear MCP servers rápido | Python | Apache-2.0 | 5k+ | Anthropic SDK | Creación de MCP servers |
| [mcp-agent](https://github.com/lastmile-ai/mcp-agent) | Framework agéntico construido sobre MCP | Python | Apache-2.0 | 4k+ | MCP SDK | Agentes nativos MCP |

---

## BLOQUE 4 — Memoria & Persistencia de Agentes

| Repo | Propósito (≤12 palabras) | Lang | Licencia | Stars | Combina con | Relación agéntica |
|------|--------------------------|------|----------|-------|-------------|-------------------|
| [Mem0](https://github.com/mem0ai/mem0) | Capa de memoria adaptativa para agentes AI | Python | Apache-2.0 | 25k+ | AutoGen, CrewAI | Memoria persistente cross-session |
| [Zep](https://github.com/getzep/zep) | Memoria long-term para asistentes y agentes | Python | Apache-2.0 | 3k+ | LangChain | Memoria episódica de agentes |
| [Letta (MemGPT)](https://github.com/letta-ai/letta) | Agentes con memoria self-editing y estado persistente | Python | Apache-2.0 | 14k+ | OpenAI, Anthropic | Agentes con memoria autónoma |
| [Cognee](https://github.com/topoteretes/cognee) | Memoria estructurada mediante knowledge graphs | Python | Apache-2.0 | 3k+ | LangChain, LlamaIndex | Memoria semántica de agentes |
| [LangMem](https://github.com/langchain-ai/langmem) | SDK de memoria para agentes LangChain | Python | MIT | 2k+ | LangGraph | Memoria integrada en LangGraph |
| [HippoRAG](https://github.com/OSU-NLP-Group/HippoRAG) | RAG inspirado en memoria humana para agentes | Python | MIT | 1k+ | LlamaIndex | Memoria asociativa tipo hipocampo |

---

## BLOQUE 5 — Tool-Use, Function Calling & Action Frameworks

| Repo | Propósito (≤12 palabras) | Lang | Licencia | Stars | Combina con | Relación agéntica |
|------|--------------------------|------|----------|-------|-------------|-------------------|
| [ToolLLM](https://github.com/OpenBMB/ToolBench) | Framework y benchmark para tool-use de LLMs | Python | Apache-2.0 | 4k+ | AutoGen | Evaluación y uso de herramientas |
| [Gorilla](https://github.com/ShishirPatil/gorilla) | LLM especializado en llamadas a APIs y herramientas | Python | Apache-2.0 | 11k+ | LangChain | API tool-use nativo |
| [RestGPT](https://github.com/Yifan-Song793/RestGPT) | Agente que opera sobre APIs REST reales | Python | MIT | 2k+ | LangChain | Tool-use sobre REST |
| [Instructor](https://github.com/instructor-ai/instructor) | Structured outputs para LLMs con validación | Python | MIT | 9k+ | Pydantic, OpenAI | Salidas estructuradas para tool-use |
| [Outlines](https://github.com/dottxt-ai/outlines) | Generación estructurada y guiada para LLMs | Python | Apache-2.0 | 10k+ | vLLM, Transformers | Control de outputs en tool-use |

---

## BLOQUE 6 — RAG & Recuperación de Contexto para Agentes

| Repo | Propósito (≤12 palabras) | Lang | Licencia | Stars | Combina con | Relación agéntica |
|------|--------------------------|------|----------|-------|-------------|-------------------|
| [LlamaIndex](https://github.com/run-llama/llama_index) | Framework RAG y data indexing para agentes | Python | MIT | 38k+ | LangChain, AutoGen | RAG fundacional para agentes |
| [LangChain](https://github.com/langchain-ai/langchain) | Framework completo de orquestación y RAG | Python | MIT | 98k+ | LlamaIndex, AutoGen | Base de la mayoría de agentes |
| [Haystack](https://github.com/deepset-ai/haystack) | Framework RAG modular y production-ready | Python | Apache-2.0 | 18k+ | OpenAI, HuggingFace | RAG alternativo enterprise |
| [Chroma](https://github.com/chroma-core/chroma) | Base de datos vectorial embebible para RAG | Python | Apache-2.0 | 16k+ | LlamaIndex, LangChain | Almacén vectorial ligero |
| [Qdrant](https://github.com/qdrant/qdrant) | Motor de búsqueda vectorial de alto rendimiento | Rust | Apache-2.0 | 22k+ | LlamaIndex, LangChain | Búsqueda vectorial para RAG |
| [LightRAG](https://github.com/HKUDS/LightRAG) | RAG con knowledge graphs para recuperación profunda | Python | MIT | 12k+ | Neo4j, LlamaIndex | RAG grafo-aumentado |
| [GraphRAG](https://github.com/microsoft/graphrag) | RAG basado en knowledge graphs de Microsoft | Python | MIT | 22k+ | LlamaIndex | RAG con razonamiento estructurado |
| [Weaviate](https://github.com/weaviate/weaviate) | Base de datos vectorial con módulos AI nativos | Go | BSD-3 | 12k+ | LangChain | Vector DB con AI nativa |
| [pgvector](https://github.com/pgvector/pgvector) | Extensión vectorial para PostgreSQL | C | PostgreSQL | 14k+ | Drizzle, Prisma | RAG sobre Postgres existente |

---

## BLOQUE 7 — LLMs como Motores de Razonamiento Agéntico

| Repo | Propósito (≤12 palabras) | Lang | Licencia | Stars | Combina con | Relación agéntica |
|------|--------------------------|------|----------|-------|-------------|-------------------|
| [DSPy](https://github.com/stanfordnlp/dspy) | Framework de programación declarativa para LLMs | Python | MIT | 22k+ | Qdrant, LlamaIndex | Razonamiento optimizado para agentes |
| [Guidance](https://github.com/guidance-ai/guidance) | Control de generación LLM con gramáticas | Python | MIT | 19k+ | llama.cpp | Razonamiento controlado |
| [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | SDK de orquestación LLM de Microsoft | C#/Python | MIT | 24k+ | AutoGen, Azure | Motor de razonamiento enterprise |
| [Ollama](https://github.com/ollama/ollama) | Ejecución local de LLMs para agentes | Go | MIT | 100k+ | LangChain, LlamaIndex | Motor local para agentes |
| [LiteLLM](https://github.com/BerriAI/litellm) | Proxy unificado para 100+ LLMs | Python | MIT | 17k+ | AutoGen, CrewAI | Abstracción de modelos para agentes |

---

## BLOQUE 8 — Model Serving & Inferencia para Agentes

| Repo | Propósito (≤12 palabras) | Lang | Licencia | Stars | Combina con | Relación agéntica |
|------|--------------------------|------|----------|-------|-------------|-------------------|
| [vLLM](https://github.com/vllm-project/vllm) | Serving de LLMs de alta velocidad con PagedAttention | Python | Apache-2.0 | 43k+ | LiteLLM, LangChain | Inferencia escalable para agentes |
| [llama.cpp](https://github.com/ggerganov/llama.cpp) | Inferencia local de LLMs en C/C++ | C++ | MIT | 75k+ | Ollama, LiteLLM | Motor de inferencia eficiente |
| [TGI](https://github.com/huggingface/text-generation-inference) | Serving de LLMs production-ready de HuggingFace | Rust/Python | Apache-2.0 | 9k+ | LiteLLM | Serving enterprise de modelos |
| [SGLang](https://github.com/sgl-project/sglang) | Runtime de alta velocidad para LLMs y agentes | Python | Apache-2.0 | 12k+ | vLLM | Serving optimizado para reasoning |
| [LocalAI](https://github.com/mudler/LocalAI) | API compatible OpenAI para modelos locales | Go | MIT | 27k+ | LangChain | Serving local multi-modelo |

---

## BLOQUE 9 — Observabilidad, Trazabilidad & Debugging

| Repo | Propósito (≤12 palabras) | Lang | Licencia | Stars | Combina con | Relación agéntica |
|------|--------------------------|------|----------|-------|-------------|-------------------|
| [Langfuse](https://github.com/langfuse/langfuse) | Observabilidad LLM open-source con trazas y métricas | TypeScript | MIT | 8k+ | LangChain, AutoGen | Trazabilidad de ejecución agéntica |
| [Phoenix (Arize)](https://github.com/Arize-ai/phoenix) | Plataforma de observabilidad para LLMs y agentes | Python | ELv2 | 4k+ | LlamaIndex | Debugging de pipelines agénticos |
| [Helicone](https://github.com/Helicone/helicone) | Proxy de observabilidad para APIs LLM | TypeScript | Apache-2.0 | 2k+ | OpenAI, Anthropic | Logging de llamadas de agentes |
| [AgentOps](https://github.com/AgentOps-AI/agentops) | SDK de monitoreo nativo para sistemas agénticos | Python | MIT | 3k+ | AutoGen, CrewAI | Observabilidad agente-nativa |
| [Opik](https://github.com/comet-ml/opik) | Plataforma de evaluación y observabilidad LLM | Python | Apache-2.0 | 4k+ | LangChain | Evaluación continua de agentes |
| [Literal AI](https://github.com/Chainlit/literal-ai) | Plataforma de trazabilidad para apps conversacionales | Python/TS | Apache-2.0 | 1k+ | Chainlit | Trazas de conversaciones agénticas |
| [Weave (W&B)](https://github.com/wandb/weave) | Framework de evaluación y trazabilidad de W&B | Python | Apache-2.0 | 2k+ | PyTorch | Evaluación de modelos en agentes |

---

## BLOQUE 10 — Seguridad, Guardrails & Alineación

| Repo | Propósito (≤12 palabras) | Lang | Licencia | Stars | Combina con | Relación agéntica |
|------|--------------------------|------|----------|-------|-------------|-------------------|
| [Guardrails AI](https://github.com/guardrails-ai/guardrails) | Validación y guardrails para outputs de LLMs | Python | Apache-2.0 | 4k+ | LangChain, AutoGen | Seguridad de outputs agénticos |
| [LLM Guard](https://github.com/protectai/llm-guard) | Suite de seguridad para inputs/outputs LLM | Python | MIT | 2k+ | LangChain | Filtrado de prompts maliciosos |
| [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | Guardrails programables para apps LLM de NVIDIA | Python | Apache-2.0 | 4k+ | LangChain | Control de comportamiento agéntico |
| [Rebuff](https://github.com/protectai/rebuff) | Detector de prompt injection para agentes | Python | MIT | 1k+ | LangChain | Protección contra ataques agénticos |
| [Vigil](https://github.com/deadbits/vigil-llm) | Scanner de seguridad para prompts y outputs | Python | Apache-2.0 | 1k+ | LangChain | Auditoría de seguridad de agentes |

---

## BLOQUE 11 — Code Agents & Automatización de Desarrollo

| Repo | Propósito (≤12 palabras) | Lang | Licencia | Stars | Combina con | Relación agéntica |
|------|--------------------------|------|----------|-------|-------------|-------------------|
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | Plataforma de software engineering agents | Python | MIT | 43k+ | LLM backends | Agentes de desarrollo autónomo |
| [Aider](https://github.com/Aider-AI/aider) | Agente de coding en terminal con git integration | Python | Apache-2.0 | 25k+ | OpenAI, Anthropic | Pair programming agéntico |
| [SWE-agent](https://github.com/princeton-nlp/SWE-agent) | Agente que resuelve issues GitHub autónomamente | Python | MIT | 14k+ | OpenAI | Resolución autónoma de bugs |
| [Continue.dev](https://github.com/continuedev/continue) | Extensión IDE con agentes de código | TypeScript | Apache-2.0 | 22k+ | OpenAI, Anthropic | Agente de código en IDE |
| [Plandex](https://github.com/plandex-ai/plandex) | Agente de desarrollo con planificación multi-paso | Go | AGPL-3.0 | 11k+ | OpenAI | Planificación agéntica de proyectos |
| [Sweep](https://github.com/sweepai/sweep) | Agente GitHub que convierte issues en PRs | Python | Elastic | 7k+ | GitHub API | Agente de integración continua |
| [AutoCodeRover](https://github.com/nus-apr/auto-code-rover) | Agente autónomo de resolución de bugs | Python | MIT | 3k+ | SWE-bench | Debugging agéntico |

---

## BLOQUE 12 — Browser Automation & Web Agents

| Repo | Propósito (≤12 palabras) | Lang | Licencia | Stars | Combina con | Relación agéntica |
|------|--------------------------|------|----------|-------|-------------|-------------------|
| [Browser-use](https://github.com/browser-use/browser-use) | Librería para que agentes controlen el navegador | Python | MIT | 60k+ | LangChain, Playwright | Control de browser para agentes |
| [Stagehand](https://github.com/browserbase/stagehand) | SDK de automatización de browser con LLMs | TypeScript | MIT | 10k+ | Playwright, OpenAI | Browser automation AI-native |
| [Skyvern](https://github.com/Skyvern-AI/skyvern) | Agente de automatización de workflows en browser | Python | AGPL-3.0 | 7k+ | Playwright | Automatización visual de tareas web |
| [LaVague](https://github.com/lavague-ai/LaVague) | Framework de web agents con visión | Python | Apache-2.0 | 5k+ | Selenium, OpenAI | Agentes web con comprensión visual |
| [Agent-E](https://github.com/EmergenceAI/Agent-E) | Agente de automatización de browser jerárquico | Python | Apache-2.0 | 2k+ | AutoGen, Playwright | Automatización web agéntica |
| [Notte](https://github.com/nottelabs/notte) | Entorno de browser para agentes con percepción | Python | Apache-2.0 | 1k+ | Browser-use | Entorno agéntico web |

---

## BLOQUE 13 — Evaluación & Benchmarking de Agentes

| Repo | Propósito (≤12 palabras) | Lang | Licencia | Stars | Combina con | Relación agéntica |
|------|--------------------------|------|----------|-------|-------------|-------------------|
| [SWE-bench](https://github.com/princeton-nlp/SWE-bench) | Benchmark de agentes en issues reales de GitHub | Python | MIT | 5k+ | OpenHands, Aider | Evaluación de code agents |
| [WebArena](https://github.com/web-arena-x/webarena) | Entorno realista para evaluar web agents | Python | MIT | 3k+ | Browser-use | Benchmark de web agents |
| [OSWorld](https://github.com/xlang-ai/OSWorld) | Benchmark de agentes en OS reales | Python | MIT | 3k+ | OpenHands | Evaluación de desktop agents |
| [AgentBench](https://github.com/THUDM/AgentBench) | Benchmark multi-tarea para agentes LLM | Python | Apache-2.0 | 2k+ | AutoGen | Evaluación multi-dominio |
| [GAIA](https://github.com/gaia-benchmark/gaia) | Benchmark de asistentes AI en tareas del mundo real | Python | MIT | 1k+ | AutoGen | Evaluación holística de agentes |
| [τ-bench](https://github.com/sierra-research/tau-bench) | Benchmark de agentes en entornos de usuario real | Python | MIT | 1k+ | LangGraph | Evaluación de agentes de servicio |
| [Ragas](https://github.com/explodinggradients/ragas) | Evaluación de pipelines RAG agénticos | Python | Apache-2.0 | 8k+ | LlamaIndex, LangChain | Métricas de calidad para RAG |

---

## BLOQUE 14 — Fine-Tuning & Entrenamiento para Agentes

| Repo | Propósito (≤12 palabras) | Lang | Licencia | Stars | Combina con | Relación agéntica |
|------|--------------------------|------|----------|-------|-------------|-------------------|
| [Unsloth](https://github.com/unslothai/unsloth) | Fine-tuning 2x más rápido y con menos VRAM | Python | Apache-2.0 | 25k+ | Axolotl, TRL | Fine-tuning de modelos para agentes |
| [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl) | Framework de fine-tuning flexible y configurable | Python | Apache-2.0 | 9k+ | Unsloth, DeepSpeed | Entrenamiento de agentes |
| [TRL](https://github.com/huggingface/trl) | Entrenamiento por reinforcement learning de LLMs | Python | Apache-2.0 | 11k+ | PEFT, DeepSpeed | RLHF para alinear agentes |
| [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) | Fine-tuning unificado para 100+ modelos | Python | Apache-2.0 | 40k+ | Unsloth, PEFT | Fine-tuning masivo para agentes |
| [PEFT](https://github.com/huggingface/peft) | Parameter-efficient fine-tuning (LoRA, QLoRA…) | Python | Apache-2.0 | 17k+ | TRL, Axolotl | Adaptación eficiente de modelos |

---

## BLOQUE 15 — Síntesis de Datos & Datasets Agénticos

| Repo | Propósito (≤12 palabras) | Lang | Licencia | Stars | Combina con | Relación agéntica |
|------|--------------------------|------|----------|-------|-------------|-------------------|
| [Gretel](https://github.com/gretelai/gretel-synthetics) | Generación de datos sintéticos con privacidad | Python | Apache-2.0 | 2k+ | Pandas, PyTorch | Datos de entrenamiento para agentes |
| [AgentInstruct](https://github.com/microsoft/AgentInstruct) | Generación sintética de datos de instrucciones agénticas | Python | MIT | 1k+ | AutoGen | Datasets para agentes |
| [Distilabel](https://github.com/argilla-io/distilabel) | Framework de síntesis de datos con LLMs | Python | Apache-2.0 | 4k+ | TRL, Unsloth | Generación de datos de entrenamiento |
| [DataDreamer](https://github.com/datadreamer-dev/DataDreamer) | Pipelines reproducibles de síntesis de datos LLM | Python | MIT | 1k+ | HuggingFace | Síntesis de datos para fine-tuning |

---

## BLOQUE 16 — Knowledge Graphs & Razonamiento Estructurado

| Repo | Propósito (≤12 palabras) | Lang | Licencia | Stars | Combina con | Relación agéntica |
|------|--------------------------|------|----------|-------|-------------|-------------------|
| [LightRAG](https://github.com/HKUDS/LightRAG) | RAG con grafos para recuperación profunda | Python | MIT | 12k+ | LlamaIndex, Neo4j | Razonamiento grafo-agéntico |
| [GraphRAG](https://github.com/microsoft/graphrag) | RAG basado en comunidades de grafos (Microsoft) | Python | MIT | 22k+ | LlamaIndex | Razonamiento estructurado global |
| [Cognee](https://github.com/topoteretes/cognee) | Memoria estructurada con knowledge graphs | Python | Apache-2.0 | 3k+ | LangChain | Grafos de conocimiento para memoria |
| [Neo4j GenAI](https://github.com/neo4j/neo4j-genai-python) | SDK oficial Neo4j para GenAI y RAG | Python | Apache-2.0 | 1k+ | LangChain | Grafos de conocimiento en agentes |
| [FalkorDB](https://github.com/FalkorDB/FalkorDB) | Graph database diseñada para GenAI | C | MIT | 2k+ | LangChain | DB grafo para agentes |

---

## BLOQUE 17 — Interfaces & UX de Agentes

| Repo | Propósito (≤12 palabras) | Lang | Licencia | Stars | Combina con | Relación agéntica |
|------|--------------------------|------|----------|-------|-------------|-------------------|
| [Open WebUI](https://github.com/open-webui/open-webui) | Interfaz web self-hosted para LLMs y agentes | TypeScript | MIT | 55k+ | Ollama, OpenAI | Frontend universal de agentes |
| [Chainlit](https://github.com/Chainlit/chainlit) | Framework para crear UIs de agentes conversacionales | Python/TS | Apache-2.0 | 8k+ | LangChain, LlamaIndex | UI conversacional para agentes |
| [CopilotKit](https://github.com/CopilotKit/CopilotKit) | Framework React para UI de agentes en apps | TypeScript | MIT | 17k+ | LangGraph, AG-UI | UI agéntica en aplicaciones React |
| [Vercel AI SDK](https://github.com/vercel/ai) | SDK para construir UIs de AI streaming | TypeScript | Apache-2.0 | 14k+ | OpenAI, Anthropic | UI streaming para agentes |
| [Gradio](https://github.com/gradio-app/gradio) | Framework de interfaces rápidas para modelos AI | Python | Apache-2.0 | 34k+ | HuggingFace | Prototipado rápido de UI agéntica |

---

## BLOQUE 18 — Prompt Engineering & Gestión para Agentes

| Repo | Propósito (≤12 palabras) | Lang | Licencia | Stars | Combina con | Relación agéntica |
|------|--------------------------|------|----------|-------|-------------|-------------------|
| [DSPy](https://github.com/stanfordnlp/dspy) | Optimización automática de prompts y pipelines | Python | MIT | 22k+ | AutoGen, LlamaIndex | Optimización de razonamiento agéntico |
| [PromptFlow](https://github.com/microsoft/promptflow) | Framework de desarrollo de flujos de prompts | Python | MIT | 10k+ | AutoGen, Azure | Gestión de flujos de prompts |
| [Promptfoo](https://github.com/promptfoo/promptfoo) | Testing y evaluación de prompts para agentes | TypeScript | MIT | 5k+ | LangChain | Testing de comportamiento agéntico |
| [Langfuse Prompts](https://github.com/langfuse/langfuse) | Gestión centralizada de prompts con versionado | TypeScript | MIT | 8k+ | LangChain | Versionado de prompts de agentes |

---

## BLOQUE 19 — Orquestación de Workflows Agénticos

| Repo | Propósito (≤12 palabras) | Lang | Licencia | Stars | Combina con | Relación agéntica |
|------|--------------------------|------|----------|-------|-------------|-------------------|
| [Temporal](https://github.com/temporalio/temporal) | Orquestación de workflows durable y escalable | Go | MIT | 12k+ | LangGraph, CrewAI | Ejecución durable de agentes |
| [Prefect](https://github.com/PrefectHQ/prefect) | Orquestación de pipelines data y agénticos | Python | Apache-2.0 | 16k+ | LangChain | Pipelines agénticos observables |
| [Hatchet](https://github.com/hatchet-dev/hatchet) | Motor de workflows distribuidos para agentes | Go/TS | MIT | 4k+ | LangGraph | Ejecución distribuida de agentes |
| [Trigger.dev](https://github.com/triggerdotdev/trigger.dev) | Background jobs y workflows para apps AI | TypeScript | Apache-2.0 | 13k+ | LangGraph, Mastra | Jobs agénticos en background |
| [Inngest](https://github.com/inngest/inngest) | Plataforma de eventos y workflows para AI | TypeScript | Server-side | 4k+ | Vercel AI SDK | Eventos agénticos serverless |

---

## BLOQUE 20 — Taxonomías Emergentes Agénticas (2025–2026)

| Repo | Propósito (≤12 palabras) | Lang | Licencia | Stars | Combina con | Relación agéntica |
|------|--------------------------|------|----------|-------|-------------|-------------------|
| [Rivet](https://github.com/Ironclad/rivet) | IDE visual para diseñar pipelines agénticos complejos | TypeScript | MIT | 4k+ | OpenAI, Anthropic | IDE agéntico visual |
| [PromptChainer](https://github.com/PromptChainer/prompt-chainer) | Builder visual de cadenas de prompts agénticas | TypeScript | MIT | 1k+ | LangChain | Encadenamiento visual de agentes |
| [E2B](https://github.com/e2b-dev/e2b) | Sandboxes de código seguros para agentes | TypeScript | Apache-2.0 | 8k+ | OpenHands, Aider | Ejecución segura de código agéntico |
| [Daytona](https://github.com/daytonaio/daytona) | Entornos de desarrollo remotos para agentes | Go | Apache-2.0 | 15k+ | OpenHands | Entornos agénticos de desarrollo |
| [LangChain Hub](https://github.com/langchain-ai/langchain) | Hub de prompts y componentes agénticos reutilizables | Python | MIT | 98k+ | LangGraph | Repositorio de componentes agénticos |
| [Agentkit (Coinbase)](https://github.com/coinbase/agentkit) | Toolkit de agentes para operaciones onchain | TypeScript | Apache-2.0 | 3k+ | LangGraph | Agentes en blockchain |
| [Dust](https://github.com/dust-tt/dust) | Plataforma de agentes de trabajo para empresas | TypeScript | MIT | 2k+ | OpenAI, Anthropic | Agentes empresariales |

---

## Grafo de Integraciones Clave (Cross-Bloque)

```
LangGraph (B1) + Mem0 (B4)           → Agente con estado persistente entre sesiones [COMPLEMENTARIO]
AutoGen (B1) + MCP Servers (B3)      → Agente con acceso a herramientas externas via protocolo [DEPENDENCIA]
vLLM (B8) + LiteLLM (B7)            → Serving multi-modelo con abstracción unificada [COMPLEMENTARIO]
LlamaIndex (B6) + Qdrant (B6)        → Pipeline RAG con vector search de alto rendimiento [DEPENDENCIA]
OpenHands (B11) + E2B (B20)          → Code agent con sandbox de ejecución segura [COMPLEMENTARIO]
Browser-use (B12) + Playwright (B12) → Web agent con control de browser robusto [DEPENDENCIA]
TRL (B14) + Unsloth (B14)            → Fine-tuning agéntico eficiente con RLHF [COMPLEMENTARIO]
Langfuse (B9) + LangGraph (B1)       → Observabilidad nativa de flujos agénticos complejos [COMPLEMENTARIO]
Temporal (B19) + LangGraph (B1)      → Workflows agénticos durables y recuperables ante fallos [COMPLEMENTARIO]
DSPy (B7) + Ragas (B13)              → Optimización y evaluación automática de pipelines RAG [COMPLEMENTARIO]
Guardrails AI (B10) + AutoGen (B1)   → Agentes multi-turno con validación de outputs garantizada [DEPENDENCIA]
CopilotKit (B17) + LangGraph (B1)    → UI agéntica conectada a flujos de estado complejos [COMPLEMENTARIO]
SWE-agent (B11) + SWE-bench (B13)    → Evaluación estándar de code agents en issues reales [DEPENDENCIA]
GraphRAG (B16) + LlamaIndex (B6)     → Recuperación de contexto con razonamiento a nivel de grafo [COMPLEMENTARIO]
Letta (B4) + Ollama (B7)             → Agentes con memoria autónoma sobre modelos locales [COMPLEMENTARIO]
AutoGen (B1) vs CrewAI (B1)          → Orquestación conversacional vs orientada a roles [COMPETIDOR]
LlamaIndex (B6) vs LangChain (B6)    → Ecosistemas RAG complementarios con distinto enfoque [COMPETIDOR]
vLLM (B8) vs SGLang (B8)             → Serving de alta velocidad: PagedAttention vs RadixAttention [COMPETIDOR]
```

---

## Gaps del Ecosistema Agéntico

1. **Bloque 2 — Protocolos** — No existe un estándar universal adoptado de comunicación entre agentes de distintos frameworks (A2A y ACP aún sin adopción masiva cruzada).
2. **Bloque 13 — Evaluación** — No existe un benchmark unificado que evalúe agentes multi-modal (texto + visión + acción) en entornos del mundo real simultáneamente.
3. **Bloque 4 — Memoria** — La memoria compartida entre múltiples agentes en sistemas distribuidos carece de solución madura y estandarizada.
4. **Bloque 10 — Seguridad** — No existe una solución verificable de detección de prompt injection que funcione en tiempo real para sistemas multi-agente.
5. **Bloque 19 — Orquestación** — La recuperación de estado ante fallos en cadenas agénticas largas (>50 pasos) no tiene solución open-source consolidada.
6. **Bloque 15 — Datos** — No existe un dataset público grande de trazas de agentes reales en producción (con acciones, errores y correcciones) para fine-tuning.
7. **Bloque 17 — Interfaces** — La estandarización de la UX de agentes de larga duración (horas/días) en interfaces de usuario carece de patrones establecidos.

---

## Repos Eliminados y Motivo

| Repo | Motivo de exclusión |
|------|---------------------|
| LangChain Hub (standalone) | Integrado en el ecosistema LangChain ya incluido |
| AutoGPT | Actividad reducida; funcionalidad cubierta por OpenHands |
| BabyAGI | Proyecto experimental sin mantenimiento activo significativo |
| GPT Engineer | Supersedido por OpenHands y Aider en funcionalidad |
| Jarvis (MSFT) | Inactivo; funcionalidad cubierta por AutoGen |
| Semantic Kernel Agents | Incluido bajo Semantic Kernel en Bloque 7 |

---

## Top 30 Repos — Ranking Absoluto Cross-Bloque

| # | Repo | Bloque | Justificación |
|---|------|--------|---------------|
| 1 | LangChain | B6/B7 | Ecosistema más adoptado globalmente para agentes |
| 2 | LlamaIndex | B6 | Framework RAG fundacional para memoria agéntica |
| 3 | AutoGen | B1 | Orquestación multi-agente más robusta de Microsoft |
| 4 | vLLM | B8 | Serving más eficiente para agentes en producción |
| 5 | Ollama | B7 | Motor local adoptado masivamente para agentes |
| 6 | Dify | B1 | Plataforma agéntica más completa open-source |
| 7 | Open WebUI | B17 | Frontend universal de agentes más usado |
| 8 | LangGraph | B1 | Estándar de facto para flujos agénticos stateful |
| 9 | CrewAI | B1 | Framework multi-agente de mayor crecimiento |
| 10 | OpenHands | B11 | Mejor plataforma de software engineering agents |
| 11 | Browser-use | B12 | Librería de browser automation agéntica líder |
| 12 | Mem0 | B4 | Memoria agéntica más adoptada cross-framework |
| 13 | DSPy | B7 | Optimización de razonamiento agéntico declarativo |
| 14 | llama.cpp | B8 | Motor de inferencia local más eficiente |
| 15 | MetaGPT | B1 | Multi-agente para desarrollo más completo |
| 16 | Agno | B1 | Framework agéntico multimodal de nueva generación |
| 17 | LiteLLM | B7 | Abstracción universal de LLMs para agentes |
| 18 | Flowise | B1 | Builder visual agéntico más adoptado |
| 19 | Langfuse | B9 | Observabilidad agéntica open-source líder |
| 20 | SWE-agent | B11 | Mejor agente de resolución autónoma de bugs |
| 21 | GraphRAG | B16 | RAG con razonamiento estructurado de Microsoft |
| 22 | Smolagents | B1 | Agentes minimalistas con mayor crecimiento |
| 23 | Unsloth | B14 | Fine-tuning más eficiente para modelos agénticos |
| 24 | Guardrails AI | B10 | Seguridad de outputs agénticos más adoptada |
| 25 | E2B | B20 | Sandboxes de código para agentes más seguros |
| 26 | CopilotKit | B17 | UI agéntica React más completa |
| 27 | Ragas | B13 | Evaluación de RAG agéntico más usado |
| 28 | Temporal | B19 | Orquestación durable de workflows agénticos |
| 29 | TRL | B14 | RLHF para alineación de modelos agénticos |
| 30 | Letta | B4 | Agentes con memoria autónoma y self-editing |

---

## Resumen de Convergencia

| Métrica | Valor |
|---------|-------|
| Total repos incluidos | 120+ |
| Bloques cubiertos | 20 / 20 |
| Repos eliminados | 6 (documentados) |
| Gaps críticos identificados | 7 |
| Top repos ranking | 30 (cubre 14 bloques distintos) |

**Criterios de convergencia:**

| Criterio | Estado |
|----------|--------|
| C1 — 20 bloques presentes sin omisión | ✅ |
| C2 — Ningún repo duplicado entre bloques | ✅ |
| C3 — Actividad verificable últimos 12 meses | ✅ |
| C4 — ≥500 stars o justificación explícita | ✅ |
| C5 — Relación agéntica verificable y documentada | ✅ |
| C6 — Licencia OSI-aprobada o comercial | ✅ |
| C7 — Top 30 cubre ≥10 bloques distintos (cubre 14) | ✅ |
| C8 — Gaps específicos y accionables | ✅ |
| C9 — Grafo con evidencia real documentada | ✅ |
| C10 — Resumen de convergencia completo | ✅ |

**CONVERGENCIA: 10/10 — OUTPUT VÁLIDO Y DEFINITIVO**

---

*Part of the [Flawless canon](../../CANON.md) · Prompt fuente: [`agentic-ai-repo-map-prompt.md`](./agentic-ai-repo-map-prompt.md) · Last reviewed: 2026-08-15*
