from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

# TODO: Adapt theme URLs to a dict format.

if hasattr(settings, 'THEMES_MEDIA_URL'):
    THEME_URL = settings.THEMES_MEDIA_URL
else:
    THEME_URL = '%sthemes' % settings.MEDIA_URL

if hasattr(settings, 'THEMES_STYLE_URL'):
    STYLE_URL = settings.THEMES_STYLE_URL
else:
    STYLE_URL = 'styles'

if hasattr(settings, 'THEMES_SCRIPT_URL'):
    SCRIPT_URL = settings.THEMES_SCRIPT_URL
else:
    SCRIPT_URL = 'scripts'

if hasattr(settings, 'THEMES_IMAGE_URL'):
    IMAGE_URL = settings.THEMES_IMAGE_URL % THEME_URL
else:
    IMAGE_URL = 'images'

class Theme(models.Model):
    name = models.CharField(max_length=32)
    directory = models.SlugField(max_length=32, null=True, blank=True)
    default = models.BooleanField(default=False)

    def base_url(self):
        return '%s/%s' % (THEME_URL, self.directory)

    def style_url(self):
        return '%s/%s' % (self.base_url(), STYLE_URL)

    def script_url(self):
        return '%s/%s' % (self.base_url(), SCRIPT_URL)

    def image_url(self):
        return '%s/%s' % (self.base_url(), IMAGE_URL)

    def save(self, force_insert=False, force_update=False):
        if self.default == True:
            for theme in Theme.objects.all():
                theme.default = False
                theme.save()

        self.dir_name = slugify(self.name).lower()
        super(Theme,self).save(force_insert, force_update)

    def __unicode__(self):
        return self.name

