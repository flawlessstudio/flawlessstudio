# Claude Skill & MCP Ecosystem — Master Reference Document

**Version**: 1.0  
**Status**: Frozen  
**Author**: flawlessstudio  
**Created**: 2026-06-18  
**Prompt Score**: 97.0/100 (815/840 — v5.0)

---

## Part 0: Executive Summary

This document is the authoritative reference for exhaustively mapping the Claude skill and MCP (Model Context Protocol) ecosystem across GitHub and claudemarketplaces.com. It covers:

- **What** to map: skills, MCPs, plugins, authors, ecosystem markers
- **How** to map it: 8-phase process (Phase -1 through Phase 7)
- **When the site is blocked**: GitHub-First strategy with 7 bypass tiers
- **Quality standards**: 10 Hard Rules, 9 Decision Rules, 8 Closure Criteria
- **Agentic patterns**: ReAct, Reflexion, Chain-of-Verification, and more
- **Output format**: 19 files, JSON Schema Draft 2020-12, streaming NDJSON

The companion file `MAPPING_PROMPT_v5.md` is the standalone executable prompt ready for use as a system prompt or task brief.

---

## Part 1: Core Concepts

### 1.1 What Is a Claude Skill?

A Claude skill is a reusable behavioral instruction set for Claude Code, stored in a GitHub repository as a `SKILL.md` file. Skills are:

- Discovered via `claudemarketplaces.com` or directly via GitHub
- Installed locally (`.claude/skills/`) or globally (`~/.claude/skills/`)
- Referenced by name in Claude Code sessions via `/skill-name`
- Packaged in plugin repos with a `.claude-plugin/plugin.json` manifest

### 1.2 What Is an MCP Server?

An MCP (Model Context Protocol) server exposes tools to Claude via a standardized protocol. MCP servers are declared in:
- `.mcp.json` (primary discovery target)
- `mcp.json` (alternate)
- `.mcprc` (alternate)

Three transport types: `stdio` (process), `http` (REST), `websocket` (real-time).

### 1.3 What Is claudemarketplaces.com?

A Next.js marketplace website that acts as a **wrapper over GitHub repos**. All substantive data (SKILL.md, plugin.json) lives on GitHub. The marketplace provides:
- Discovery/browsing interface
- Author profiles
- Plugin pages with install commands

**Critical**: As of 2026, the site returns 403 on all automated routes. Always use GitHub-First strategy.

### 1.4 The Plugin Structure

```
{author}/{plugin-repo}/
├── .claude-plugin/
│   └── plugin.json          ← manifest (primary location)
├── plugin.json              ← alternate location
├── skills/
│   ├── {skill-a}/
│   │   └── SKILL.md         ← skill definition
│   └── {skill-b}/
│       └── SKILL.md
├── .mcp.json                ← MCP server config
├── AGENTS.md                ← agent instructions (always read)
├── README.md
└── LICENSE
```

### 1.5 Multi-Ecosystem Repos

A single repo can serve 14+ AI tools simultaneously:

```
.claude-plugin/    → Claude Code
.cursor-plugin/    → Cursor IDE
.codex-plugin/     → OpenAI Codex
.kimi-plugin/      → Moonshot Kimi
.gemini-plugin/    → Google Gemini
gemini-extension.json → Google Gemini (file variant)
```

This `{ecosystem}-plugin/` naming pattern is the primary ecosystem marker.

---

## Part 2: Data Model

### 2.1 Node Schema (30 Fields)

