from django.db.models.signals import post_save
from django.dispatch import receiver
from themes.models import Theme

@receiver(post_save, sender=Theme)
def post_save_handler(sender, instance, **kwargs):
    for site in instance.sites_enabled.all():
        offending_themes = Theme.objects.filter(sites_enabled=site)

        for theme in offending_themes:
            enabled_sites = list(theme.sites_enabled.all())
            enabled_sites.remove(site)

            theme.sites_enabled = enabled_sites
            theme.save()

