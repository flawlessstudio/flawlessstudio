# Agent Contracts

Completion markers and handoff schemas for all GSD agents. Workflows use these markers to detect agent completion and route accordingly.

## Agent Registry

| Agent | Role | Completion Markers |
|---|---|---|
| gsd-planner | Plan creation | `PLANNING COMPLETE` |
| gsd-executor | Plan execution | `PLAN COMPLETE`, `CHECKPOINT REACHED` |
| gsd-phase-researcher | Phase-scoped research | `RESEARCH COMPLETE`, `RESEARCH BLOCKED` |
| gsd-project-researcher | Project-wide research | `RESEARCH COMPLETE`, `RESEARCH BLOCKED` |
| gsd-plan-checker | Plan validation | `VERIFICATION PASSED`, `ISSUES FOUND` |
| gsd-research-synthesizer | Multi-research synthesis | `SYNTHESIS COMPLETE`, `SYNTHESIS BLOCKED` |
| gsd-debugger | Debug investigation | `DEBUG COMPLETE`, `ROOT CAUSE FOUND`, `CHECKPOINT REACHED` |
| gsd-roadmapper | Roadmap creation/revision | `ROADMAP CREATED`, `ROADMAP REVISED`, `ROADMAP BLOCKED` |
| gsd-ui-auditor | UI review | `UI REVIEW COMPLETE` |
| gsd-ui-checker | UI validation | `ISSUES FOUND` |
| gsd-ui-researcher | UI spec creation | `UI-SPEC COMPLETE`, `UI-SPEC BLOCKED` |
| gsd-verifier | Post-execution verification | `Verification Complete` (title case) |
| gsd-integration-checker | Cross-phase integration check | `Integration Check Complete` (title case) |
| gsd-nyquist-auditor | Sampling audit | `PARTIAL`, `ESCALATE` (non-standard) |
| gsd-security-auditor | Security audit | `OPEN_THREATS`, `ESCALATE` (non-standard) |
| gsd-codebase-mapper | Codebase analysis | No marker — writes docs directly |
| gsd-assumptions-analyzer | Assumption extraction | No marker — returns Assumptions sections |
| gsd-doc-verifier | Doc validation | No marker — writes JSON to `.planning/tmp` |
| gsd-doc-writer | Doc generation | No marker — writes docs directly |
| gsd-advisor-researcher | Advisory research | No marker — utility agent |
| gsd-user-profiler | User profiling | No marker — returns JSON in `<analysis>` tags |
| gsd-intel-updater | Codebase intelligence analysis | `INTEL UPDATE COMPLETE`, `INTEL UPDATE FAILED` |

## Marker Rules

1. ALL-CAPS markers (e.g., `PLANNING COMPLETE`) are the standard convention.
2. Title-case markers (e.g., `Verification Complete`) exist in gsd-verifier and gsd-integration-checker — intentional, not bugs.
3. Non-standard markers (e.g., `PARTIAL`, `ESCALATE`) in audit agents indicate partial results requiring orchestrator judgment.
4. Agents without markers either write artifacts directly to disk or return structured data (JSON/sections) that the caller parses.
5. Markers must appear as H2 headings at the start of a line in the agent's final output.