Every skill or MCP is represented as a node. Core fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | ✓ | `{author}/{plugin_slug}/{skill_slug}` |
| `run_id` | uuid | ✓ | Crawl run identifier |
| `schema_version` | `"2.0"` | ✓ | Fixed |
| `author` | string | ✓ | GitHub login |
| `plugin_slug` | string | ✓ | Repo name |
| `skill_slug` | string | ✓ | Skills directory name |
| `name` | string | — | From SKILL.md frontmatter |
| `display_name` | string | — | Human-readable name |
| `description` | string | — | What the skill does |
| `version` | string | — | Semver preferred |
| `license` | string | — | SPDX identifier |
| `disable_model_invocation` | boolean | — | No AI invocation |
| `server_type` | enum | — | `stdio\|http\|websocket` |
| `required_env_vars` | string[] | — | Env vars needed |
| `ecosystems` | object | — | Cross-ecosystem flags |
| `completeness_score` | 0-1 | — | Field completeness |
| `confidence` | enum | — | `high\|medium\|low` |
| `status` | enum | ✓ | `PENDING\|IN_PROGRESS\|DONE\|BLOCKED\|ERROR` |
| `source` | enum | — | Where data came from |
| `fetched_at` | datetime | ✓ | ISO 8601 |

Full schema: `schemas/node.schema.json` (JSON Schema Draft 2020-12).

### 2.2 Completeness Score Formula

```
score = (filled_required / 4) × 0.7 + (filled_optional / 7) × 0.3

required fields: [name, description, license, author]
optional fields: [version, homepage, tags, categories, disable_model_invocation, server_type, required_env_vars]
```

Scores below 0.5 → `confidence: "low"`.

---

## Part 3: Agentic Framework

### 3.1 Phase Overview

| Phase | Name | Input | Output |
|-------|------|-------|--------|
| -1 | Reachability | Target URLs | SITE_BLOCKED flag |
| 0 | Seed Discovery | Marketplace or GitHub search | seeds[] |
| 1 | Manifest Discovery | seeds[] | plugin.json data |
| 2 | Skill Enumeration | plugin.json | skill slugs[] |
| 3 | Deep Parse | skill slugs | SKILL.md node data |
| 4 | Author Graph | author logins | org/user metadata |
| 5 | Cross-Reference | all nodes | validated, deduped nodes |
| 6 | MCP Catalog | .mcp.json files | MCP server nodes |
| 7 | Output Generation | all nodes | 19 output files |

### 3.2 Priority Queue

```
score = (phase_weight × 10) − (depth × 1)
```

Higher-phase nodes process first. BFS depth penalized to prevent runaway recursion.

### 3.3 Convergence

Process runs until all 8 closure criteria are simultaneously true (see §8 of `MAPPING_PROMPT_v5.md`).

**Ronda**: One complete pass over all PENDING nodes at the start of that pass. "Dry ronda" = 0 new nodes discovered. 2 consecutive dry rondas → convergence.

---

## Part 4: Guardrails

### 4.1 The 10 Hard Rules

| ID | Rule | Why It Matters |
|----|------|----------------|
| HR-01 | Never invent data | False data poisons the catalog |
| HR-02 | Never skip dedup | Duplicate nodes inflate counts |
| HR-03 | Never assume `main` branch | Many repos use `master` or custom |
| HR-04 | Never mark DONE with missing required fields | Incomplete catalog is misleading |
| HR-05 | Never conflate slug with display_name | They can legitimately differ |
| HR-06 | Never assume plugin.json path | It exists in 4 known locations |
| HR-07 | Never skip AGENTS.md | May contain undeclared skills |
| HR-08 | Never emit catalog with PENDING nodes | Incomplete run = invalid catalog |
| HR-09 | Never use marketplace as primary when GITHUB_FIRST | Site is blocked; use GitHub raw |
| HR-10 | Never process >1000 nodes without checkpoint | Resume support for large runs |

### 4.2 Confidence Levels

| Level | Meaning | Triggers |
|-------|---------|---------|
| `high` | All data directly confirmed from source | Full SKILL.md parse, no conflicts |
| `medium` | Data reconstructed from multiple sources | Bypass tier 1-3 used, no major conflict |
| `low` | Data inferred or conflicted | Unresolved CRP, missing SKILL.md, license mismatch |

---

## Part 5: Protocols

### 5.1 Conflict Resolution Protocol (CRP)

When two sources disagree on a field value:

