from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.contrib.sites.models import Site
from themes.managers import ThemeManager
import pdb

# This is a default mapping used when there are no overrides present
# in the database or in settings
theme_directories = {
    'scripts': 'scripts',
    'images': 'images',
    'styles': 'styles',
}

if hasattr(settings, 'THEME_MEDIA_DIRS'):
    theme_directories.update(settings.THEME_MEDIA_DIRS)

if hasattr(settings, 'THEME_URL'):
    theme_url = settings.theme_url
else:
    theme_url = 'themes'

class ThemeOverride(models.Model):
    """ Used to override a theme's settings in the database. """

    name = models.CharField(max_length=16)
    directory = models.CharField(max_length=16)
    theme = models.ForeignKey('Theme')

    def __unicode__(self):
        return self.name

class Theme(models.Model):
    """ Represents a theme (aka skin) that can be applied to your
        django application. """

    name = models.CharField(max_length=32)
    directory = models.SlugField(max_length=32, null=True, blank=True)
    sites_enabled = models.ManyToManyField(Site, related_name='enabled_themes', blank=True)
    sites_available = models.ManyToManyField(Site, related_name='available_themes', blank=True)

    objects = ThemeManager()

    def base_url(self):
        return '%s/%s' % (theme_url, self.directory)

    def media_url(self, media_type):
        media_dir = media_type

        if media_type in theme_directories:
            media_dir = theme_directories[media_type]

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

        # Checks if any attributes retrieved end with _url...
        if name.endswith('_url'):
            # ...and calls self.media_url with the 'name' stripped
            # of it's last four characters (_url)
            return self.media_url(name[:-4])
        else:
            return getattr(super(Theme, self), name)

    def __unicode__(self):
        return self.name

