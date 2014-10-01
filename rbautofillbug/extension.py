# rbautofillbug Extension for Review Board.

from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include
from reviewboard.extensions.base import Extension


class AutoFillBugExtension(Extension):
    metadata = {
        'Name': 'rbautofillbug',
        'Summary': 'Describe your extension here.',
    }
    is_configurable = True

    def initialize(self):
        # Your extension initialization is done here.
        pass