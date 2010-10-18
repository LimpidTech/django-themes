from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from models import Theme

def set(request, identifier, slugified=False):
    if slugified == True:
        theme = get_object_or_404(Theme, name=identifier)
    else:
        theme = get_object_or_404(Theme, id=identifier)

    request.session['theme_id'] = theme.pk

    return HttpResponseRedirect('/')
