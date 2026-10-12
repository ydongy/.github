<!-- template: account/README.md v1 -->
# .github

Account-wide defaults for the repositories under ydongy. This repository has two layers.

1. **Community defaults and profile (all repositories).** Issue templates (bug, feature, documentation), the pull
   request template, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md` and the account `profile/`. GitHub
   applies them to every repository that has none of its own. They are written for open source.
2. **Closed-product process (loggia, barekeep and similar only).** The handbook (`handbook/core/` and the
   type, stack and template material), `scripts/check-docs.py`, `scripts/check-issues.py` and the reusable
   workflows. Product-only issue and pull request templates live in `handbook/templates/product/`; a closed
   product copies what it needs into its own `.github/`.

Open-source repositories do not use layer 2. They follow [handbook/oss.md](handbook/oss.md) and stay
self-contained.

## Contents

| Path | Purpose |
|---|---|
| `handbook/oss.md` | Standard for every open-source repository |
| `handbook/` | Closed-product process: mandatory `core/`, conditional `guides/`, language `stacks/` and repository `types/` |
| `handbook/templates/` | Templates for every kind of document, and `manifest.json` (which repository type needs which) |
| `.github/workflows/` | Reusable workflows for closed products (macOS, MyGo, websites, pipelines, document checks), plus this repository's own CI |
| `pull_request_template.md`, `ISSUE_TEMPLATE/` | Generic defaults for every repository that has none of its own |
| `handbook/templates/product/` | Product-only issue templates (task, decision) and the product pull request template |
| `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md` | Community health files GitHub applies to repositories that have none of their own |
| `labels.yml`, `scripts/sync-labels.sh` | `common` and `product` label groups; the script applies `common` by default and `product` with `--product` |
| `scripts/check-docs.py` | Closed products: checks a repository's documents against the templates |
| `scripts/check-issues.py` | Closed products: checks a repository's open issues against the milestone rules |
| `profile/README.md` | Account profile |
| `LICENSE` | MIT |

## Visibility

This repository is public: GitHub applies account-wide defaults only from a public `.github` repository, and the
reusable workflows must be callable from the closed product repositories. It never contains product code,
credentials or internal hostnames; examples use `<Name>` and `<domain>`.
