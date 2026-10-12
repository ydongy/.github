<!-- template: account/README.md v1 -->
# .github

Account-wide defaults for the repositories under ydongy.

## Contents

| Path | Purpose |
|---|---|
| `handbook/` | Mandatory `core/`, conditional `guides/`, language `stacks/` and repository `types/` |
| `handbook/templates/` | Templates for every kind of document, and `manifest.json` (which repository type needs which) |
| `.github/workflows/` | Reusable workflows for macOS, MyGo, websites, pipelines and document checks |
| `pull_request_template.md`, `ISSUE_TEMPLATE/` | Defaults for every repository that has none of its own |
| `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md` | Community health files GitHub applies to repositories that have none of their own |
| `labels.yml`, `scripts/sync-labels.sh` | Shared labels and the script that applies them |
| `scripts/check-docs.py` | Checks a repository's documents against the templates |
| `scripts/check-issues.py` | Checks a repository's open issues against the milestone rules |
| `profile/README.md` | Account profile |
| `LICENSE` | MIT |

## Visibility

This repository is public: GitHub applies account-wide defaults only from a public `.github` repository, and the
reusable workflows must be callable from every repository owned by ydongy. It never contains product code,
credentials or internal hostnames; examples use `<Name>` and `<domain>`.
