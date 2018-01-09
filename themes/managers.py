from django.contrib.sites import models as site_models
from django.db import models


def _get_current_site(request):
    # Attempts to use monodjango.middleware.SiteProviderMiddleware
    try:
        return Site.objects.get_current(request)
    except TypeError:
        pass

    return Site.objects.get_current()


class ThemeManager(models.Manager):
    def get_current_by_request(self, request=None):
        """ Gets the current  """

        return self.get_current(_get_current_site(request))

    def get_current(self, site=None):
        """ Gets the current system theme. """

        if site is None:
            site = Site.objects.get_current()

        return self.get(sites_enabled=site)

    def get_list_by_request(self, request=None):
        """ Gets a list of themes that are available for the given request. """

        return self.get_list(_get_current_site(request))

    def get_list(self, site=None):
        """ Get a list of themes available on a specific site. """

        if site is None:
            site = Site.objects.get_current()

        return self.filter(sites_available=site)

    def get_default(self):
            return self.get(default=True)