**Priority ladder** (highest to lowest):
1. SKILL.md frontmatter
2. plugin.json
3. README.md
4. claudemarketplaces.com page
5. Inferred from structure/patterns

**Special cases**:
- `slug` vs `display_name`: not a conflict — store both fields
- Same-type conflict (two SKILL.md versions): use semver comparison for version fields
- License mismatch (frontmatter vs LICENSE file): keep P1, downgrade confidence, flag for review
- Unresolvable (5 different values at all levels): keep P1, mark `"conflict": "unresolved"`

Every CRP decision must be logged in `conflict_log[]`. Never silently resolve.

### 5.2 Branch Resolution Protocol

For each repo, resolve the default branch once and cache:
1. Try `main`
2. Try `master`
3. Try `HEAD` via `GET /repos/{owner}/{repo}` → `default_branch`
4. Cache resolved branch for all subsequent requests to that repo

### 5.3 plugin.json Discovery Protocol

Probe in order (stop at first success):
1. `.claude-plugin/plugin.json`
2. `plugin.json` (root)
3. `.claude/plugin.json`
4. GitHub Contents API: `GET /repos/{owner}/{repo}/contents/.claude-plugin/plugin.json`

If none found: continue with skills directory scan only.

---

## Part 6: Decision Rules

| # | Rule | Condition | Action |
|---|------|-----------|--------|
| DR-1 | No plugin.json → still scan | plugin.json missing from all 4 paths | Process `skills/` directory directly |
| DR-2 | No frontmatter → extract from body | SKILL.md has no `---` delimiter | Extract name from H1, description from first paragraph |
| DR-3 | Large org → topic filter | `public_repos > 100` | Search `topic:claude-skills OR topic:claude-plugin` first |
| DR-4 | Low completeness | `completeness_score < 0.5` | Set `confidence: "low"` |
| DR-5 | Unresolvable conflict | CRP finds 5 different values | Keep P1, mark `"conflict": "unresolved"` |
| DR-6 | `gemini-extension.json` | Found at repo root | Parse as JSON, not as directory marker |
| DR-6.5 | Org >100 repos | Same as DR-3 | Topic filter reduces API calls by ~99% |
| DR-7 | AGENTS.md exists | Found at any repo root | Read fully before concluding skill enumeration |
| DR-8 | MCP requires env vars | `required_env_vars` non-empty | Set `requires_config: true` in output |

---

## Part 7: Sub-Prompts

### SP-1: Skill Extractor

```
Extract all skill definitions from this SKILL.md content.
Return JSON with: name, description, version, license, author, tags, categories,
disable_model_invocation, required_env_vars, and any non-standard frontmatter fields.
If a field is missing, omit it (do not set null). If frontmatter is absent,
extract name from H1 heading and description from the first non-heading paragraph.
```

### SP-2: Conflict Resolver

```
Two sources provide different values for field "{field}" in node "{node_id}":
Source A ({priority_a}): {value_a}
Source B ({priority_b}): {value_b}

Apply the CRP priority ladder:
1. SKILL.md frontmatter > 2. plugin.json > 3. README > 4. marketplace > 5. inferred

Return: { "kept_value": ..., "resolution": "PRIORITY|SEMVER_HIGHER|KEEP_BOTH|UNRESOLVED",
          "confidence_impact": "none|downgrade", "requires_human_review": boolean }
```

### SP-3: Author Type Resolver

```
Given GitHub API response for "{author}":
{ "type": "{type}", "public_repos": {count} }

Determine:
1. Is this a User or Organization?
2. Should topic filtering be applied (repos > 100)?
3. What search queries should be used?

Return the enumeration strategy.
```

### SP-4: Ecosystem Scanner

```
Given this list of paths from GitHub Tree API for repo "{owner}/{repo}":
{paths}

Identify all ecosystem markers:
- .cursor-plugin/ → cursor_support
- .codex-plugin/ → codex_support
- .kimi-plugin/ → kimi_support
- .gemini-plugin/ → gemini_support
- gemini-extension.json → gemini_support (file)
- .mcp.json / mcp.json → has_mcp
- AGENTS.md → has_agents_md

Return ecosystems object and list of MCP config files to parse.
```

