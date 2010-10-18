from django.conf.urls.defaults import *
from django.conf import settings

if hasattr(settings, 'THEMES_MEDIA_URL'):
    DEFAULT_THEME = settings.THEMES_DEFAULT
else:
    DEFAULT_THEME = 'default'

urlpatterns = patterns('',
    url(r'^set/(?P<identifier>[\d^/]+)/$', 'themes.views.set'),
    url(r'^set/(?P<identifier>[^/]+)/$', 'themes.views.set', {'slugified': True}),
)
