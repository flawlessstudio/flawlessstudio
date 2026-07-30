# Example 01: Full Phase 3 Execution Trace — `obra/superpowers`

**Scenario**: Map all skills in the `obra/superpowers` GitHub repository.
**Demonstrates**: Complete Phase 3 walkthrough, multi-ecosystem discovery, AGENTS.md processing.

---

## Step 0: Phase -1 Reachability

```http
GET https://claudemarketplaces.com/       → 403 Forbidden
GET https://claudemarketplaces.com/skills → 403 Forbidden
GET https://claudemarketplaces.com/api/plugins → 403 Forbidden
```

**Decision**: 3/3 routes blocked → `SITE_BLOCKED=true`, `GITHUB_FIRST=true`

---

## Step 1: Phase 0 Seed Discovery (GitHub-First)

```
GitHub search: topic:claude-skills
→ resultado: obra/superpowers (among others)
```

Seed enqueued:
```json
{ "author": "obra", "plugin_slug": "superpowers", "source_url": "https://github.com/obra/superpowers" }
```

---

## Step 2: Phase 1 — Plugin Manifest Discovery

Branch resolution:
```http
GET https://api.github.com/repos/obra/superpowers → default_branch: "main"
```

plugin.json probe sequence:
```http
1. GET https://raw.githubusercontent.com/obra/superpowers/main/.claude-plugin/plugin.json → 200 OK
```

plugin.json content:
```json
{
  "name": "superpowers",
  "display_name": "Superpowers",
  "version": "1.0.0",
  "description": "A collection of superpowers for Claude",
  "author": "obra",
  "license": "MIT",
  "skills": [
    "git-commit",
    "code-review",
    "refactor",
    "test-writer",
    "debugger"
  ]
}
```

---

## Step 3: Phase 2 — Skill Enumeration

From plugin.json `skills[]`: 5 skill slugs extracted.

GitHub Tree API cross-check:
```http
GET https://api.github.com/repos/obra/superpowers/git/trees/main?recursive=1
```

Matching paths found:
```
skills/git-commit/SKILL.md
skills/code-review/SKILL.md
skills/refactor/SKILL.md
skills/test-writer/SKILL.md
skills/debugger/SKILL.md
```

5 Phase 3 nodes enqueued. No discrepancy.

---

## Step 4: Phase 3A — Raw Content Fetch

Fetching `skills/git-commit/SKILL.md`:
```http
GET https://raw.githubusercontent.com/obra/superpowers/main/skills/git-commit/SKILL.md → 200 OK
```

Raw content:
```
---
name: git-commit
description: Generate conventional commit messages from staged changes
version: 1.2.0
license: MIT
author: obra
tags: [git, commits, conventional-commits]
categories: [developer-tools]
---

## Git Commit Message Generator

Analyzes your staged changes and generates a conventional commit message...
```

---

## Step 5: Phase 3B — Frontmatter Parse

Extracted fields:
```json
{
  "name": "git-commit",
  "description": "Generate conventional commit messages from staged changes",
  "version": "1.2.0",
  "license": "MIT",
  "author": "obra",
  "tags": ["git", "commits", "conventional-commits"],
  "categories": ["developer-tools"],
  "disable_model_invocation": false
}
```

Validation: all standard fields present. License `MIT` → valid SPDX. `confidence: "high"`.

---

## Step 6: Phase 3C — Ecosystem Scan (once per repo)

Directory structure probe:
```
.cursor-plugin/   → EXISTS → cursor_support: true
.codex-plugin/    → EXISTS → codex_support: true  
.kimi-plugin/     → EXISTS → kimi_support: true
.claude-plugin/   → EXISTS (already found)
gemini-extension.json → NOT FOUND
.mcp.json         → NOT FOUND
AGENTS.md         → EXISTS → READ FULLY
```

**AGENTS.md content** (relevant excerpt):
```markdown
# Agent Instructions

## Skills
The following skills are available for use with AI coding assistants:
- git-commit: for staged change commit message generation
- code-review: for pull request review assistance
```

No new skill declarations beyond plugin.json list. AGENTS.md processed ✓.

**ecosystems result**:
```json
{
  "cursor": true,
  "codex": true,
  "kimi": true,
  "claude": true,
  "gemini": false
}
```

---

## Step 7: CRP Check

No conflicts found between plugin.json and SKILL.md frontmatter for `git-commit`.
All 5 skills processed. No CRP events triggered.

---

## Step 8: Phase 4 — Author Graph

```http
GET https://api.github.com/users/obra
→ { "type": "User", "login": "obra", "name": "Jesse Vincent", "public_repos": 47 }
```

47 repos < 100 → enumerate all:
```http
GET https://api.github.com/users/obra/repos?per_page=100&type=public
```

Cross-repo skill check: 2 additional repos with `skills/` directory found → enqueued.

---

## Step 9: Final Node Output

```json
{
  "id": "obra/superpowers/git-commit",
  "run_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "schema_version": "2.0",
  "author": "obra",
  "plugin_slug": "superpowers",
  "skill_slug": "git-commit",
  "name": "git-commit",
  "description": "Generate conventional commit messages from staged changes",
  "version": "1.2.0",
  "license": "MIT",
  "tags": ["git", "commits", "conventional-commits"],
  "categories": ["developer-tools"],
  "ecosystems": { "cursor": true, "codex": true, "kimi": true, "claude": true, "gemini": false },
  "completeness_score": 0.95,
  "confidence": "high",
  "status": "DONE",
  "source": "github_raw",
  "branch": "main",
  "skill_md_path": "skills/git-commit/SKILL.md",
  "is_published": false,
  "fetched_at": "2026-06-18T04:00:00Z"
}
```

---

**Key takeaways**:
- `GITHUB_FIRST=true` means marketplace is never called; GitHub raw is sufficient
- Multi-ecosystem markers (`.cursor-plugin/`, `.codex-plugin/`, `.kimi-plugin/`) found in same repo
- AGENTS.md must always be read but may add no new data
- Author graph expansion from 47 repos found 2 additional skill repos
