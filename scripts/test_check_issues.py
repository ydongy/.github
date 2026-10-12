#!/usr/bin/env python3
"""Self-test for check-issues.py: python3 scripts/test_check_issues.py"""
import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("check_issues", Path(__file__).resolve().parent / "check-issues.py")
check_issues = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_issues)
check = check_issues.check


def issue(number, milestone, *labels):
    return {"number": number, "milestone": milestone, "labels": set(labels)}


MILESTONES = ["v1.1", "v1.2", "Later"]
GOOD = [
    issue(1, "v1.1", "milestone"), issue(2, "v1.1", "feat"),
    issue(3, "v1.2", "milestone"), issue(4, "v1.2", "feat"),
    issue(5, "Later", "feat", "needs-decision"),
]
SUBS = {1: [2], 3: [4]}


class CheckIssues(unittest.TestCase):
    def test_good(self):
        self.assertEqual(check(MILESTONES, GOOD, SUBS), [])

    def test_no_issues_needs_no_later(self):
        self.assertEqual(check([], [], {}), [])

    def test_missing_milestone(self):
        self.assertEqual(check(MILESTONES, GOOD + [issue(6, None, "feat")], SUBS),
                         ["#6: no milestone; file it in Later or a planned milestone"])

    def test_missing_later(self):
        problems = check(["v1.1"], [issue(1, "v1.1", "milestone")], {})
        self.assertEqual(problems, ['milestone "Later": missing; unscheduled issues go there'])

    def test_tracking_issue_count(self):
        problems = check(MILESTONES, GOOD + [issue(6, "v1.1", "milestone")], SUBS)
        self.assertIn("found #1, #6", problems[0])
        problems = check(MILESTONES, [i for i in GOOD if i["number"] != 3], SUBS)
        self.assertIn("found none", problems[0])

    def test_not_a_sub_issue(self):
        self.assertEqual(check(MILESTONES, GOOD + [issue(6, "v1.2", "feat")], SUBS),
                         ['#6: not a sub-issue of #3, the tracking issue of "v1.2"'])

    def test_tracker_in_later(self):
        self.assertEqual(check(MILESTONES, GOOD + [issue(6, "Later", "milestone")], SUBS),
                         ["#6: a tracking issue in Later"])

    def test_closed_milestone(self):
        self.assertEqual(check(MILESTONES, GOOD + [issue(6, "v1.0", "feat")], SUBS),
                         ['#6: in the closed milestone "v1.0"'])


if __name__ == "__main__":
    unittest.main()
