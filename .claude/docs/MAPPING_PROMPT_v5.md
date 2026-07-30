---
title: "Claude Skill/MCP Ecosystem Mapping Prompt v5.0"
version: "5.0"
status: "frozen"
author: "flawlessstudio"
created: "2026-06-18"
scoring: "97.0/100 (815/840)"
---

# Exhaustive Recursive Mapping Prompt v5.0
## Claude Skill & MCP Ecosystem — GitHub-First Edition

---

## §0 GLOBALS

```yaml
SITE_BLOCKED: false          # set true when ≥3 Phase -1 routes return 403
GITHUB_FIRST: false          # set true when SITE_BLOCKED=true
run_id: ""                   # UUID stamped at run start
schema_version: "2.0"
output_dir: "./mapping_output"
```

**Trigger**: `SITE_BLOCKED=true` → flip `GITHUB_FIRST=true`, skip all site routes, promote GitHub raw as primary.

---

## §1 OBJECTIVE

Produce a **complete, deduplicated, schema-valid map** of every Claude skill and MCP server in a target ecosystem, including:
- All published and unpublished skills
- All SKILL.md fields including non-standard extensions
- Cross-ecosystem markers (14+ AI tools)
- Author graphs (user→org→repo relationships)
- Full bypass cascade when primary source is blocked

**Convergence** is reached when all 8 closure criteria (§8.8) are simultaneously true.

---

## §2 HARD RULES

| ID | Rule |
|----|------|
| HR-01 | Never invent data. If a field cannot be confirmed, set `"confidence": "low"` and `"source": "inferred"` |
| HR-02 | Never skip deduplication. Every node gets a canonical `id = "{author}/{plugin}/{skill}"` |
| HR-03 | Never assume `main` as the default branch. Always resolve via `HEAD` or `git ls-remote` |
| HR-04 | Never mark a node DONE if any required field is missing and unresolvable |
| HR-05 | Never conflate author slug with display name without a confirmed mapping |
| HR-06 | Never assume a plugin.json path. Probe all 4 known locations (§3C.2) |
| HR-07 | Never skip AGENTS.md if present — it may contain skill declarations |
| HR-08 | Never emit catalog output while any node is PENDING or IN_PROGRESS |
| HR-09 | Never use claudemarketplaces.com as a primary source when `GITHUB_FIRST=true` |
| HR-10 | Never process more than 1000 nodes per run without emitting a checkpoint |

---

## §3 PHASE REFERENCE

### Phase -1: Reachability Assessment

**Goal**: Determine if claudemarketplaces.com is accessible.

```
Routes to test (parallel):
  GET https://claudemarketplaces.com/                           → expect 200
  GET https://claudemarketplaces.com/skills                     → expect 200
  GET https://claudemarketplaces.com/api/plugins                → expect 200
```

**Decision**:
- ≥3 routes return 403/blocked → set `SITE_BLOCKED=true`, `GITHUB_FIRST=true`
- Proceed to Phase 0

### Phase 0: Seed Discovery

**If GITHUB_FIRST=false** (site accessible):
1. Scrape `https://claudemarketplaces.com/skills` — extract `{author}/{plugin}` pairs from listing
2. Scrape `https://claudemarketplaces.com/mcps` — extract MCP entries
3. Extract `__NEXT_DATA__` JSON blob from page HTML for structured data
4. Use `buildId` from `__NEXT_DATA__` → `/_next/data/{buildId}/skills.json` for paginated API

**If GITHUB_FIRST=true** (site blocked):
1. Search GitHub: `topic:claude-skills` → collect repos
2. Search GitHub: `topic:claude-plugin` → collect repos
3. Search GitHub: `filename:.claude-plugin/plugin.json` → collect repos
4. Search GitHub: `filename:SKILL.md path:.claude` → collect repos
5. Known seed authors from HR-02 canonical list

**Output**: `seeds[]` — list of `{author, plugin_slug, source_url}`

