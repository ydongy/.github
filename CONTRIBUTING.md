# Contributing

Thanks for helping. These defaults apply to every repository owned by ydongy that has no `CONTRIBUTING.md` of its own.

## Before you start

- Search existing issues and pull requests first.
- Open an issue before any large change so the approach can be agreed before you write code. Small fixes can go
  straight to a pull request.
- Read the repository's `README.md` (and `AGENTS.md`, if present) for setup, test and lint commands.

## Making a change

1. Fork the repository and create a branch from `main`, named `<type>/<issue>-<slug>`, for example
   `fix/42-empty-input`.
2. Keep the change focused: one concern per pull request.
3. Run the repository's test and lint commands and make sure they pass.
4. Update documentation and the changelog when behavior changes.
5. Use [Conventional Commits](https://www.conventionalcommits.org/) for commit messages and the PR title:
   `feat|fix|docs|refactor|perf|test|build|ci|chore|revert(scope)!: subject`.
6. Open a pull request and fill in the template.

Pull requests are squash-merged by a maintainer, so the PR title becomes the commit message. No DCO or
sign-off is required.

## Security

Do not report vulnerabilities in public issues. See [SECURITY.md](SECURITY.md).

## Conduct and license

Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md). Unless a repository says otherwise,
contributions are licensed under the MIT License, the same as the project.
