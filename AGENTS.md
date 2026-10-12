<!-- template: AGENTS.md v1 -->
# AGENTS.md

## What it is

The account defaults repository of ydongy: the handbook, the document templates, the shared labels, issue and PR
templates, community health files, and the reusable CI workflows used by every repository.

## Sources of truth

`handbook/` is the single source for how repositories are structured, documented, built and released.
`handbook/templates/manifest.json` says which repository type needs which documents. Core rules are mandatory. Type and stack presets apply to the components a project actually uses;
a documented project decision may override a preset, but not the security or maintainer-approval rules.

## Directory boundaries

```
handbook/              core/ (mandatory), guides/ (conditional), stacks/ (per language), types/ (presets),
                       playbooks/, templates/ (common/ and one directory per type)
.github/workflows/     reusable workflows (workflow_call), called from product repositories
scripts/               check-docs.py, check-issues.py, sync-labels.sh
profile/               account profile page
```

Nothing product-specific lives here; use `<Name>` and `<domain>` in examples.

## Commands

```bash
python3 scripts/check-docs.py .        # documents against the templates
python3 scripts/check-issues.py <owner/repo>   # open issues against the milestone rules (needs gh)
scripts/sync-labels.sh <owner/repo>    # apply labels.yml
```

## Project rules

- A change to a template raises its version (`<!-- template: <name> v<N> -->`) and every product repository
  migrates explicitly with its pinned handbook revision (`handbook/core/docs.md`).
- A change to a reusable workflow is tested from a product repository's branch before it is merged.

## Red lines

This repository is public: no credentials, no internal hostnames. See `handbook/core/agents.md`.
