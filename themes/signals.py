from django.contrib.sites import models
from django.db.models import signals
from django.dispatch import receiver

from themes.models import Theme


@receiver(signals.m2m_changed, sender=Theme.sites_enabled.through)
def post_save_handler(sender, instance, **kwargs):
    if instance.__class__ is not Theme:
        return

    for site in models.Site.objects.filter(enabled_themes=instance):
        site.enabled_themes = [instance]
        site.save()
