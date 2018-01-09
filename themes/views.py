from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from themes import models

def set(request, identifier, slugified=False):
    if slugified == True:
        theme = get_object_or_404(models.Theme, name=identifier)
    else:
        theme = get_object_or_404(models.Theme, id=identifier)

    request.session['theme_id'] = theme.pk

    return HttpResponseRedirect('/')