### Phase 1: Plugin Manifest Discovery

For each seed `{author, plugin_slug}`:

**Primary** (GITHUB_FIRST=false): `https://claudemarketplaces.com/skills/{author}/{plugin_slug}`
**Primary** (GITHUB_FIRST=true): `https://raw.githubusercontent.com/{author}/{plugin_slug}/main/.claude-plugin/plugin.json`

**plugin.json probe sequence** (in order):
1. `https://raw.githubusercontent.com/{author}/{plugin_slug}/{branch}/.claude-plugin/plugin.json`
2. `https://raw.githubusercontent.com/{author}/{plugin_slug}/{branch}/plugin.json`
3. `https://raw.githubusercontent.com/{author}/{plugin_slug}/{branch}/.claude/plugin.json`
4. `https://api.github.com/repos/{author}/{plugin_slug}/contents/.claude-plugin/plugin.json`

**Branch resolution**:
- Try `main` first, then `master`, then `HEAD`
- Cache resolved branch per repo

**plugin.json fields to extract**:
```json
{
  "name": "",
  "display_name": "",
  "version": "",
  "description": "",
  "author": "",
  "license": "",
  "homepage": "",
  "repository": "",
  "skills": [],
  "mcps": [],
  "tags": [],
  "categories": []
}
```

### Phase 2: Skill Enumeration

For each plugin, enumerate all skill slugs:
1. From `plugin.json` → `skills[]` array
2. From GitHub Tree API: `GET /repos/{author}/{repo}/git/trees/{sha}?recursive=1` → filter `path` matching `skills/*/SKILL.md`
3. From directory listing fallback: probe `skills/` directory contents

For each skill slug → enqueue Phase 3 node.

### Phase 3: SKILL.md Deep Parse

#### Phase 3A: Raw Content Fetch

```
GET https://raw.githubusercontent.com/{author}/{repo}/{branch}/skills/{skill}/SKILL.md
```

On 404: try alternate paths:
- `skills/{skill}/skill.md` (lowercase)
- `.claude/skills/{skill}/SKILL.md`
- `{skill}/SKILL.md` (root level)

#### Phase 3B: Frontmatter Parse

Extract ALL YAML frontmatter fields (standard + extensions):

**Standard fields**:
```yaml
name: string
description: string
version: string
license: string       # SPDX identifier
author: string
homepage: url
```

**Known extension fields**:
```yaml
disable-model-invocation: boolean   # from mattpocock/grill-me
requires_approval: boolean
min_claude_version: string
tags: string[]
categories: string[]
```

**Enum validation**:
- `license`: validate against SPDX list; if unknown → `"confidence": "low"`
- `version`: semver preferred; accept any string

#### Phase 3C: Repository Ecosystem Scan

For the repo containing this skill, run once per unique repo:

**3C.1 — Ecosystem Markers** (check each):
```
.cursor-plugin/       → cursor_support: true
.codex-plugin/        → codex_support: true
.kimi-plugin/         → kimi_support: true
.gemini-plugin/       → gemini_support: true
gemini-extension.json → gemini_support: true  [file, not dir]
.mcp.json             → has_mcp: true
mcp.json              → has_mcp: true
.mcprc                → has_mcp: true
AGENTS.md             → read fully; may contain skill/MCP declarations
```

**3C.2 — MCP Discovery** (if `has_mcp: true`):
```
.mcp.json → parse servers[], extract name/command/server_type/required_env_vars
mcp.json  → same
```

**3C.3 — License** (if not in plugin.json):
```
LICENSE, LICENSE.md, LICENSE.txt → extract SPDX from content
```

**3C.4 — README**:
```
README.md → extract: description (first paragraph), usage examples, install instructions
```

#### Phase 3D: Conflict Resolution Protocol (CRP)

When two sources provide different values for the same field:

```
Priority (highest → lowest):
  1. SKILL.md frontmatter
  2. plugin.json
  3. README.md
  4. claudemarketplaces.com page
  5. Inferred from repo structure
```

