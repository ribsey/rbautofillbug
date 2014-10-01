from __future__ import unicode_literals

from reviewboard.extensions.packaging import setup


PACKAGE = "rbautofillbug"
VERSION = "0.1"

setup(
    name=PACKAGE,
    version=VERSION,
    description="Extension rbautofillbug",
    author="Jeremie Jost",
    author_email="jeremiejost@gmail.com"
    packages=["rbautofillbug"],
    entry_points={
        'reviewboard.extensions':
            '%s = rbautofillbug.extension:AutoFillBugExtension' % PACKAGE,
    },
    package_data={
        'rbautofillbug': [
            'templates/rbautofillbug/*.txt',
            'templates/rbautofillbug/*.html',
        ],
    }
)
