from reviewboard.extensions.packaging import setup


PACKAGE = "rbautofillbug"
VERSION = "0.1.2"

setup(
    name=PACKAGE,
    version=VERSION,
    description="A ReviewBoard extension that extracts bug IDs from review "
                "request summaries",
    author="Jeremie Jost",
    author_email="jeremiejost@gmail.com",
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
