# Example 04: Hidden Directory Scan — Unpublished Skills in `mattpocock/grill-me`

**Scenario**: Phase 3 scan discovers 10 unpublished skills across deprecated/, in-progress/, personal/, and misc/ directories.
**Demonstrates**: Unpublished skill discovery, `disable-model-invocation` field, skill lifecycle states.

---

## Context

`mattpocock/grill-me` is listed on claudemarketplaces.com with 2 published skills.
Phase 2 GitHub Tree API scan reveals a much richer directory structure.

---

## GitHub Tree API Response

```http
GET https://api.github.com/repos/mattpocock/grill-me/git/trees/main?recursive=1
```

Relevant paths:
```
skills/quiz-me/SKILL.md                    ← published
skills/flash-cards/SKILL.md                ← published
skills/deprecated/srs-review/SKILL.md     ← UNPUBLISHED
skills/deprecated/cloze-test/SKILL.md     ← UNPUBLISHED
skills/in-progress/audio-quiz/SKILL.md    ← UNPUBLISHED
skills/in-progress/video-explain/SKILL.md ← UNPUBLISHED
skills/in-progress/debate-me/SKILL.md     ← UNPUBLISHED
skills/personal/morning-standup/SKILL.md  ← UNPUBLISHED
skills/personal/code-kata/SKILL.md        ← UNPUBLISHED
skills/personal/rubber-duck/SKILL.md      ← UNPUBLISHED
skills/misc/prompt-tester/SKILL.md        ← UNPUBLISHED
skills/misc/context-checker/SKILL.md      ← UNPUBLISHED
```

10 unpublished skills found beyond the 2 published ones.

---

## Parsing `deprecated/srs-review/SKILL.md`

```yaml
---
name: srs-review
description: Spaced repetition system review for active recall practice
version: 1.0.0
license: MIT
author: mattpocock
disable-model-invocation: true
tags: [learning, spaced-repetition, deprecated]
categories: [education]
---
```

**Notable**: `disable-model-invocation: true` — this skill disables the AI model from being invoked during execution. It runs as a pure template/script.

Node output:
```json
{
  "id": "mattpocock/grill-me/srs-review",
  "disable_model_invocation": true,
  "is_published": false,
  "skill_md_path": "skills/deprecated/srs-review/SKILL.md",
  "lifecycle_state": "deprecated",
  "confidence": "high",
  "status": "DONE"
}
```

---

## Parsing `in-progress/audio-quiz/SKILL.md`

```yaml
---
name: audio-quiz
description: Quiz generation from audio transcripts (WIP - not ready)
version: 0.1.0-alpha
license: MIT
author: mattpocock
tags: [audio, quiz, wip]
---
```

Node output:
```json
{
  "id": "mattpocock/grill-me/audio-quiz",
  "version": "0.1.0-alpha",
  "is_published": false,
  "skill_md_path": "skills/in-progress/audio-quiz/SKILL.md",
  "lifecycle_state": "in-progress",
  "confidence": "high"
}
```

---

## Parsing `personal/rubber-duck/SKILL.md`

```yaml
---
name: rubber-duck
description: Personal rubber duck debugging assistant with project memory
version: 2.3.1
license: MIT
author: mattpocock
disable-model-invocation: false
tags: [debugging, personal, productivity]
---
```

Note: `disable-model-invocation: false` (explicit false, not missing).

---

## `unpublished_skills.json` Output

```json
{
  "run_id": "...",
  "author": "mattpocock",
  "plugin_slug": "grill-me",
  "published_skills": ["quiz-me", "flash-cards"],
  "unpublished_skills": [
    {
      "slug": "srs-review",
      "path": "skills/deprecated/srs-review/SKILL.md",
      "lifecycle_state": "deprecated",
      "disable_model_invocation": true
    },
    {
      "slug": "cloze-test",
      "path": "skills/deprecated/cloze-test/SKILL.md",
      "lifecycle_state": "deprecated",
      "disable_model_invocation": false
    },
    {
      "slug": "audio-quiz",
      "path": "skills/in-progress/audio-quiz/SKILL.md",
      "lifecycle_state": "in-progress"
    },
    {
      "slug": "video-explain",
      "path": "skills/in-progress/video-explain/SKILL.md",
      "lifecycle_state": "in-progress"
    },
    {
      "slug": "debate-me",
      "path": "skills/in-progress/debate-me/SKILL.md",
      "lifecycle_state": "in-progress"
    },
    {
      "slug": "morning-standup",
      "path": "skills/personal/morning-standup/SKILL.md",
      "lifecycle_state": "personal"
    },
    {
      "slug": "code-kata",
      "path": "skills/personal/code-kata/SKILL.md",
      "lifecycle_state": "personal"
    },
    {
      "slug": "rubber-duck",
      "path": "skills/personal/rubber-duck/SKILL.md",
      "lifecycle_state": "personal"
    },
    {
      "slug": "prompt-tester",
      "path": "skills/misc/prompt-tester/SKILL.md",
      "lifecycle_state": "misc"
    },
    {
      "slug": "context-checker",
      "path": "skills/misc/context-checker/SKILL.md",
      "lifecycle_state": "misc"
    }
  ],
  "total_published": 2,
  "total_unpublished": 10,
  "total_with_disable_model_invocation": 2
}
```

---

## Key Findings

1. **`disable-model-invocation`** is a real SKILL.md frontmatter extension field (first found in `mattpocock/grill-me`). When `true`, the skill runs without invoking the AI model — it acts as a pure template processor or script runner.

2. **Lifecycle state inference**: Path prefix (`deprecated/`, `in-progress/`, `personal/`, `misc/`) is a reliable signal for lifecycle state, even though it's not a formal SKILL.md field.

3. **5x discovery multiplier**: GitHub Tree API found 5x more skills (12) than the marketplace showed (2). Always run the tree scan.

4. **HR-07 applies**: Even deprecated/in-progress skills should be processed and included in `unpublished_skills.json` — they represent real authored content.
