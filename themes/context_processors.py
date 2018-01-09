from django.contrib.sites.models import Site
from django.http import Http404

from themes import models

def _default_theme(request):
    try:
        theme = models.Theme.objects.get_current_by_request(request)
    except models.Theme.DoesNotExist:
        try:
            theme = models.Theme.objects.get_list_by_request(request)[0]
        except IndexError:
            raise Http404('You must create a theme in the system.')

    return theme 

def theme_list(request):
    theme_list = models.Theme.objects.get_list_by_request(request)

    return {
        'theme_list': theme_list,
    }

def current_theme(request):
    theme = _default_theme(request)

    if request.session.get('theme_id'):
        try:
            theme = models.Theme.objects.get(pk=request.session.get('theme_id'))
        except:
            request.session['theme_id'] = theme.pk

    return {
        'current_theme': theme,
    }
