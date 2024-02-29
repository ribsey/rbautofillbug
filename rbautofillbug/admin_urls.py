from django.urls import path
from reviewboard.extensions.views import configure_extension

from rbautofillbug.extension import AutoFillBugExtension
from rbautofillbug.forms import AutoFillBugExtensionSettingsForm

urlpatterns = [path('',
                    configure_extension,
                    {
                        'ext_class': AutoFillBugExtension,
                        'form_class': AutoFillBugExtensionSettingsForm,
                    }),
               ]
