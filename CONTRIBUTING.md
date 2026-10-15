# Contributing

Thanks for helping. These defaults apply to every repository owned by ydongy that has no `CONTRIBUTING.md` of
its own. Most ydongy projects are built by the maintainer working with AI coding agents; contributions from
anyone are welcome.

## Languages

Issues, pull requests, commit messages and reviews may be in English or Simplified Chinese. Replies follow the
language of the thread.
欢迎用中文或英文提 issue、PR 和写提交信息，回复跟随所在讨论的语言。

## Before you start

- Search existing issues and pull requests first.
- Open an issue before any large change so the approach can be agreed before you write code. Small fixes can go
  straight to a pull request. A feature outside the project's stated scope may be closed.
- Read the repository's `README.md` and `AGENTS.md` for setup, test and lint commands.

## Making a change

1. Fork the repository and create a branch from `main`, named `<type>/<issue>-<slug>`, for example
   `fix/42-empty-input`.
2. Keep the change focused: one concern per pull request.
3. Run the repository's test and lint commands and make sure they pass.
4. Update documentation and the changelog when behavior changes.
5. Use [Conventional Commits](https://www.conventionalcommits.org/) for commit messages and the PR title:
   `feat|fix|docs|refactor|perf|test|build|ci|chore|revert(scope)!: subject`.
6. Open a pull request, link the issue with `Closes #<n>` and fill in the template.

Pull requests are squash-merged by the maintainer, so the PR title becomes the commit message. No DCO or
sign-off is required.

## AI-assisted changes

AI tools are fine. Say in the pull request which one you used and for what. You are responsible for every line
you submit: read it, understand it and run it.

## Security

Do not report vulnerabilities in public issues. See [SECURITY.md](SECURITY.md).

## Conduct and license

Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md). Contributions are licensed under the
repository's license (MIT unless the repository says otherwise).
