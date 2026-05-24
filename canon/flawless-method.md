# Flawless Method

> The decision-making method of Flawless Studio. How every problem is approached, every system is designed, and every change is validated.

## The Method

```
Understand → Scope → Plan → Execute → Verify → Document
```

### 1. Understand
- State the objective in one sentence.
- Identify constraints, context, and canonical references.

### 2. Scope
- Define minimum sufficient scope.
- List what is explicitly out of scope.

### 3. Plan
- Produce a minimal execution plan.
- Identify risks before acting.

### 4. Execute
- Controlled, atomic actions.
- One subgoal at a time.

### 5. Verify
- Audit the output against the objective.
- Apply the Flawless Filter.

### 6. Document
- Record the decision in `docs/decisions/`.
- Update the relevant canonical document if impacted.

## Anti-patterns

| Anti-pattern | Consequence |
|---|---|
| Skipping scope | Scope creep, wasted effort |
| Acting without planning | Silent failures, hard rollbacks |
| Undocumented decisions | Knowledge loss, repeated mistakes |
| Duplicate sources of truth | Contradictions, confusion |

---

_Version: 1.0 · Last reviewed: May 2026_
