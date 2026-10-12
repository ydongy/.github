#!/bin/bash
# Create or update labels from labels.yml in one or more repositories.
#
#   scripts/sync-labels.sh [--product] <owner/repo> [<owner/repo> ...]
#
# Default: the `common` group (open-source friendly labels). With --product the `product` group
# (handbook type/status labels for closed product repositories) is applied as well.
# Existing labels with the same name are updated (color, description); other labels in the repository
# are left alone, so per-repository scope labels survive. Needs gh with repo scope and python3.
set -euo pipefail

cd "$(dirname "$0")/.."
groups=common
if [ "${1:-}" = "--product" ]; then groups="common product"; shift; fi
[ $# -ge 1 ] || { sed -n '2,9p' "$0" | sed 's/^# \{0,1\}//'; exit 1; }

# labels.yml has top-level group keys, each a list; parse it without PyYAML so the script runs anywhere.
labels=$(GROUPS_WANTED="$groups" python3 - <<'PY'
import re, json, os
wanted = os.environ["GROUPS_WANTED"].split()
items, cur, group = [], None, None
for line in open("labels.yml", encoding="utf-8"):
    if line.lstrip().startswith("#") or not line.strip():
        continue
    m = re.match(r"^(\w+):\s*$", line)
    if m:
        group = m.group(1); cur = None; continue
    if group not in wanted:
        continue
    m = re.match(r"^\s*- name: (.+)$", line)
    if m:
        cur = {"name": m.group(1).strip()}; items.append(cur); continue
    m = re.match(r"^\s+(color|description): (.+)$", line)
    if m and cur is not None:
        cur[m.group(1)] = m.group(2).strip().strip('"')
print(json.dumps(items))
PY
)

for repo in "$@"; do
  echo "==> $repo ($groups)"
  echo "$labels" | python3 -c 'import json,sys; [print(l["name"], l["color"], l["description"], sep="\t") for l in json.load(sys.stdin)]' |
  while IFS=$'\t' read -r name color desc; do
    if gh label create "$name" --repo "$repo" --color "$color" --description "$desc" --force >/dev/null 2>&1; then
      echo "    $name"
    else
      echo "    FAILED: $name" >&2
    fi
  done
done
