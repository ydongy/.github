# Open-source repository standard

The single source of truth for every public repository owned by ydongy, except the closed products
(`loggia`, `barekeep`), which follow the product flow in the rest of this handbook (`core/`, docs-check,
check-issues, reusable workflows).

Open-source repositories are self-contained: they do not depend on this handbook, `docs-check`, `check-issues`,
reusable workflows or pinned SHAs from `ydongy/.github`. They only inherit its community health files and
templates through GitHub's account defaults.

## Root files

- `README.md`: `# Name`, a one-line description, badges (CI, License MIT; a repository with releases also shows
  the latest release), then the sections Features (optional), Quick start, Usage, Development (exact commands),
  Contributing (link) and License. English. A Chinese README may exist as `README.zh-CN.md`, with an
  `English | 中文` switch line at the top of both.
- `LICENSE`: MIT, `Copyright (c) 2026 ydongy`.
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
  reference this handbook, docs-check, milestones, tracking issues, sign-off, pinned SHAs or `ORG_DOCS_ROOT`.
- `CLAUDE.md`: one line, `@AGENTS.md`. No `GEMINI.md` and no `.github/copilot-instructions.md`.
- `.editorconfig`: utf-8, lf, final newline, trimmed trailing whitespace; 2 spaces by default, tabs for Go and
  Makefiles, 4 spaces for Python and Swift.

## `.github/`

- `CODEOWNERS`: `* @ydongy`
- `dependabot.yml`: `github-actions` monthly, plus the repository's own ecosystem (gomod, pip, npm, swift)
  weekly when present.
- `workflows/ci.yml`: self-contained (no `uses: ydongy/.github/...`); runs on `pull_request` and on push to
  `main`; `permissions: contents: read`; concurrency with cancel-in-progress for pull requests; actions pinned to
  major tags (for example `actions/checkout@v5`).
- `workflows/pr-title.yml`: `pull_request_target` with types `opened`, `edited`, `synchronize`, `reopened`;
  `permissions: pull-requests: read`; no checkout; the title (`${{ github.event.pull_request.title }}`) is passed
  through an environment variable and validated against the Conventional Commits pattern in bash; skipped for
  `dependabot[bot]`.
- Issue and pull request templates: none per repository; they are inherited from `ydongy/.github`
  (bug, feature, documentation; a short pull request template). Blank issues are disabled there.
- Not present: a docs-check caller workflow, any `uses: ydongy/.github/...` caller, `.docs-check.json`,
  `.repo-type`.

## `docs/`

Keep only documents that describe the project to its users and contributors: architecture, ADRs, design notes.
Do not keep internal process material (milestones, process, legal or website plans, roadmaps with internal
dependencies), template version markers such as `<!-- template: ... v1 -->`, or links into private
repositories. Remove `.claude/` and `.codex/` directories unless they are part of what the project offers (for
example a template that ships agent configuration on purpose); in that case say so in the README.

## Labels

`scripts/sync-labels.sh <owner/repo>` applies the `common` group of `labels.yml` (bug, enhancement,
documentation, question, good first issue, help wanted, dependencies, duplicate, invalid, wontfix). The `product`
group is only for closed products (`--product`).

## Releases

- Repositories with releases use release-please (`googleapis/release-please-action@v4`, release type `simple`,
  `release-please-config.json` and `.release-please-manifest.json`, a `VERSION` file when useful). Tags are
  `vX.Y.Z`. The workflow has `contents: write` and `pull-requests: write` and uses `GITHUB_TOKEN`.
- Other repositories (templates, websites, tooling) have no release automation; `CHANGELOG.md` `[Unreleased]` is
  maintained by hand.
