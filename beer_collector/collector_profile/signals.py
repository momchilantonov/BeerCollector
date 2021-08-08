import os
from beer_collector.core.utilities import get_obj_by_pk
from django.conf import settings
from django.db.models.signals import pre_delete, post_save, pre_save
from django.contrib.auth import get_user_model
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
    if instance.username \
            and instance.first_name \
            and instance.last_name \
            and instance.image \
            and instance.about:
        instance.is_complete = True
    else:
        instance.is_complete = False


@receiver(pre_delete, sender=UserModel)
def delete_image_when_delete_account(sender, instance, **kwargs):
    current_profile = get_obj_by_pk(CollectorProfile, instance.pk)
    current_profile_image_location = os.path.join(settings.MEDIA_ROOT, str(instance.email))
    if current_profile.image:
        current_profile.image.delete()
    if os.path.isdir(current_profile_image_location):
        os.rmdir(current_profile_image_location)
