# Agent Contracts

> Formal specifications for all AI agents operating within the Flawless ecosystem. Every agent must have a contract before it can operate.

## Contract Template

```yaml
agent:
  id: {agent-id}
  name: {Human-readable name}
  version: {semver}
  role: {one-line role description}
  scope:
    in: [{what it can touch}]
    out: [{what it cannot touch}]
  inputs:
    - name: {input-name}
      type: {type}
      required: true|false
  outputs:
    - name: {output-name}
      type: {type}
  constraints:
    - {constraint 1}
    - {constraint 2}
  escalation: {what to do when blocked}
```

## Active Contracts

| Agent ID | Role | Status |
|---|---|---|
| `schema-guard` | Validates schema integrity across repos | Draft |
| `nc-intake` | Processes non-conformity reports | Draft |
| `mr-reporter` | Generates management review reports | Draft |

---

_Contracts must be reviewed every 90 days or on major system change._
_Last reviewed: May 2026_
