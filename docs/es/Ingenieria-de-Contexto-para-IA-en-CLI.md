# Arquitectura Integral para Ingeniería de Contexto en Ecosistemas Windows
## Protocolos, Automatización y Orquestación de Agentes de IA

### 1. Introducción — El Cambio de Paradigma hacia la Ingeniería de Contexto

La irrupción de los Modelos de Lenguaje Grande (LLM) ha transformado radicalmente el flujo de trabajo en la ingeniería de software. La industria ha superado la fase inicial de Ingeniería de Prompts para adentrarse en una disciplina más técnica y arquitectónica: la **Ingeniería de Contexto**.

Mientras que el prompt es efímero y transaccional, el contexto es el sustrato cognitivo persistente sobre el cual opera la inteligencia artificial.

### 2. Fundamentos Teóricos de la Ingeniería de Contexto

La ventana de contexto de un LLM no es simplemente un búfer de memoria; es el espacio de trabajo cognitivo del modelo.

#### 2.1 La Economía de la Ventana de Contexto

Existe un sesgo de primacía y recencia: la información ubicada al principio y al final del prompt tiene mayor probabilidad de ser atendida y procesada correctamente.

### 3. El Ecosistema Windows como Host de IA

Con la llegada de WSL2 y PowerShell Core 7.x, Windows se ha convertido en una plataforma de primer nivel para la orquestación de IA.

### 4. El Protocolo de Contexto de Modelo (MCP)

MCP estandariza cómo los asistentes de IA (Clientes) descubren y consumen recursos (Servidores). La arquitectura MCP se desglosa en tres roles: Host, Cliente y Servidor.

### 5. Orquestación de Herramientas y Agentes CLI

* **Fabric:** Biblioteca de Patrones de IA — brilla cuando se integra en la tubería de PowerShell.
* **Aider:** Agente de codificación en línea de comandos con mapa de repositorio.
* **LLM (Simon Willison):** Interfaz unificada para múltiples modelos con logging en SQLite.
* **DuckDB:** Motor de análisis SQL OLAP para datos estructurados locales.

### 6. Implementación Práctica — Suite Win-Omarchy

Esta suite de scripts y configuraciones transforma una instalación estándar de Windows en una estación de trabajo de Ingeniería de Contexto de vanguardia.