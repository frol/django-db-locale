from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('db_locale.views',
    url(r'^$', 'language_list', name="db_locale_language_list"),
    url(r'^refresh/$', 'refresh_request', name="db_locale_refresh_request"),
    url(r'^apply/$', 'apply_request', name="db_locale_apply_request"),
    url(r'^(?P<language>\w+)/(?:(?P<status>nontrans)/)?$', 'translation_list', name="db_locale_translation_list"),
) 