**Name conflicts** (slug vs display_name):
- Keep both: `slug` (from path) and `display_name` (from frontmatter)
- Log conflict with `conflict_log[]` entry

**Version conflicts**:
- If semver: take higher version
- If non-semver: keep frontmatter value, log conflict

**Enum escalation**:
- If source 1 says `license: MIT` and source 2 says `license: Apache-2.0`: flag as `"confidence": "low"`, keep frontmatter, log both

### Phase 4: Author Graph Construction

For each unique `author`:

**4A — User/Org determination**:
```
GET https://api.github.com/users/{author}
→ type: "User" or "Organization"
```

**4B — Repository enumeration**:
```
If type=User:  GET /users/{author}/repos?per_page=100&type=public
If type=Org:   GET /orgs/{author}/repos?per_page=100&type=public
               If >100 repos: filter with topic first
               GET /search/repositories?q=org:{author}+topic:claude-skills
```

**4C — Cross-repo skill discovery**:
For each repo that contains `.claude-plugin/` or `skills/` → enqueue Phase 1

**4D — Author metadata**:
```json
{
  "login": "",
  "display_name": "",
  "type": "User|Organization",
  "bio": "",
  "location": "",
  "website": "",
  "repo_count": 0,
  "skill_repos": [],
  "total_skills": 0
}
```

### Phase 5: Cross-Reference & Validation

**5A — Deduplication**:
- Canonical ID: `"{author}/{plugin_slug}/{skill_slug}"`
- On collision: merge fields, keep highest-confidence values, log merge

**5B — Link validation**:
- All `homepage` URLs → HEAD request, record status
- All `repository` URLs → verify resolves to GitHub

**5C — Schema validation**:
- Validate every node against `node.schema.json`
- Flag violations as `validation_errors[]`

**5D — Completeness check**:
For each node, compute completeness score:
```
required_fields = [name, description, license, author]
optional_fields = [version, homepage, tags, categories, disable-model-invocation]
score = (filled_required / total_required) * 0.7 + (filled_optional / total_optional) * 0.3
```

### Phase 6: MCP Catalog Construction

For each MCP server discovered:

```json
{
  "id": "{author}/{repo}/{server_name}",
  "name": "",
  "description": "",
  "server_type": "stdio|http|websocket",
  "command": "",
  "args": [],
  "env": {},
  "required_env_vars": [],
  "tools": [
    {
      "name": "",
      "description": "",
      "input_schema": {}
    }
  ],
  "source_repo": "",
  "source_file": ".mcp.json"
}
```

### Phase 7: Output Generation

Emit all 19 output files (§10).

---

## §4 BYPASS TIERS

When a URL returns 403/429/503 or times out:

| Tier | Method | Use Case |
|------|--------|----------|
| 1 | Wayback Machine `https://web.archive.org/web/*/{url}` | Recent snapshots |
| 2 | archive.ph `https://archive.ph/{url}` | JavaScript-rendered pages |
| 3 | Google cache `https://webcache.googleusercontent.com/search?q=cache:{url}` | Search cache |
| 4 | GitHub raw direct `https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}` | **Primary for GITHUB_FIRST** |
| 5 | CommonCrawl index `https://index.commoncrawl.org/CC-MAIN-{latest}/cdx?url={url}` | Historical |
| 6 | Reference reconstruction | Build from known sub-parts |
| 7 | Pattern generation | Infer from adjacent confirmed nodes |

**PERMANENTLY_BLOCKED**: If all 7 tiers fail for a URL → mark node as `"status": "BLOCKED"`, emit to `blocked_nodes.ndjson`, continue.

**GitHub-First Strategy Decision Matrix**:
```
claudemarketplaces.com accessible? 
  YES → use marketplace as primary, GitHub as supplement
  NO  → use GitHub as primary (Tier 4 always available), marketplace as Tier 1-3 fallback
```

---

