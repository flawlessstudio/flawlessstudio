# Desarrollo Web Full-Stack e Infraestructura de Empresas Autónomas Impulsadas por IA

> Runbook operativo. Fuente: conocimiento transferido desde docs/es/.

---

## El nuevo stack de la empresa autónoma

Una empresa autónoma impulsada por IA no es una empresa con chatbots. Es una organización donde los sistemas de IA ejecutan procesos completos de negocio con supervisión humana mínima.

### Capas de la infraestructura

| Capa | Tecnología | Rol |
|---|---|---|
| **Frontend** | Next.js / React / Astro | Interfaz de usuario y dashboards |
| **Backend** | Node.js / FastAPI / Rust | APIs, lógica de negocio |
| **Agentes IA** | Claude / GPT-4o / Gemini | Ejecución de tareas autónomas |
| **Orquestación** | n8n / Make / LangGraph | Flujos de trabajo multi-agente |
| **Base de datos** | Supabase / PostgreSQL / Redis | Persistencia y caché |
| **Infraestructura** | Vercel / Railway / Docker | Despliegue y contenedorización |
| **Monitoreo** | Sentry / PostHog / Grafana | Observabilidad |

## Principios de diseño

1. **API-first** — Todo es un endpoint. Los agentes consumen APIs como los humanos consumen UIs.
2. **Stateless agents** — Los agentes no guardan estado. El estado vive en la base de datos.
3. **Contract-driven** — Cada agente tiene un contrato formal. Ver `docs/reference/agent-contracts.md`.
4. **Observable by default** — Todo output de agente se loguea y es auditable.

## Stack Flawless

El stack de Flawless Studio sigue estos principios con TypeScript como lenguaje principal, Vercel como plataforma de despliegue, y Claude como agente de razonamiento primario.

---

_Última revisión: Mayo 2026_
