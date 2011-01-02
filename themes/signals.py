from django.db.models.signals import post_save
from django.dispatch import receiver
from themes.models import Theme

@receiver(post_save, sender=Theme)
def post_save_handler(sender, instance, **kwargs):
    for site in instance.sites_enabled.all():
        site.enabled_themes = [instance]
        site.save()

