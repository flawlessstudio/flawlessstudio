# Workflows

> GitHub Actions workflows for the Flawless Studio ecosystem hub.

## Active workflows

| Workflow | Trigger | Purpose |
|---|---|---|
| [`validate-markdown.yml`](./validate-markdown.yml) | push / PR → main (`.md` files) | Lint all Markdown files with `markdownlint` |
| [`validate-bilingual-parity.yml`](./validate-bilingual-parity.yml) | push / PR → main (canonical files) | Verify every EN canonical file has its `.es.md` pair |
| [`validate-yaml.yml`](./validate-yaml.yml) | push / PR → main (`registries/**.yaml`) | Lint all registry YAML files |
| [`audit-report.yml`](./audit-report.yml) | cron (1st of month) / manual dispatch | Create GitHub issue as monthly audit reminder |

## Design principles

- Workflows run only on file types they are responsible for (path filters).
- No workflow builds, deploys, or installs dependencies beyond its specific tool.
- Failures are reported as GitHub annotations (`::error`) for inline visibility.
- The audit workflow requires `issues: write` permission and no other elevated access.

---

*Governed by [`GOVERNANCE.md`](../GOVERNANCE.md).*
