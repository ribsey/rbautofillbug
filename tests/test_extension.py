#!/usr/bin/env python

from rbautofillbug.extension import AutoFillBugExtension, find_bugs
from unittest import TestCase
import unittest
from django.conf import settings
settings.configure()


class TestAutoFillBugsExtension(TestCase):
    def test_find_bugs_single_regex(self):
        bug_regex = "#(\d+)"
        bugs = find_bugs(bug_regex, "#42: frobnicate() throws ValueError")
        self.assertItemsEqual(bugs, ['42'])

    def test_find_bugs_default_regex(self):
        bug_regex = AutoFillBugExtension.default_settings['bug_format']
        bugs = find_bugs(bug_regex, "#42: frobnicate() throws ValueError")
        self.assertItemsEqual(bugs, ['42'])

    def test_find_bugs_multiple_regexes(self):
        bug_regex = "#(\d+)|issue (\d+)"
        # The regex should work for both formats.
        bugs = find_bugs(bug_regex, "#42: frobnicate() throws ValueError")
        self.assertItemsEqual(bugs, ['42'])
        bugs = find_bugs(bug_regex, "issue 42: frobnicate() throws ValueError")
        self.assertItemsEqual(bugs, ['42'])

    def test_find_bugs_multiple_regexes_in_same_summary(self):
        bug_regex = "#(\d+)|issue (\d+)"
        bugs = find_bugs(bug_regex,
                         "#17: foo() returns trailing whitespace (also fixes issue 11)")
        self.assertItemsEqual(bugs, ['17', '11'])


if __name__ == '__main__':
    unittest.main()
