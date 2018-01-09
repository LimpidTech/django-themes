from django.conf import settings
from django.contrib.sites import models as site_models
from django.db import models
from django.template.defaultfilters import slugify

from themes import managers


# This is a default mapping used when there are no overrides present
# in the database or in settings
THEME_DIRECTORIES = getattr(settings, 'THEME_MEDIA_DIRECTORIES', {
    'scripts': 'scripts',
    'images': 'images',
    'styles': 'styles',
})


THEME_URL = getattr(settings, 'THEME_URL', 'themes')


class ThemeOverride(models.Model):
    """ Used to override a theme's settings in the database. """

    name = models.CharField(max_length=16)
    directory = models.CharField(max_length=16)
    theme = models.ForeignKey('Theme', on_delete=models.DO_NOTHING)

    def __unicode__(self):
        return self.name


class Theme(models.Model):
    """ Represents a theme (aka skin) that can be applied to your
        django application. """

    name = models.CharField(max_length=32)
    directory = models.SlugField(max_length=32, null=True, blank=True)
    sites_enabled = models.ManyToManyField(site_models.Site, related_name='enabled_themes', blank=True)
    sites_available = models.ManyToManyField(site_models.Site, related_name='available_themes', blank=True)

    objects = managers.ThemeManager()

    def base_url(self):
        return '%s/%s' % (THEME_URL, self.directory)

    def media_url(self, media_type):
        media_dir = media_type

        if media_type in THEME_DIRECTORIES:
            media_dir = THEME_DIRECTORIES[media_type]

        try:
            override = ThemeOverride.objects.get(theme=self,name=media_type)
            media_dir = override.value

        except ThemeOverride.DoesNotExist:
            pass

        return '%s/%s' % (self.base_url(), media_type)

    def save(self, *args, **kwargs):
        if self.directory is None:
            self.directory = slugify(self.name).lower()

        super(Theme, self).save(*args, **kwargs)

    def __getattr__(self, name):
        potential_suffix = '_url'

        if name.endswith(potential_suffix):
            offset = len(potential_suffix) * -1
            return self.media_url(name[:offset])

        return getattr(super(Theme, self), name)

    def __unicode__(self):
        return self.name
