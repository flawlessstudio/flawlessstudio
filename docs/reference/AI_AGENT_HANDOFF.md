# AI Agent Handoff Protocol

> Standard procedure for transferring context between AI agents in the Flawless ecosystem.

## Handoff Package

Every handoff must include:

```yaml
handoff:
  from: {source-agent-id}
  to: {target-agent-id}
  timestamp: {ISO-8601}
  task_id: {task-id}
  status: completed|partial|blocked
  context:
    summary: {one-paragraph summary of work done}
    outputs: [{list of produced artifacts}]
    open_items: [{unresolved items for next agent}]
  escalation_needed: true|false
```

## Rules

1. Never hand off without a complete package.
2. If `status: blocked`, escalate to Founder before handing off.
3. Receiving agent must confirm receipt before acting.

---

_Last reviewed: May 2026_
