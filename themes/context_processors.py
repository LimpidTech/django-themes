from django.http import Http404
from models import Theme

def _default_theme():
    try:
        theme = Theme.objects.get(default=True)
    except:
        try:
            theme = Theme.objects.all()[0]
        except:
            raise Http404('You must create a theme in the system.')

    return theme 

def list(request):
    return {'theme_list': Theme.objects.all()}

def current(request):
    theme = _default_theme()

    if request.session.get('theme_id'):
        try:
            theme = Theme.objects.get(pk=request.session.get('theme_id'))
        except:
            request.session['theme_id'] = theme.pk

    return {'current_theme': theme}

