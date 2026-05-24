# AGENTS

> Multi-agent system specification for the Flawless ecosystem.

## System Design Principles

1. **Contract-first** — No agent operates without a formal contract.
2. **Minimal scope** — Each agent does one thing well. No agent is general-purpose.
3. **Traceable handoffs** — Every inter-agent transfer is documented.
4. **Founder as arbiter** — All escalations route to the Founder.

## Active Agents

| ID | Name | Role |
|---|---|---|
| `schema-guard` | SchemaGuard | Schema integrity validation |
| `nc-intake` | NCIntake | Non-conformity intake and triage |
| `mr-reporter` | MRReporter | Management review report generation |

## Orchestration Flow

```
Founder → Task → Agent Contract → Agent Execution → Output → Audit Log
                                         ↓
                              Escalation (if blocked)
                                         ↓
                                      Founder
```

---

_Last reviewed: May 2026_
