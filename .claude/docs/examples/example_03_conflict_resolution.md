# Example 03: Conflict Resolution Protocol (CRP) in Action

**Scenario**: Three conflict types encountered during mapping of `alpha-tools/dev-kit`.
**Demonstrates**: CRP priority ladder, name slug vs display_name, enum escalation, branch version conflict.

---

## Conflict 1: Name Slug vs Display Name

**Source A** (SKILL.md frontmatter — priority 1):
```yaml
name: typescript-refactor
```

**Source B** (plugin.json — priority 2):
```json
{ "display_name": "TypeScript Refactoring Assistant" }
```

**Source C** (claudemarketplaces.com page title — priority 4):
```
"TypeScript Refactor"
```

**CRP Decision**:
```json
{
  "field": "name",
  "source_a": "SKILL.md frontmatter",
  "value_a": "typescript-refactor",
  "source_b": "plugin.json",
  "value_b": "TypeScript Refactoring Assistant",
  "resolution": "KEEP_BOTH",
  "outcome": {
    "slug": "typescript-refactor",
    "display_name": "TypeScript Refactoring Assistant"
  },
  "note": "slug and display_name are different fields — no actual conflict"
}
```

**Rule**: Slug (from path) and display_name (from frontmatter/plugin.json) are stored separately. This is not a true conflict — keep both.

---

## Conflict 2: License Enum Escalation

**Source A** (SKILL.md frontmatter — priority 1):
```yaml
license: MIT
```

**Source B** (LICENSE file in repo — priority 5):
```
Apache License
Version 2.0
```

**Analysis**:
- SKILL.md says `MIT`
- Actual LICENSE file says `Apache-2.0`
- These are incompatible — someone made a mistake

**CRP Decision**:
```json
{
  "field": "license",
  "source_a": "SKILL.md frontmatter",
  "value_a": "MIT",
  "source_b": "LICENSE file",
  "value_b": "Apache-2.0",
  "resolution": "ESCALATE",
  "kept_value": "MIT",
  "confidence": "low",
  "note": "SPDX conflict between frontmatter and LICENSE file. Kept frontmatter per priority ladder. Flagged as low confidence for human review.",
  "requires_human_review": true
}
```

**Rule**: SKILL.md frontmatter wins per priority ladder (priority 1 > priority 5), but `confidence` is downgraded to `"low"` and `requires_human_review: true` is set. This surfaces in the `validation_errors` output.

---

## Conflict 3: Branch Version Conflict

**Context**: `alpha-tools/dev-kit` has two active branches with different SKILL.md versions.

**Source A** (branch `main`, SKILL.md — priority 1):
```yaml
version: 2.1.0
```

**Source B** (branch `v2`, SKILL.md — priority 1, same source type):
```yaml
version: 2.3.0-beta
```

**CRP Decision** (version conflict, same priority level):
```json
{
  "field": "version",
  "source_a": "SKILL.md @ main",
  "value_a": "2.1.0",
  "source_b": "SKILL.md @ v2",
  "value_b": "2.3.0-beta",
  "resolution": "SEMVER_HIGHER",
  "kept_value": "2.3.0-beta",
  "note": "Both sources are SKILL.md frontmatter (same priority). Semver comparison: 2.3.0-beta > 2.1.0. Kept higher version, recorded both branches.",
  "branches_found": ["main", "v2"]
}
```

**Rule DR-version**: When same-priority sources conflict on a semver field, keep the higher version. When non-semver: keep frontmatter source, log both.

---

## Conflict 4: Unresolvable Conflict

**Scenario**: `description` field differs across all 5 priority levels with no clear winner:

```
P1 (SKILL.md):    "Refactor TypeScript code with AI assistance"
P2 (plugin.json): "TypeScript refactoring tool"
P3 (README.md):   "An AI-powered tool for refactoring TypeScript codebases"
P4 (marketplace): "TS Refactor"
P5 (inferred):    "TypeScript refactoring"
```

**CRP Decision**:
```json
{
  "field": "description",
  "resolution": "UNRESOLVED",
  "all_values": {
    "SKILL.md": "Refactor TypeScript code with AI assistance",
    "plugin.json": "TypeScript refactoring tool",
    "README.md": "An AI-powered tool for refactoring TypeScript codebases",
    "marketplace": "TS Refactor",
    "inferred": "TypeScript refactoring"
  },
  "kept_value": "Refactor TypeScript code with AI assistance",
  "note": "All 5 priority levels provide different values. Kept P1 (highest priority) but marked conflict as unresolved for audit.",
  "conflict": "unresolved"
}
```

**Rule DR-5**: If CRP cannot resolve a conflict after all 5 priority levels, keep all values in `conflict_log[]`, mark `"conflict": "unresolved"`, and use P1 value in the node. Never silently pick one value.

---

## CRP Summary for `alpha-tools/dev-kit`

```json
{
  "node_id": "alpha-tools/dev-kit/typescript-refactor",
  "crp_events": 4,
  "resolved": 3,
  "unresolved": 1,
  "requires_human_review": true,
  "confidence": "low",
  "conflict_log": [
    { "conflict_id": 1, "resolution": "KEEP_BOTH" },
    { "conflict_id": 2, "resolution": "ESCALATE", "confidence_downgrade": true },
    { "conflict_id": 3, "resolution": "SEMVER_HIGHER" },
    { "conflict_id": 4, "resolution": "UNRESOLVED" }
  ]
}
```

**Key principles demonstrated**:
1. Never silently resolve conflicts — always log the decision
2. Same-type conflicts (two SKILL.md versions) resolve by additional rules (semver)
3. Confidence is a first-class field, downgraded by conflict evidence
4. Unresolvable conflicts are valid outputs, not errors — they surface for human review
