---
name: sfs-agent-type-designer
version: 3.1.2
type: agent
namespace: sfs-agent-
description: Typographic design, accessibility review, font pairing, branding support, and implementation guidance for Claude Code workflows.
triggers:
  - typography
  - font pairing
  - type system
  - accessibility WCAG type contrast
  - brand type guidelines
  - typeface selection
  - implementation of type tokens
license: Closed
package: Flawless Studio
---

# sfs-agent-type-designer

Closed product package for Claude Code typographic design workflows.

## Capabilities

- Typeface selection and pairing aligned with brand voice
- Type-scale and rhythm systems (modular scale, baseline grids)
- WCAG-compliant type contrast and accessibility review
- Font licensing and delivery (web, print, app)
- Implementation guidance (CSS/Tailwind tokens, design-system handoff)
- Brand typography documentation

## Operational assets

- `.claude-plugin/plugin.json` — plugin descriptor
- `agents/type-designer.md` — agent prompt
- `skills/type-design/SKILL.md` — bundled skill
- `hooks/hooks.json` — Claude Code hooks
- `mcp/mcp.json` — MCP server configuration
- `docs/CLAUDE.md` — operating context
- `debug/config.md` — debug configuration
- `troubleshooting/errors.md` — known issues
- `release/LAUNCH_CHECKLIST.md` — release gate
- `release/RELEASE_NOTES.md` — version history
- `release/LICENSE.md` — license

## Installation

1. Unzip the package.
2. Copy plugin and project files to the correct Claude Code locations.
3. Merge `hooks/hooks.json`.
4. Register `mcp/mcp.json`.
5. Validate with `doctor`, `status`, `hooks`, `mcp`.
6. Test with a short type brief.

## Suite contract

Component of Some Flawless Skills v3.1.2. Naming: `sfs-agent-` namespace. Brand: INUI design system, teal `#14B8A6`, grafito `#0F172A`.