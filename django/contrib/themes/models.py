from django.db import models

class Theme(models.Model):
    """ A theme is a collection of scripts, images, templates, and any other media
        that might need to be used as a resource for downloading a web site. """
    name = models.CharField(max_length=32, null=False, blank=False)
    directory = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

