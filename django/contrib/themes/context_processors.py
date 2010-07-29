from models import Theme

def current_theme(request):
    if not request.theme is None:
        return {'current_theme': request.theme}

def theme_list(request):
    return {'theme_list': Theme.objects.all()}