## §5 CONTENT HANDLERS

| Content Type | Handler |
|-------------|---------|
| `text/html` | Parse DOM, extract `__NEXT_DATA__`, scrape listing cards |
| `application/json` | Direct parse, validate against schema |
| `text/plain` (SKILL.md) | Split frontmatter `---` delimiters, parse YAML header, parse Markdown body |
| `application/json` (plugin.json) | Parse, extract skills[], mcps[], metadata |
| Binary/PDF | Skip, log as `"content_type": "unsupported"` |

**SKILL.md parse algorithm**:
```python
lines = content.split('\n')
if lines[0] == '---':
    end = lines.index('---', 1)
    frontmatter = yaml.parse('\n'.join(lines[1:end]))
    body = '\n'.join(lines[end+1:])
else:
    frontmatter = {}
    body = content
```

---

## §6 PRIORITY QUEUE

Node processing order uses score:
```
score = (phase_weight × 10) − (depth × 1)
```

Phase weights:
```
Phase -1: 10 (reachability, must run first)
Phase 0:   9 (seed discovery)
Phase 1:   8 (manifest)
Phase 2:   7 (enumeration)
Phase 3:   6 (deep parse)
Phase 4:   5 (author graph)
Phase 5:   4 (cross-reference)
Phase 6:   3 (MCP catalog)
Phase 7:   2 (output)
```

Depth = BFS depth from seed node (penalizes deep recursion).

---

## §7 EXECUTION CHECKLIST

### Pre-run
- [ ] Set `run_id` (UUID)
- [ ] Set `schema_version: "2.0"`
- [ ] Initialize output directory
- [ ] Load known seed authors

### Phase -1
- [ ] Test 3 claudemarketplaces.com routes in parallel
- [ ] Set `SITE_BLOCKED` and `GITHUB_FIRST` flags

### Phase 0
- [ ] Execute seed strategy matching `GITHUB_FIRST` flag
- [ ] Dedup seeds by canonical ID
- [ ] Enqueue all seeds into Phase 1

### Phase 1-3 (per node)
- [ ] Resolve branch (main/master/HEAD)
- [ ] Probe plugin.json at all 4 locations
- [ ] Extract all SKILL.md files
- [ ] Run CRP on all field conflicts
- [ ] Run Phase 3C ecosystem scan (once per repo)

### Phase 4 (per author)
- [ ] Determine User vs Org
- [ ] Enumerate repos (with topic filter if >100)
- [ ] Discover cross-repo skills

### Phase 5
- [ ] Dedup all nodes
- [ ] Validate all links
- [ ] Schema-validate all nodes

### Phase 6
- [ ] Catalog all MCP servers
- [ ] Extract tools[] with input_schema

### Phase 7
- [ ] Emit all 19 output files
- [ ] Verify 8 closure criteria

---

## §8 CLOSURE CRITERIA

All 8 must be simultaneously true:

1. **Queue empty**: No nodes in PENDING or IN_PROGRESS state
2. **No orphan authors**: Every `author` in any node has a Phase 4 record
3. **No unresolved conflicts**: CRP has run on every conflict
4. **Schema valid**: 0 validation errors in current run
5. **MCP complete**: Every `has_mcp: true` repo has Phase 6 record
6. **Links checked**: All `homepage` URLs have HTTP status recorded
7. **Checkpoint written**: If nodes > 1000, checkpoint file emitted
8. **Dry rounds = 2**: Last 2 consecutive rondas added 0 new nodes

**Ronda definition**: One complete pass over all PENDING nodes at the start of that pass.

---

## §9 SCHEMA SUMMARY

Four JSON Schema Draft 2020-12 files:

| File | Purpose |
|------|---------|
| `node.schema.json` | Single skill/MCP node (30 fields) |
| `crawl_config.schema.json` | Run parameters + coverage report |
| `skills_catalog.schema.json` | Published skills catalog |
| `mcps_catalog.schema.json` | MCP servers with tools[] |

