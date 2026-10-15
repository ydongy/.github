# AGENTS.md

## What it is

The account defaults repository of ydongy: community health files, issue and pull request templates, the
account profile, the shared label set and `STANDARD.md`, the repository standard. It has no product code.

## Layout

```
STANDARD.md            the repository standard (single source of truth)
pull_request_template.md  the PR template
profile/README.md      account profile
labels.yml             common labels; scripts/sync-labels.sh applies them
.github/               ISSUE_TEMPLATE/ (issue forms; GitHub reads account defaults only from here),
                       CODEOWNERS, dependabot.yml, workflows (ci.yml, pr-title.yml)
```

## Commands

```bash
actionlint .github/workflows/*.yml     # lint workflows
scripts/sync-labels.sh <owner/repo>    # apply labels.yml (needs gh)
```

## Conventions

- English. Conventional Commits for commits and PR titles: `feat|fix|docs|refactor|perf|test|build|ci|chore|revert(scope)!: subject`.
- Branches are named `<type>/<issue>-<slug>`; pull requests are squash-merged by the maintainer.
- A rule change goes into `STANDARD.md` only; do not duplicate rules in other files.
- Keep the community files short and written for outside contributors.

## Red lines

- This repository is public: no credentials, no internal hostnames, no product code.
- Do not change repository settings or push without the maintainer's confirmation.
