# Repository standard

The single source of truth for how repositories owned by ydongy are set up. Every repository follows
[Part 1](#part-1-all-repositories). Closed-source products additionally follow
[Part 2](#part-2-closed-source-products).

Repositories are self-contained: they do not call reusable workflows, scripts or pinned revisions from
`ydongy/.github`. They only inherit its community health files and templates through GitHub's account defaults.

## Contents

- [Part 1: All repositories](#part-1-all-repositories)
  - [Root files](#root-files)
  - [.github/](#github)
  - [docs/](#docs)
  - [Labels](#labels)
  - [Releases](#releases)
- [Part 2: Closed-source products](#part-2-closed-source-products)
- [Repository checklist](#repository-checklist)
- [Starting a new project](#starting-a-new-project)

## Part 1: All repositories

### Root files

- `README.md` and `README.zh-CN.md`: English (default) and Simplified Chinese, same structure and same facts.
  Both open with a centered block: `# Name`, a one-line description, badges (CI using the repository's real
  workflow file, License MIT; extra badges only when real: latest release for release-please repositories,
  platform, website) and a language switch line (`**English** · [简体中文](README.zh-CN.md)`, mirrored in the
  Chinese file). Closed products use a `license-proprietary-lightgrey` badge and a Website badge, and no CI
  badge. Sections in this order, omitting one only if it does not apply: Features, Requirements, Quick start,
  Usage, Development (exact commands), Contributing (link), Security, License; Acknowledgements may precede
  License. Every command must be verified against the repository's scripts.
- `LICENSE`: MIT, `Copyright (c) 2026 ydongy` (closed products: see Part 2).
- `CHANGELOG.md`: Keep a Changelog style with an `## [Unreleased]` section. Repositories that use release-please
  let it write the entries. Do not keep `CHANGELOG.zh.md` unless a website consumes it.
- `CONTRIBUTING.md`: per repository, short, English. It states: open an issue before large changes; development
  setup; the exact test and lint commands; Conventional Commits for commit messages and pull request titles
  (`feat|fix|docs|refactor|perf|test|build|ci|chore|revert(scope)!: subject`); branches named
  `<type>/<issue>-<slug>`; squash merge by a maintainer; no DCO or sign-off. A repository without its own file
  inherits the account default.
- `CODE_OF_CONDUCT.md` and `SECURITY.md`: not per repository; inherited from `ydongy/.github`. A repository may
  keep its own `SECURITY.md` only if it has repository-specific scope; reporting must then go through
  `https://github.com/ydongy/<repo>/security/advisories/new` (no e-mail).
- `AGENTS.md`: a self-contained agent guide (layout, commands, conventions, Conventional Commits). It does not
  reference `ydongy/.github`, milestones, tracking issues, sign-off or pinned SHAs.
- `CLAUDE.md`: one line, `@AGENTS.md`. No `GEMINI.md` and no `.github/copilot-instructions.md`.
- `.editorconfig`: utf-8, lf, final newline, trimmed trailing whitespace; 2 spaces by default, tabs for Go and
  Makefiles, 4 spaces for Python and Swift.

### .github/

- `CODEOWNERS`: `* @ydongy`
- `dependabot.yml`: `github-actions` monthly, plus the repository's own ecosystem (gomod, pip, npm, swift)
  weekly when present.
- `workflows/ci.yml`: self-contained; runs on `pull_request` and on push to `main`;
  `permissions: contents: read`; concurrency with cancel-in-progress for pull requests; actions pinned to major
  tags (for example `actions/checkout@v5`).
- `workflows/pr-title.yml`: `pull_request_target` with types `opened`, `edited`, `synchronize`, `reopened`;
  `permissions: pull-requests: read`; no checkout; the title (`${{ github.event.pull_request.title }}`) is passed
  through an environment variable and validated against the Conventional Commits pattern in bash; skipped for
  `dependabot[bot]`.
- Issue and pull request templates: none per repository; they are inherited from `ydongy/.github`
  (bug, feature, documentation; a short pull request template). Blank issues are disabled there.
- Not present: any `uses: ydongy/.github/...` caller, document-check configuration, repository-type markers or
  template version markers in documents.

### docs/

Keep only documents that describe the project to its users and contributors: architecture, ADRs, design notes.
Do not keep internal process material (milestones, process, roadmaps with internal dependencies), template
version markers (HTML comments naming a template and version), or links into private repositories. Remove `.claude/` and
`.codex/` directories unless they are part of what the project offers (for example a template that ships agent
configuration on purpose); in that case say so in the README. Closed products keep more; see Part 2.

### Labels

`scripts/sync-labels.sh <owner/repo>` in `ydongy/.github` applies the labels in `labels.yml` (bug, enhancement,
documentation, question, good first issue, help wanted, dependencies, duplicate, invalid, wontfix). Per-repository
scope labels are never created or removed by the sync.

### Releases

- Repositories with releases use release-please (`googleapis/release-please-action@v4`, release type `simple`,
  `release-please-config.json` and `.release-please-manifest.json`, a `VERSION` file when useful). Tags are
  `vX.Y.Z`. The workflow has `contents: write` and `pull-requests: write` and uses `GITHUB_TOKEN`.
- Other repositories (templates, websites, tooling) have no release automation; `CHANGELOG.md` `[Unreleased]` is
  maintained by hand.

## Part 2: Closed-source products

A closed product repository (currently `loggia` and `barekeep`) follows everything in Part 1 (root files,
self-contained `AGENTS.md`, one-line `CLAUDE.md`, CODEOWNERS, Dependabot, `pr-title.yml`, Conventional Commits,
branch naming, squash merge) plus the rules below. The repository stays private.

### License

`LICENSE` is proprietary: the terms-of-service text, with the first line `Copyright (c) 2026 ydongy. All rights
reserved.` and no template marker.

### Release pipeline

The release pipeline is kept in the repository and is self-contained: `scripts/release.sh`, `bump.sh`,
`check-release.sh`, `verify-published.sh`, `release-credentials.sh`, `scan_secrets.py`, `Config/release.conf`, a
release workflow (if any) and the `release` environment secrets. Do not change release workflow triggers,
`Config/Version.xcconfig` or the changelog heading format `## [X.Y.Z] - YYYY-MM-DD` / `## [Unreleased]`: the
release scripts and the website changelog tool parse them. No release-please.

The `release` environment needs a deployment branch policy that allows only `main`.

### Changelog

`CHANGELOG.md` and `CHANGELOG.zh.md` both stay. The Chinese file feeds the product website's changelog page via
`scripts/website-changelog.py`. Both files carry the same bullets; `CONTRIBUTING.md` explains this.

### CONTRIBUTING.md

Written for a future contributor and a future open-sourcing: setup; build and test commands; Conventional Commits
with the repository's scopes; branch naming; squash merge; changelog rules (English and Chinese, same bullets);
release = merging a version bump made with `scripts/bump.sh`; UI changes start from a mockup.

### docs/

Product documents stay in `docs/`: `spec.md`, `design.md`, `legal.md`, `website.md`, `adr/` and `releasing.md`
(release steps, secrets table, what to do when a release is wrong).

- There is no `docs/process.md`: scopes, CI and branch rules live in `CONTRIBUTING.md`, agent rules in
  `AGENTS.md`, release content in `docs/releasing.md`.
- An ADR that only says to follow a shared document layout gets a short note that it is superseded by the
  repository's self-contained conventions; the file is kept.
- Security review records live in `docs/security/<version>-review.md`. There is no `docs/milestones/`; useful
  history is folded into the changelog or the roadmap. `docs/roadmap.md` may stay as a plain list without
  milestone or tracking-issue rules.

### Issues and labels

No milestone, tracking-issue or `Later` rules, and no issue-checking script. Labels are the common set, plus
product labels where useful. Issue and pull request templates are inherited from `ydongy/.github`; do not add
task or decision forms.

### Design

Keep `design/screens/*.html` mockups, tokens, icon sources and their scripts (`check-tokens.py`,
`export-icons.mjs`, `icon.html`, `*-icon.js`, `icon-layers`). `design/README.md` is a short self-contained
description: what is there, how to preview it, how to regenerate icons. No status ledger, status words, A/B
tiers, sign-off states or screenshot checks. `AGENTS.md` keeps one design rule: "A UI change starts from the
mockup in design/screens/; the maintainer confirms the visual direction before UI code is written." Screenshots
in `design/screenshots` may stay as assets.

### Agent configuration

`.claude/` and `.codex/` stay tracked. `AGENTS.md` keeps these red lines: credentials never go into pull
requests, issues, logs or chat; signing, releases and anything sent to an external service need the maintainer's
confirmation; merging a version bump publishes a release; no blind `git add -A` of unknown files.
Project-specific rules (UI states, string conventions, the security walkthrough requirement and similar) stay
in `AGENTS.md` and do not cite paths outside the repository.

### CI cost

Private repositories pay a multiplier for hosted macOS minutes, so CI is split by cost and is self-contained
(either one `ci.yml` or a separate cheap-checks workflow; say which in `CONTRIBUTING.md`):

- A Linux job runs on every pull request and push: shell and Python syntax, script tests, secret scanning,
  changelog tooling tests, and anything else cheap that already exists.
- A macOS build and test job runs only on manual dispatch (`workflow_dispatch`) and on pull requests that touch
  `Config/Version.xcconfig` (release pull requests). It uses a hosted runner (no self-hosted labels), selects the
  Xcode version the project requires with `sudo xcode-select -s /Applications/Xcode_<version>.app`, and fails
  with an error when that Xcode is not installed. Test runs set `TEST_RUNNER_COMPAT_RUN=1` as the macOS template
  does.

## Repository checklist

Check each item when creating a repository.

- [ ] Name, one-line description and topics set; visibility chosen (open source: public; closed product: private)
- [ ] `LICENSE` matches the visibility (MIT or proprietary)
- [ ] `README.md` and `README.zh-CN.md` have the required sections, badges and language switch line
- [ ] `CONTRIBUTING.md` lists the exact test and lint commands (open source may inherit the default)
- [ ] `AGENTS.md` is self-contained; `CLAUDE.md` is the single line `@AGENTS.md`; no `GEMINI.md`, no
      `.github/copilot-instructions.md`
- [ ] `CHANGELOG.md` has `## [Unreleased]` (closed products: plus `CHANGELOG.zh.md`)
- [ ] `.editorconfig` present
- [ ] `.github/CODEOWNERS` is `* @ydongy`
- [ ] `.github/dependabot.yml`: github-actions monthly plus the repository's ecosystem weekly
- [ ] `.github/workflows/ci.yml` is self-contained, with `contents: read` and actions pinned to major tags
- [ ] `.github/workflows/pr-title.yml` present
- [ ] No per-repository issue or pull request templates, no `CODE_OF_CONDUCT.md`, no `SECURITY.md` unless
      repository-specific
- [ ] No `uses: ydongy/.github/...`, no template version markers, no links into private repositories (public
      repositories)
- [ ] Labels synced: `scripts/sync-labels.sh ydongy/<repo>` from `ydongy/.github`
- [ ] Squash merge only; the default commit message is the pull request title; branches deleted on merge
- [ ] Branch protection or ruleset on `main`: pull request required, the CI and PR title checks required
- [ ] Private vulnerability reporting enabled (public repositories)
- [ ] Releases: release-please configured, or none (see Releases); closed products: release pipeline files and
      the `release` environment with a deployment branch policy limited to `main`
- [ ] Closed products: macOS CI job runs only on manual dispatch and release pull requests

## Starting a new project

Create the repository from a template instead of copying files by hand:

- `ydongy/template-macos-app`: a native macOS app.
- `ydongy/template-mygo-app`: a Go desktop app with MyGo.

Use "Use this template" on GitHub (or `gh repo create ydongy/<name> --template ydongy/<template>`), then run the
template's `init` command with the license that matches the repository:

```bash
init --license mit          # open source
init --license proprietary  # closed-source product
```

See the template's README for the exact invocation. Afterwards go through the
[Repository checklist](#repository-checklist).
