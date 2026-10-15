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
  - [Repository settings](#repository-settings)
- [Part 2: Closed-source products](#part-2-closed-source-products)
  - [Pre-release products](#pre-release-products)
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
- `LICENSE`: MIT, `Copyright (c) 2026 ydongy` (closed products: see Part 2). Do not change an existing
  repository's license without the maintainer's decision.
- `THIRD_PARTY.md`: only when the repository ships third-party code or licenses in its build artifacts.
- `CHANGELOG.md`: Keep a Changelog style with an `## [Unreleased]` section. Repositories that use release-please
  let it write the entries and have no `## [Unreleased]` section (release-please inserts each release on top). Do not keep `CHANGELOG.zh.md` unless a website consumes it.
- `CONTRIBUTING.md`: per repository, short, English. It states: issues and pull requests may be written in
  English or Simplified Chinese; open an issue before large changes; development
  setup; the exact test and lint commands; Conventional Commits for commit messages and pull request titles
  (`feat|fix|docs|refactor|perf|test|build|ci|chore|revert(scope)!: subject`); branches named
  `<type>/<issue>-<slug>`; squash merge by a maintainer; no DCO or sign-off. A repository without its own file
  inherits the account default.
- `CODE_OF_CONDUCT.md`, `SECURITY.md`, `GOVERNANCE.md` and `SUPPORT.md`: not per repository. The first two are
  inherited from `ydongy/.github`; governance and support are covered by `CONTRIBUTING.md`. A repository may
  keep its own `SECURITY.md` only if it has repository-specific scope; reporting must then go through
  `https://github.com/ydongy/<repo>/security/advisories/new` (no e-mail).
- `AGENTS.md`: a self-contained agent guide (what it is, layout, commands, conventions, red lines). It does not
  reference `ydongy/.github`, milestones, tracking issues, sign-off or pinned SHAs. It has an "Issues and pull
  requests" section that spells out the issue forms and the pull request template (headings and labels), because
  agents create issues and pull requests with `gh` and the command line skips the forms and the template:
  bug (`## What happened`, `## What you expected`, `## Steps to reproduce`, `## Version and environment`),
  feature (`## Problem`, `## Proposed solution`, `## Alternatives considered`, `## Done when`), documentation
  (`## Where`, `## What is missing, unclear or wrong`, `## Suggested change`), and the pull request body
  (`## Summary`, `## Related issue`, `## How tested`, `## Checklist`). Red lines always include: credentials never
  go into pull requests, issues, logs or chat; releases, signing and anything sent to an external service need
  the maintainer's confirmation; no blind `git add -A` of unknown files.
- `CLAUDE.md`: one line, `@AGENTS.md`. No `GEMINI.md` and no `.github/copilot-instructions.md`.
- `.editorconfig`: utf-8, lf, final newline, trimmed trailing whitespace; 2 spaces by default, tabs for Go and
  Makefiles, 4 spaces for Python and Swift.
- Toolchain pins where the ecosystem has them: `.go-version`, `.node-version`.

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
- Other workflows only when the repository needs them (`package.yml` for unsigned development builds,
  `release.yml` for releases). No `dco.yml`.
- Issue and pull request templates: none per repository; they are inherited from `ydongy/.github`
  (bug, feature, documentation in its `.github/ISSUE_TEMPLATE/`, the only place GitHub reads account defaults
  from; a short pull request template). Blank issues are disabled there.
- Not present: any `uses: ydongy/.github/...` caller, document-check configuration, repository-type markers or
  template version markers in documents.

### docs/

Keep only documents that describe the project to its users and contributors: architecture, ADRs, design notes.
Do not keep internal process material (milestones, process, roadmaps with internal dependencies), template
version markers (HTML comments naming a template and version), or links into private repositories. Remove `.claude/` and
`.codex/` directories unless they are part of what the project offers (for example a template that ships agent
configuration on purpose); in that case say so in the README. Closed products keep more; see Part 2.

Screenshots for a pull request go into the pull request body, not into the repository.

### Labels

`scripts/sync-labels.sh <owner/repo>` in `ydongy/.github` applies the labels in `labels.yml` (bug, enhancement,
documentation, question, good first issue, help wanted, dependencies, duplicate, invalid, wontfix). A repository
may add its own scope labels (for example `ui`, `accessibility`, `scope:web`); the sync never creates or removes
them. Labels that duplicate a Conventional Commits type (`feat`, `fix`, `docs` and so on) or encode a process
state (`needs-decision`, `needs-triage`, `accepted`) are not used.

### Releases

- Repositories with releases use release-please (`googleapis/release-please-action@v5`, release type `simple`,
  `release-please-config.json` and `.release-please-manifest.json` with `include-component-in-tag: false`, a
  `VERSION` file when useful). Tags are `vX.Y.Z`; release-please creates the tag and the GitHub Release when its
  release pull request is merged.
- release-please runs with a token of the account's release GitHub App, never `GITHUB_TOKEN` or a personal access
  token: pull requests opened with `GITHUB_TOKEN` start no workflows, so the checks the `main` ruleset requires
  would never run. The workflow's own permissions are `contents: read`; a first step mints the token with
  `actions/create-github-app-token` (`client-id` and `private-key` from the repository secrets
  `RELEASE_APP_CLIENT_ID` and `RELEASE_APP_PRIVATE_KEY`, `repositories: <repo>`, `permission-contents: write`,
  `permission-pull-requests: write`). The app has only Contents and Pull requests write, no webhook, is installable
  only on this account, and is installed only on the repositories that release with it.
- Other repositories (templates, websites, tooling) have no release automation; `CHANGELOG.md` `[Unreleased]` is
  maintained by hand.

### Repository settings

Set on GitHub by the ydongy account (they are not stored in files):

- Squash merge only; the default commit message is the pull request title; delete head branches on merge.
- Ruleset `main` on the default branch: no deletion, no force push, linear history, pull request required (squash
  only), the CI and PR title checks required; repository admins may bypass only when merging a pull request.
  Private repositories on GitHub Free cannot have rulesets or branch protection: follow the same flow by
  convention (branch, pull request, green checks, squash merge).
- Private vulnerability reporting enabled (public repositories).
- Discussions off unless the repository's `CONTRIBUTING.md` points to them.

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

### Pre-release products

A closed product whose code is finished but which is not yet on sale (no domain, mailbox, download host or release
credentials) is pre-release. The state is explicit and temporary; it ends with the launch pull request.

**Status marking**

- `README.md` and `README.zh-CN.md` carry the badge `![Status](https://img.shields.io/badge/status-pre--release-orange)`
  and one sentence of status that says the product is not available yet and links `docs/launch.md`. The website
  repository uses `status-pre--launch` instead.
- No link or badge points to a domain that does not resolve yet. No public text promises a mailbox or download
  address that does not exist yet; the security contact is the account's SECURITY policy (GitHub private
  vulnerability reporting).
- Text that is private to the repository (`LICENSE`, `docs/`, code constants) may already name the planned domain;
  `docs/launch.md` lists every such place.

**Release machinery**

- No `release` environment, no release secrets, no release workflow, no automatic publishing.
- The version and the changelog are maintained as usual. Notes stay under `## [Unreleased]` (or the first version's
  section stays a draft). No tag and no GitHub Release is created.

**`docs/launch.md`**

- Required. It is the launch checklist and the single source of truth: Markdown checkboxes grouped by phase, each item
  stating what to do, where, and how to verify it, including every place that depends on the planned domain.
- Items are checked off before launch; the launch pull request links the file.

**Launch**

1. Complete the infrastructure phases of `docs/launch.md` (domain, site, mail, downloads and updates, signing,
   legal and content).
2. One pull request titled `chore(release): launch <version>` removes the pre-release state: the README badge and
   status sentence (both languages), the website's pre-launch marking, and restores the support mailbox and
   download links.
3. The version bump pull request publishes the release (`docs/releasing.md`).
4. After the release, run the post-launch checks, then archive the checklist: keep the file, add the launch date
   and mark it as done.

### Issues and labels

No milestone, tracking-issue or `Later` rules, and no issue-checking script. Labels are the common set, plus
product labels where useful. Issue and pull request templates are inherited from `ydongy/.github`; do not add
task or decision forms.

### Design

Keep `design/screens/*.html` mockups, tokens, icon sources and their scripts (`check-tokens.py`,
`export-icons.mjs`, `icon.html`, `*-icon.js`, `icon-layers`). `design/README.md` is a short self-contained
description: what is there, how to preview it, how to regenerate icons. No status ledger, status words, A/B
tiers, sign-off states or screenshot checks. `AGENTS.md` keeps one design rule: "A UI change starts from the
mockup in design/screens/; the maintainer confirms the visual direction before UI code is written."

Screenshots of the running app are not tracked. Capture scripts write them to `design/screenshots/`, which
`.gitignore` lists; a UI pull request shows light and dark screenshots in its description, and the README image
links to the product website. A repository that once tracked screenshots removes them from its history.

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

Check each item when creating or auditing a repository.

- [ ] Name, one-line description and topics set; visibility chosen (open source: public; closed product: private)
- [ ] `LICENSE` matches the visibility (MIT or proprietary)
- [ ] `README.md` and `README.zh-CN.md` have the required sections, badges and language switch line
- [ ] `CONTRIBUTING.md` lists the exact test and lint commands and the language rule (open source may inherit
      the default)
- [ ] `AGENTS.md` is self-contained with the red lines and the "Issues and pull requests" section; `CLAUDE.md` is
      the single line `@AGENTS.md`; no `GEMINI.md`, no `.github/copilot-instructions.md`
- [ ] `CHANGELOG.md` has `## [Unreleased]`, except with release-please (closed products: plus `CHANGELOG.zh.md`)
- [ ] `.editorconfig` present; toolchain pins (`.go-version`, `.node-version`) where the ecosystem has them
- [ ] `.github/CODEOWNERS` is `* @ydongy`
- [ ] `.github/dependabot.yml`: github-actions monthly plus the repository's ecosystem weekly
- [ ] `.github/workflows/ci.yml` is self-contained, with `contents: read` and actions pinned to major tags
- [ ] `.github/workflows/pr-title.yml` checks Conventional Commits; no `dco.yml`
- [ ] No per-repository issue or pull request templates, no `CODE_OF_CONDUCT.md`, `GOVERNANCE.md` or
      `SUPPORT.md`, no `SECURITY.md` unless repository-specific
- [ ] No `uses: ydongy/.github/...`, no template version markers, no links into private repositories (public
      repositories)
- [ ] Labels synced: `scripts/sync-labels.sh ydongy/<repo>` from `ydongy/.github`; no type or process-state
      labels
- [ ] Repository settings applied (see [Repository settings](#repository-settings))
- [ ] No screenshots tracked; a pull request shows them in its description
- [ ] Releases: release-please configured, or none (see Releases); with release-please, the release app installed
      on the repository and `RELEASE_APP_CLIENT_ID` / `RELEASE_APP_PRIVATE_KEY` set; closed products: release
      pipeline files and the `release` environment with a deployment branch policy limited to `main`
- [ ] Closed products: macOS CI job runs only on manual dispatch and release pull requests
- [ ] Closed products: no screenshots tracked, in the tree or in the history; `design/screenshots/` ignored
- [ ] Closed products not yet on sale: follow [Pre-release products](#pre-release-products) (badge, `docs/launch.md`,
      no release environment)

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
