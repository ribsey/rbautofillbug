from __future__ import unicode_literals

from django.conf.urls import patterns, url

from rbautofillbug.extension import AutoFillBugExtension


urlpatterns = patterns(
    'rbautofillbug.views',

    url(r'^$', 'configure'),
)