### SP-5: MCP Parser

```
Parse this MCP configuration file content ({filename}):
{content}

Extract all server definitions. For each server return:
{ name, server_type (stdio/http/websocket), command, args, url,
  env (object), required_env_vars (env keys with empty string values),
  requires_config (true if required_env_vars non-empty) }
```

---

## Part 8: Agentic Patterns

### 8.1 ReAct (Reason + Act)

At each phase boundary, the agent must explicitly state:
- **Observe**: What the current data shows
- **Reason**: What it implies for the next step
- **Act**: The exact operation to perform

Prevents silent assumption-making and makes the mapping process auditable.

### 8.2 Chain-of-Verification

After each Phase 3 parse, verify 3 key fields against a second source:
1. `license` → cross-check with LICENSE file
2. `description` → cross-check with README.md first paragraph
3. `name` → cross-check with directory path (slug)

### 8.3 Reflexion

After each ronda, compare:
- Expected new nodes (based on plugin.json skill lists)
- Actual new nodes found

If actual < 10% of expected → trigger alternate discovery:
- Expand search to all org repos
- Try alternate path patterns
- Check AGENTS.md for undeclared skills

### 8.4 Least-to-Most Decomposition

For large orgs (>100 repos):
```
1. Topic filter → candidate repos (2-10 repos typically)
2. Per-repo → plugin.json + tree scan → skill slugs
3. Per-skill → SKILL.md parse → node data
```

Never jump from "org" directly to "skill" — always intermediate steps.

### 8.5 Constitutional AI Guardrails

Before emitting any node to output:
- Check HR-01 through HR-10
- If any rule violated → reject emission, log violation, do not include in catalog

This is a hard check, not advisory.

---

## Part 9: Practical Examples

Five worked examples in the `examples/` directory:

| File | Scenario | Key Concepts |
|------|----------|-------------|
| `example_01_superpowers_full_trace.md` | Full Phase 3 trace for `obra/superpowers` | Multi-ecosystem markers, AGENTS.md |
| `example_02_bypass_cascade.md` | All 7 bypass tiers + PERMANENTLY_BLOCKED | GitHub-First decision matrix |
| `example_03_conflict_resolution.md` | 4 conflict types in `alpha-tools/dev-kit` | CRP, enum escalation, unresolvable |
| `example_04_unpublished_skills_mattpocock.md` | 10 hidden skills in `mattpocock/grill-me` | `disable-model-invocation`, lifecycle states |
| `example_05_author_graph_org_supabase.md` | Org scan of `supabase` (342 repos) | Topic filter, `.mcp.json`, MCP + skills in same repo |

---

## Part 10: Standards & References

### 10.1 JSON Schema

All output conforms to JSON Schema Draft 2020-12 (`$schema: https://json-schema.org/draft/2020-12/schema`).

Four schema files in `schemas/`:
- `node.schema.json` — single skill/MCP node
- `crawl_config.schema.json` — run parameters and coverage report
- `skills_catalog.schema.json` — published skills catalog
- `mcps_catalog.schema.json` — MCP servers with tools[]

### 10.2 SPDX License Identifiers

All `license` fields use SPDX identifiers: `MIT`, `Apache-2.0`, `GPL-3.0-only`, `BSD-3-Clause`, `agpl-3.0`, etc.
Non-SPDX values → `confidence: "low"`, flag for review.

### 10.3 Streaming NDJSON

Large output files use NDJSON (newline-delimited JSON): one JSON object per line.
Enables streaming processing without loading entire dataset into memory.

### 10.4 GitHub API Rate Limits

- Authenticated: 5,000 req/hour
- Search API: 30 req/minute
- Contents API: 1,000 req/hour (separate limit)

Mitigation: cache branch resolutions, batch tree API requests, use topic filter to reduce search volume.

