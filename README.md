Auto Fill Bugs extension for ReviewBoard
========================================

Overview
--------

This ReviewBoard extension automatically fills the _Bugs_ field of a review request draft with the bug IDs mentioned in the request summary.

Requirements
------------

This extension requires ReviewBoard 2.0 or higher.

Installation
------------

```bash
git clone git://github.com/jjst/rbautofillbug
cd rbautofillbug
python setup.py install
```

Then go to your Administration UI -> Extensions page and click "Check for installed extensions". The extension should show up. If it does not, reload your web server and try again.

Configuration
-------------

You can change the regular expresssion used to extract bug IDs from the summary by clicking on the "Configure" link for the extension on the extensions list page. By default, AutoFillBugs will recognise bug IDs of the form _#42_.
