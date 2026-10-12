<div align="center">

# .github

ydongy 账号的社区默认文件、个人主页和仓库规范。

[![CI](https://github.com/ydongy/.github/actions/workflows/ci.yml/badge.svg)](https://github.com/ydongy/.github/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

[English](README.md) · **简体中文**

</div>

本仓库必须公开，因为 GitHub 只会从公开的 `.github` 仓库读取账号级默认文件。仓库中不包含产品代码、凭据或内部主机名。

## 功能特性

- 社区健康文件（`CONTRIBUTING.md`、`CODE_OF_CONDUCT.md`、`SECURITY.md`），对所有没有自带副本的仓库生效。
- Issue 表单（Bug、功能建议、文档）和简短的 Pull Request 模板。
- 账号个人主页 `profile/README.md`。
- [STANDARD.md](STANDARD.md)：唯一的仓库规范，附检查清单。
- 通用标签集 `labels.yml` 及同步脚本 `scripts/sync-labels.sh`。

## 环境要求

仅标签脚本需要：已登录且具备 repo 权限的 `gh`、`python3` 和 bash。

## 快速开始

无需安装，GitHub 会自动应用这些默认文件。要把通用标签同步到某个仓库：

```bash
scripts/sync-labels.sh ydongy/<repo>
```

## 使用方法

| 路径 | 用途 |
|---|---|
| `ISSUE_TEMPLATE/`、`pull_request_template.md` | Issue 表单和 Pull Request 模板 |
| `CONTRIBUTING.md`、`CODE_OF_CONDUCT.md`、`SECURITY.md` | 社区健康文件 |
| `profile/README.md` | 账号个人主页（中英双语；GitHub 只渲染这一份） |
| `STANDARD.md` | 开源基线、闭源补充要求、检查清单 |
| `labels.yml`、`scripts/sync-labels.sh` | 通用标签集及其同步脚本 |
| `.github/` | CODEOWNERS、Dependabot、`pr-title.yml` 和本仓库自己的 CI |

**社区默认文件。** 账号下凡是没有自带副本的仓库，GitHub 都会使用这里的 Issue 表单、Pull Request 模板、`CONTRIBUTING.md`、`CODE_OF_CONDUCT.md` 和 `SECURITY.md`。需要不同内容的仓库可以自行添加同名文件，何时适合这样做见 [STANDARD.md](STANDARD.md)。各仓库自成一体，不会调用本仓库的工作流或脚本。

**标签。**

```bash
scripts/sync-labels.sh ydongy/<repo> [ydongy/<repo2> ...]
```

创建或更新 `labels.yml` 中的全部标签（bug、enhancement、documentation、question、good first issue、help wanted、dependencies、duplicate、invalid、wontfix）。同名标签会被更新为列出的颜色和描述，其他标签保持不变。

## 开发

CI（`.github/workflows/ci.yml`）会运行 actionlint，解析 YAML 文件和 `labels.yml`，并检查脚本的 shell 语法。本地可以运行：

```bash
bash -n scripts/sync-labels.sh
actionlint
```

## 参与贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)。提交信息和 Pull Request 标题遵循 [Conventional Commits](https://www.conventionalcommits.org/)。

## 安全

请在相关仓库通过 GitHub Security 的 “Report a vulnerability” 私下报告漏洞，详见 [SECURITY.md](SECURITY.md)。

## 许可证

[MIT](LICENSE)，Copyright (c) 2026 ydongy。
