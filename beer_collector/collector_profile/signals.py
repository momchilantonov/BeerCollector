from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from beer_collector.collector_profile.models import CollectorProfile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = CollectorProfile(
            user=instance,
        )
        profile.save()


@receiver(pre_save, sender=CollectorProfile)
def is_profile_complete(sender, instance, **kwargs):
    if instance.image and instance.about:
        instance.is_complete = True
