import os
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db import models
from beer_collector.account.models import Account
from beer_collector.core.views import get_obj_by_pk

UserModel = get_user_model()


def image_upload_location(instance, filename):
    current_user = get_obj_by_pk(Account, instance.pk)
    return f'{os.path.join(current_user.email, filename)}'


class CollectorProfile(models.Model):
    username = models.CharField(
        _('username'),
        max_length=20,
        blank=True,
    )
    first_name = models.CharField(
        _('first name'),
        max_length=20,
        blank=True,
    )
    last_name = models.CharField(
        _('last name'),
        max_length=20,
        blank=True,
    )
    about = models.CharField(
        _('about'),
        max_length=300,
        blank=True,
    )
    image = models.ImageField(
        _('image'),
        upload_to=image_upload_location,
        blank=True,
    )
    is_complete = models.BooleanField(
        default=False,
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.username
