from models import Theme

class ThemeMiddleware(object):
    """ Populates our request and modifies the templating system to respect themes. """

    def process_request(self, request):
        if getattr(request, 'theme'):
            return

        request.theme = None

        if 'theme' in request.COOKIES:
            try:
                request.theme = Theme.objects.get(pk=request.COOKIES['theme'])
            except:
                del request.COOKIES.theme

