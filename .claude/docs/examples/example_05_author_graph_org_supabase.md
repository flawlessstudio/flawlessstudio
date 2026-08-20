# Example 05: Author Graph Construction — Org vs User, Topic Filter for `supabase`

**Scenario**: Phase 4 author graph for the `supabase` GitHub organization, which has 340+ repos.
**Demonstrates**: Org vs User determination, topic filter (DR-6.5), `.mcp.json` discovery, multi-ecosystem markers.

---

## Phase 4A: User vs Org Determination

```http
GET https://api.github.com/users/supabase
```

Response:
```json
{
  "login": "supabase",
  "type": "Organization",
  "name": "Supabase",
  "description": "The open source Firebase alternative.",
  "public_repos": 342,
  "location": "San Francisco, CA",
  "blog": "https://supabase.com"
}
```

**Decision**: `type=Organization`, `public_repos=342` → **apply topic filter per DR-6.5** (>100 repos).

---

## Phase 4B: Topic-Filtered Repo Enumeration

Standard enumeration (skipped — too many repos):
```
# NOT EXECUTED:
GET /orgs/supabase/repos?per_page=100  → would return 100 of 342, need 4 pages
```

Topic-filtered search (DR-6.5):
```http
GET https://api.github.com/search/repositories?q=org:supabase+topic:claude-skills&per_page=30
→ 0 results

GET https://api.github.com/search/repositories?q=org:supabase+topic:claude-plugin&per_page=30
→ 0 results

GET https://api.github.com/search/repositories?q=org:supabase+topic:ai-skills&per_page=30
→ 1 result: supabase/agent-skills

GET https://api.github.com/search/repositories?q=org:supabase+topic:mcp&per_page=30
→ 1 result: supabase/mcp-server-supabase
```

2 relevant repos found from 342 total. **Topic filter reduced scope by 99.4%**.

---

## Phase 3C Scan: `supabase/agent-skills`

Directory structure:
```
.claude-plugin/plugin.json    → EXISTS
skills/                       → EXISTS (multiple skills)
.mcp.json                     → EXISTS ← MCP SERVER FOUND
AGENTS.md                     → EXISTS
README.md                     → EXISTS
```

**plugin.json**:
```json
{
  "name": "agent-skills",
  "display_name": "Supabase Agent Skills",
  "version": "1.0.0",
  "author": "supabase",
  "license": "Apache-2.0",
  "skills": [
    "query-builder",
    "schema-designer",
    "row-level-security",
    "edge-function-writer",
    "migration-helper"
  ],
  "mcps": ["supabase-local"]
}
```

**`.mcp.json`** (priority ③ in discovery sequence):
```json
{
  "mcpServers": {
    "supabase-local": {
      "command": "npx",
      "args": ["@supabase/mcp-server", "--project-ref", "${SUPABASE_PROJECT_REF}"],
      "env": {
        "SUPABASE_ACCESS_TOKEN": "${SUPABASE_ACCESS_TOKEN}"
      }
    }
  }
}
```

MCP server node created:
```json
{
  "id": "supabase/agent-skills/supabase-local",
  "name": "supabase-local",
  "server_type": "stdio",
  "command": "npx",
  "args": ["@supabase/mcp-server", "--project-ref", "${SUPABASE_PROJECT_REF}"],
  "required_env_vars": ["SUPABASE_ACCESS_TOKEN", "SUPABASE_PROJECT_REF"],
  "requires_config": true,
  "source_file": ".mcp.json"
}
```

**AGENTS.md** excerpt:
```markdown
# Supabase Agent Skills

These skills are designed for AI coding assistants working with Supabase projects.

## Prerequisites
- Active Supabase project
- Supabase CLI installed
- Environment: SUPABASE_ACCESS_TOKEN, SUPABASE_PROJECT_REF

## Skills Overview
- query-builder: Generate type-safe Supabase queries
- schema-designer: Design database schemas with RLS in mind
```

No additional skills beyond plugin.json list. AGENTS.md processed ✓.

---

## Phase 3C Scan: `supabase/mcp-server-supabase`

Separate repo dedicated to MCP:
```
.mcp.json    → EXISTS
README.md    → EXISTS
package.json → EXISTS
```

This repo is a pure MCP server — no SKILL.md files.

**`.mcp.json`**:
```json
{
  "mcpServers": {
    "supabase": {
      "command": "npx",
      "args": ["-y", "@supabase/mcp-server-supabase@latest"],
      "env": {
        "SUPABASE_ACCESS_TOKEN": ""
      }
    }
  }
}
```

MCP node:
```json
{
  "id": "supabase/mcp-server-supabase/supabase",
  "name": "supabase",
  "server_type": "stdio",
  "command": "npx",
  "args": ["-y", "@supabase/mcp-server-supabase@latest"],
  "required_env_vars": ["SUPABASE_ACCESS_TOKEN"],
  "requires_config": true,
  "source_repo": "supabase/mcp-server-supabase",
  "source_file": ".mcp.json"
}
```

---

## Author Graph Output

```json
{
  "author": {
    "login": "supabase",
    "display_name": "Supabase",
    "type": "Organization",
    "bio": "The open source Firebase alternative.",
    "website": "https://supabase.com",
    "repo_count": 342,
    "topic_filter_applied": true,
    "skill_repos": ["agent-skills"],
    "mcp_repos": ["agent-skills", "mcp-server-supabase"],
    "total_skills": 5,
    "total_mcps": 2
  },
  "repos": [
    {
      "name": "agent-skills",
      "skills": ["query-builder", "schema-designer", "row-level-security", "edge-function-writer", "migration-helper"],
      "mcps": ["supabase-local"],
      "has_agents_md": true,
      "license": "Apache-2.0"
    },
    {
      "name": "mcp-server-supabase",
      "skills": [],
      "mcps": ["supabase"],
      "has_agents_md": false,
      "license": "Apache-2.0"
    }
  ]
}
```

---

## Key Findings

1. **Topic filter is essential for large orgs**: 342 repos → 2 relevant. Without DR-6.5, we'd waste 4 API pages and risk rate limiting.

2. **`.mcp.json` discovery**: `supabase/agent-skills` has BOTH skills (`.claude-plugin/plugin.json`) AND MCP config (`.mcp.json`) in the same repo. This is the multi-capability repo pattern.

3. **Separate MCP repos**: `supabase/mcp-server-supabase` is a dedicated MCP repo with no SKILL.md — still valid and should be included in `mcps_catalog.json`.

4. **`required_env_vars` → `requires_config: true`**: Both Supabase MCPs require credentials. The `requires_config` flag in the catalog helps users filter for install-ready vs configure-required servers.

5. **AGENTS.md confirms prerequisites**: The `supabase/agent-skills` AGENTS.md documents environment requirements that match the `.mcp.json` env vars. Cross-reference confirms data accuracy.
