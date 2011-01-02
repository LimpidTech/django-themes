from django.db.models.signals import post_save
from django.dispatch import receiver
from themes.models import Theme

@receiver(post_save, sender=Theme)
def post_save_handler(sender, instance, **kwargs):
    for site in instance.sites_enabled.all():
        offending_themes = list(Theme.objects.filter(sites_enabled=site))

        offending_themes.remove(instance)

        for theme in offending_themes:
            theme.sites_enabled.delete(site)
