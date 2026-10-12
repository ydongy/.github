# .github

Account-wide defaults for the repositories under ydongy. This repository is public because GitHub applies
account defaults only from a public `.github` repository. It never contains product code, credentials or
internal hostnames.

## What is here

| Path | Purpose |
|---|---|
| `ISSUE_TEMPLATE/`, `pull_request_template.md` | Issue forms (bug, feature, documentation) and a short pull request template |
| `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md` | Community health files |
| `profile/README.md` | The account profile page |
| `STANDARD.md` | The single repository standard: open-source baseline, closed-source overlay, checklist |
| `labels.yml`, `scripts/sync-labels.sh` | The common label set and the script that applies it |
| `.github/` | CODEOWNERS, Dependabot, `pr-title.yml` and this repository's own CI |

## Community defaults

GitHub uses the issue forms, pull request template, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` and `SECURITY.md`
for every repository under the account that does not have its own copy. A repository that needs different text
adds its own file; see [STANDARD.md](STANDARD.md) for when that is appropriate.

## Standard

[STANDARD.md](STANDARD.md) describes how every repository is set up. Repositories are self-contained: they do
not call workflows or scripts from this repository.

## Labels

```bash
scripts/sync-labels.sh ydongy/<repo> [ydongy/<repo2> ...]
```

Creates or updates every label in `labels.yml` (bug, enhancement, documentation, question, good first issue,
help wanted, dependencies, duplicate, invalid, wontfix). Existing labels with the same name get the listed color
and description; other labels are left alone. Needs `gh` with repo scope and `python3`.
