# Example 02: Complete Bypass Cascade — All 7 Tiers + PERMANENTLY_BLOCKED

**Scenario**: A skill node's primary URL is blocked; the cascade tries all 7 bypass tiers before declaring PERMANENTLY_BLOCKED.
**Demonstrates**: Tier-by-tier bypass execution, GitHub-First decision matrix, PERMANENTLY_BLOCKED handling.

---

## Target URL

```
https://claudemarketplaces.com/skills/soultrace-ai/soul-skills/meditation-guide
```

Context: `SITE_BLOCKED=true`, `GITHUB_FIRST=true` → marketplace never tried as primary.

Primary fetch:
```http
GET https://raw.githubusercontent.com/soultrace-ai/soul-skills/main/skills/meditation-guide/SKILL.md
→ 404 Not Found
```

The skill slug was referenced in plugin.json but the SKILL.md file is missing. Cascade begins.

---

## Tier 1: Wayback Machine

```http
GET https://web.archive.org/web/*/https://claudemarketplaces.com/skills/soultrace-ai/soul-skills/meditation-guide
→ 200 OK (snapshot from 2026-03-15)
```

Wayback HTML response: JavaScript-rendered page (Next.js). HTML contains `__NEXT_DATA__` → parse:
```json
{
  "props": {
    "pageProps": {
      "skill": {
        "name": "meditation-guide",
        "description": "Guided meditation sessions...",
        "version": "0.8.0",
        "license": "MIT"
      }
    }
  }
}
```

**Partial match**: description, version, license found. `name` confirmed. Missing: `tags`, `categories`.

Tier 1 result: `PARTIAL` — continue cascade for missing fields.

---

## Tier 2: archive.ph

```http
GET https://archive.ph/https://claudemarketplaces.com/skills/soultrace-ai/soul-skills/meditation-guide
→ 404 Not Found (page never archived)
```

Tier 2 result: `MISS` — continue.

---

## Tier 3: Google Cache

```http
GET https://webcache.googleusercontent.com/search?q=cache:https://claudemarketplaces.com/skills/soultrace-ai/soul-skills/meditation-guide
→ 403 Forbidden
```

Tier 3 result: `BLOCKED` — continue.

---

## Tier 4: GitHub Raw (alternate paths)

plugin.json has `"skills": ["meditation-guide"]` confirmed from:
```http
GET https://raw.githubusercontent.com/soultrace-ai/soul-skills/main/.claude-plugin/plugin.json → 200 OK
```

But SKILL.md file itself:
```http
GET https://raw.githubusercontent.com/soultrace-ai/soul-skills/main/skills/meditation-guide/SKILL.md → 404
GET https://raw.githubusercontent.com/soultrace-ai/soul-skills/main/skills/meditation-guide/skill.md → 404
GET https://raw.githubusercontent.com/soultrace-ai/soul-skills/main/.claude/skills/meditation-guide/SKILL.md → 404
GET https://raw.githubusercontent.com/soultrace-ai/soul-skills/main/meditation-guide/SKILL.md → 404
```

GitHub Tree API check:
```http
GET https://api.github.com/repos/soultrace-ai/soul-skills/git/trees/main?recursive=1
→ Path "skills/meditation-guide/SKILL.md" NOT in tree
```

Conclusion: SKILL.md was declared in plugin.json but file does not exist in repo. Possible:
- Skill planned but not yet implemented
- File deleted after plugin.json update
- Wrong path in plugin.json

Tier 4 result: `MISS` — continue.

---

## Tier 5: CommonCrawl

```http
GET https://index.commoncrawl.org/CC-MAIN-2026-06/cdx?url=claudemarketplaces.com/skills/soultrace-ai/soul-skills/meditation-guide&output=json
→ 200 OK, body: []  (no records)
```

Tier 5 result: `MISS` — continue.

---

## Tier 6: Reference Reconstruction

Using Wayback data (Tier 1 partial) + plugin.json data + README.md:
```http
GET https://raw.githubusercontent.com/soultrace-ai/soul-skills/main/README.md → 200 OK
```

README excerpt:
```markdown
## Skills

### meditation-guide
*Guided meditation sessions tailored to your stress level.*
Tags: wellness, mindfulness, productivity
```

Tags extracted: `["wellness", "mindfulness", "productivity"]`

Reconstructed node (combining all sources):
```json
{
  "name": "meditation-guide",
  "description": "Guided meditation sessions...",
  "version": "0.8.0",
  "license": "MIT",
  "tags": ["wellness", "mindfulness", "productivity"],
  "categories": [],
  "confidence": "medium",
  "source": "wayback",
  "conflict_log": [{
    "field": "description",
    "source_a": "wayback_snapshot_2026-03-15",
    "value_a": "Guided meditation sessions...",
    "source_b": "readme",
    "value_b": "Guided meditation sessions tailored to your stress level.",
    "resolution": "kept source_a (higher priority tier)",
    "kept_value": "Guided meditation sessions..."
  }]
}
```

Tier 6 result: `PARTIAL_COMPLETE` — all required fields now resolved.

---

## Tier 7: Pattern Generation (NOT NEEDED)

Tier 7 not needed since Tier 6 resolved all required fields.

---

## Final Node

Since SKILL.md file genuinely does not exist on GitHub, node is marked:
```json
{
  "id": "soultrace-ai/soul-skills/meditation-guide",
  "status": "DONE",
  "confidence": "medium",
  "is_published": true,
  "skill_md_path": null,
  "notes": "SKILL.md missing from repo; data reconstructed from Wayback + README"
}
```

---

## PERMANENTLY_BLOCKED Scenario

If Tiers 1-7 all return MISS/BLOCKED:

```json
{
  "id": "soultrace-ai/soul-skills/ghost-skill",
  "status": "BLOCKED",
  "confidence": "low",
  "bypass_tiers_tried": [1, 2, 3, 4, 5, 6, 7],
  "bypass_results": {
    "tier_1": "MISS", "tier_2": "MISS", "tier_3": "BLOCKED",
    "tier_4": "MISS", "tier_5": "MISS", "tier_6": "MISS", "tier_7": "MISS"
  },
  "notes": "PERMANENTLY_BLOCKED: emitted to blocked_nodes.ndjson"
}
```

Node is emitted to `blocked_nodes.ndjson` and processing continues.

---

## GitHub-First Strategy Decision Matrix

```
claudemarketplaces.com accessible?
├── YES
│   ├── Primary: marketplace page scraping + __NEXT_DATA__
│   ├── Secondary: GitHub raw for SKILL.md
│   └── Bypass: Tiers 1-7 as needed
└── NO (SITE_BLOCKED=true)
    ├── Primary: GitHub raw (Tier 4 always)
    ├── Supplement: Wayback for marketplace metadata (Tier 1)
    └── Skip: Tiers 2, 3 (marketplace-dependent)
```

**Key insight**: When `GITHUB_FIRST=true`, Tier 4 (GitHub raw) becomes the PRIMARY strategy, not a fallback. The cascade still applies for alternate file paths and missing SKILL.md files.
