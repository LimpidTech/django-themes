from django.contrib.sites.models import Site
from django.http import Http404
from models import Theme

def _default_theme(request):
    try:
        theme = Theme.objects.get_current_by_request(request)
    except Theme.DoesNotExist:
        try:
            theme = Theme.objects.get_list_by_request(request)[0]
        except IndexError:
            raise Http404('You must create a theme in the system.')

    return theme 

def theme_list(request):
    return {'theme_list': Theme.objects.get_list_by_request(request)}

def current_theme(request):
    theme = _default_theme(request)

    if request.session.get('theme_id'):
        try:
            theme = Theme.objects.get(pk=request.session.get('theme_id'))
        except:
            request.session['theme_id'] = theme.pk

    return {'current_theme': theme}

