<div align="center">

# .github

Account-wide community defaults, profile and repository standard for ydongy.

[![CI](https://github.com/ydongy/.github/actions/workflows/ci.yml/badge.svg)](https://github.com/ydongy/.github/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**English** · [简体中文](README.zh-CN.md)

</div>

This repository is public because GitHub applies account defaults only from a public `.github` repository. It
never contains product code, credentials or internal hostnames.

## Features

- Community health files (`CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`) that apply to every repository without its own copy.
- Issue forms (bug, feature, documentation) and a short pull request template.
- The account profile page in `profile/README.md`.
- [STANDARD.md](STANDARD.md): the single repository standard, with a checklist.
- A common label set (`labels.yml`) and `scripts/sync-labels.sh` to apply it.

## Requirements

For the label script only: `gh` (authenticated, with repo scope), `python3` and bash.

## Quick start

Nothing to install. GitHub picks up the defaults automatically. To apply the common labels to a repository:

```bash
scripts/sync-labels.sh ydongy/<repo>
```

## Usage

| Path | Purpose |
|---|---|
| `.github/ISSUE_TEMPLATE/`, `pull_request_template.md` | Issue forms and the pull request template |
| `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md` | Community health files |
| `profile/README.md` | The account profile page (bilingual; GitHub renders only this file) |
| `STANDARD.md` | Open-source baseline, closed-source overlay, checklist |
| `labels.yml`, `scripts/sync-labels.sh` | The common label set and the script that applies it |
| `.github/` | CODEOWNERS, Dependabot, `pr-title.yml` and this repository's own CI |

**Community defaults.** GitHub uses the issue forms, pull request template, `CONTRIBUTING.md`,
`CODE_OF_CONDUCT.md` and `SECURITY.md` for every repository under the account that does not have its own copy.
A repository that needs different text adds its own file; [STANDARD.md](STANDARD.md) says when that is
appropriate. Repositories are self-contained: they do not call workflows or scripts from this repository.

**Labels.**

```bash
scripts/sync-labels.sh ydongy/<repo> [ydongy/<repo2> ...]
```

Creates or updates every label in `labels.yml` (bug, enhancement, documentation, question, good first issue,
help wanted, dependencies, duplicate, invalid, wontfix). Existing labels with the same name get the listed color
and description; other labels are left alone.

## Development

CI (`.github/workflows/ci.yml`) runs actionlint, parses the YAML files and `labels.yml`, and checks the shell
syntax of the script. Locally:

```bash
bash -n scripts/sync-labels.sh
actionlint
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Commit messages and pull request titles follow
[Conventional Commits](https://www.conventionalcommits.org/).

## Security

Report vulnerabilities privately through GitHub Security, "Report a vulnerability", on the affected repository.
See [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE), copyright (c) 2026 ydongy.