### 10.5 Related Standards

- **MCP Protocol**: Model Context Protocol specification (Anthropic)
- **Claude Code Skills**: `.claude-plugin/` directory convention
- **Conventional Commits**: Used in example_01 skill
- **CommonCrawl CDX API**: Used in bypass Tier 5

---

## Appendix A: JSON Schema File References

| Schema File | `$id` |
|------------|-------|
| `node.schema.json` | `https://github.com/flawlessstudio/.github/blob/main/.claude/docs/schemas/node.schema.json` |
| `crawl_config.schema.json` | `https://github.com/flawlessstudio/.github/blob/main/.claude/docs/schemas/crawl_config.schema.json` |
| `skills_catalog.schema.json` | `https://github.com/flawlessstudio/.github/blob/main/.claude/docs/schemas/skills_catalog.schema.json` |
| `mcps_catalog.schema.json` | `https://github.com/flawlessstudio/.github/blob/main/.claude/docs/schemas/mcps_catalog.schema.json` |

---

## Appendix B: Skill Taxonomy

### Known Categories
`developer-tools`, `education`, `productivity`, `writing`, `code-review`, `testing`, `debugging`, `data`, `ai-ml`, `devops`, `security`

### Known Tags (common)
`git`, `typescript`, `python`, `refactor`, `conventional-commits`, `spaced-repetition`, `rubber-duck`, `learning`, `wellness`, `mindfulness`, `wip`, `deprecated`

---

## Appendix C: Ecosystem Marker Registry

| Marker | Type | Ecosystem | Priority |
|--------|------|-----------|---------|
| `.claude-plugin/` | directory | Claude Code | ① |
| `.cursor-plugin/` | directory | Cursor IDE | ② |
| `.codex-plugin/` | directory | OpenAI Codex | ③ |
| `.kimi-plugin/` | directory | Moonshot Kimi | ④ |
| `.gemini-plugin/` | directory | Google Gemini | ⑤ |
| `gemini-extension.json` | file | Google Gemini | ⑤ |
| `.mcp.json` | file | MCP (any) | ⑥ |
| `mcp.json` | file | MCP (any) | ⑦ |
| `.mcprc` | file | MCP (any) | ⑧ |
| `AGENTS.md` | file | Multi (read always) | — |

---

## Appendix D: SKILL.md Field Registry

| Field | Standard | Source | Notes |
|-------|----------|--------|-------|
| `name` | ✓ | frontmatter | Slug preferred |
| `description` | ✓ | frontmatter | One-line summary |
| `version` | ✓ | frontmatter | Semver preferred |
| `license` | ✓ | frontmatter | SPDX |
| `author` | ✓ | frontmatter | GitHub login |
| `homepage` | ✓ | frontmatter | URL |
| `disable-model-invocation` | extension | frontmatter | Boolean; found in mattpocock/grill-me |
| `requires_approval` | extension | frontmatter | Boolean |
| `min_claude_version` | extension | frontmatter | Semver |
| `tags` | extension | frontmatter | string[] |
| `categories` | extension | frontmatter | string[] |

---

## Appendix E: Seed Data

### Known Ecosystem Authors (starter set)

```
multica-ai      → andrej-karpathy-skills (claudemarketplaces.com)
flawlessstudio  → .github (claudemarketplaces.com)
mattpocock      → grill-me
obra            → superpowers
soultrace-ai    → soul-skills
supabase        → agent-skills, mcp-server-supabase
```

### GitHub Topics for Discovery

```
claude-skills
claude-plugin
ai-skills
claude-code-skills
mcp-server
model-context-protocol
```

### Known `.mcp.json` Patterns

```json
{ "mcpServers": { "{name}": { "command": "...", "args": [], "env": {} } } }
{ "servers": [ { "name": "...", "type": "stdio", "command": "..." } ] }
```

---

*Master Reference Document v1.0 — Frozen 2026-06-18*  
*Companion: `MAPPING_PROMPT_v5.md` (standalone executable prompt)*
