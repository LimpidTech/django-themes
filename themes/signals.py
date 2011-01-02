from django.db.models.signals import m2m_changed
from django.contrib.sites.models import Site
from django.dispatch import receiver
from themes.models import Theme

@receiver(m2m_changed, sender=Theme.sites_enabled.through)
def post_save_handler(sender, instance, **kwargs):
    if instance.__class__ is Theme:
        for site in Site.objects.filter(enabled_themes=instance):
            site.enabled_themes = [instance]
            site.save()