Key node fields: `id`, `run_id`, `schema_version`, `author`, `plugin_slug`, `skill_slug`, `name`, `display_name`, `description`, `version`, `license`, `homepage`, `repository`, `tags`, `categories`, `disable_model_invocation`, `server_type`, `required_env_vars`, `ecosystems`, `completeness_score`, `confidence`, `status`, `validation_errors`, `conflict_log`, `source`, `fetched_at`

---

## §10 OUTPUT FILES (19 total)

| # | File | Format | Description |
|---|------|--------|-------------|
| 1 | `nodes.ndjson` | NDJSON | All nodes, streaming |
| 2 | `skills_catalog.json` | JSON | Published skills only |
| 3 | `mcps_catalog.json` | JSON | MCP servers + tools |
| 4 | `author_graph.json` | JSON | Author→repo→skill graph |
| 5 | `ecosystem_matrix.json` | JSON | Repo × ecosystem support matrix |
| 6 | `conflict_log.ndjson` | NDJSON | All CRP decisions |
| 7 | `validation_errors.json` | JSON | Schema violations |
| 8 | `blocked_nodes.ndjson` | NDJSON | Permanently blocked URLs |
| 9 | `unpublished_skills.json` | JSON | Skills found but not on marketplace |
| 10 | `coverage_report.json` | JSON | Completeness scores, stats |
| 11 | `crawl_config.json` | JSON | Run parameters |
| 12 | `phase_log.ndjson` | NDJSON | Per-phase timing + counts |
| 13 | `bypass_log.ndjson` | NDJSON | Bypass tier decisions |
| 14 | `author_index.json` | JSON | Author metadata index |
| 15 | `tag_taxonomy.json` | JSON | All tags + frequencies |
| 16 | `category_taxonomy.json` | JSON | All categories + frequencies |
| 17 | `license_distribution.json` | JSON | License breakdown |
| 18 | `checkpoint.json` | JSON | Resume state (if nodes > 1000) |
| 19 | `summary.md` | Markdown | Human-readable run summary |

---

## §11 AGENTIC PATTERNS

### ReAct (Reason + Act)
At each phase boundary: explicitly state observations, reasoning, and planned action before executing.
```
Observe: [what current state/data shows]
Reason:  [what it implies for next step]
Act:     [exact tool call or fetch]
```

### Chain-of-Verification
After each Phase 3 parse: verify 3 key fields against a second source before marking DONE.

### Reflexion
After each ronda: compare expected vs actual new nodes found. If < 10% of expected → trigger alternate discovery strategy.

### Least-to-Most Decomposition
For large orgs (>100 repos): decompose by topic filter → per-repo → per-skill.

### Constitutional AI Guardrails
Before emitting any node: check against HR-01 through HR-10. Reject emission if any rule violated.

---

## §12 DECISION RULES

| # | Rule |
|---|------|
| DR-1 | If `plugin.json` missing at all 4 locations → still process `skills/` directory if it exists |
| DR-2 | If SKILL.md has no frontmatter → extract `name` from H1, `description` from first paragraph |
| DR-3 | If author has >100 repos → use topic filter before full enumeration |
| DR-4 | If node completeness_score < 0.5 → flag as `"confidence": "low"` |
| DR-5 | If CRP cannot resolve a conflict after all 5 priority levels → keep all values, mark `"conflict": "unresolved"` |
| DR-6 | If `gemini-extension.json` found → parse as JSON, extract `name`, `description`, `tools[]` |
| DR-6.5 | If org has >100 repos → apply topic filter `topic:claude-skills OR topic:claude-plugin` first |
| DR-7 | If `AGENTS.md` found → parse for `## Skills` and `## Tools` sections before concluding skill list |
| DR-8 | If `required_env_vars` present in MCP → mark as `"requires_config": true` in output |

---

*Prompt v5.0 — Frozen 2026-06-18 — Score: 97.0/100 (815/840)*
