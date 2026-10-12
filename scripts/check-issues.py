#!/usr/bin/env python3
"""Check a repository's open issues against the milestone rules (handbook/core/process.md, Roadmap and intake).

    python3 check-issues.py <owner/repo>

  - every open issue has a milestone
  - a milestone named `Later` exists when there are open issues
  - every open milestone other than `Later` has exactly one open tracking issue (label `milestone`)
  - in a milestone with a tracking issue, every other open issue is a sub-issue of it
  - `Later` holds no tracking issue

Reads GitHub through `gh api` (gh with repo scope). Exit status 1 when any check fails; every problem is
printed as `#<n>: message` or `milestone "<title>": message`.
"""
import json
import subprocess
import sys
import time

LATER = "Later"
TRACKING = "milestone"


def gh(path, attempts=3):
    """Every item of a paginated REST list; a dropped connection is retried."""
    for attempt in range(attempts):
        run = subprocess.run(["gh", "api", "--paginate", "--slurp", path], capture_output=True, text=True)
        if run.returncode == 0:
            return [item for page in json.loads(run.stdout) for item in page]
        if attempt + 1 < attempts:
            time.sleep(2 ** attempt)
    sys.exit(f"gh api {path}: {run.stderr.strip() or f'exit status {run.returncode}'}")


def check(milestones, issues, sub_issues):
    """milestones: open milestone titles; issues: open issues as {number, milestone, labels};
    sub_issues: tracking issue number -> numbers of its sub-issues. Returns the problems."""
    problems = []
    if issues and LATER not in milestones:
        problems.append(f'milestone "{LATER}": missing; unscheduled issues go there')
    by_milestone = {}
    for issue in issues:
        if issue["milestone"] is None:
            problems.append(f"#{issue['number']}: no milestone; file it in {LATER} or a planned milestone")
        else:
            by_milestone.setdefault(issue["milestone"], []).append(issue)
    for title in milestones:
        members = by_milestone.get(title, [])
        trackers = [i for i in members if TRACKING in i["labels"]]
        if title == LATER:
            problems += [f"#{i['number']}: a tracking issue in {LATER}" for i in trackers]
            continue
        if len(trackers) != 1:
            found = ", ".join(f"#{i['number']}" for i in trackers) or "none"
            problems.append(f'milestone "{title}": needs exactly one open tracking issue (label {TRACKING}), found {found}')
            continue
        tracker = trackers[0]["number"]
        children = set(sub_issues.get(tracker, ()))
        for issue in members:
            if issue["number"] != tracker and issue["number"] not in children:
                problems.append(f"#{issue['number']}: not a sub-issue of #{tracker}, the tracking issue of \"{title}\"")
    for title in by_milestone:
        if title not in milestones:
            problems += [f'#{i["number"]}: in the closed milestone "{title}"' for i in by_milestone[title]]
    return problems


def main():
    if len(sys.argv) != 2 or "/" not in sys.argv[1]:
        sys.exit(__doc__)
    repo = f"repos/{sys.argv[1]}"
    milestones = [m["title"] for m in gh(f"{repo}/milestones?state=open&per_page=100")]
    issues = [
        {"number": i["number"], "milestone": (i["milestone"] or {}).get("title"),
         "labels": {label["name"] for label in i["labels"]}}
        for i in gh(f"{repo}/issues?state=open&per_page=100") if "pull_request" not in i
    ]
    sub_issues = {
        i["number"]: [s["number"] for s in gh(f"{repo}/issues/{i['number']}/sub_issues?per_page=100")]
        for i in issues if TRACKING in i["labels"]
    }
    problems = check(milestones, issues, sub_issues)
    for problem in problems:
        print(problem)
    if problems:
        sys.exit(1)
    print("issues ok")


if __name__ == "__main__":
    main()
