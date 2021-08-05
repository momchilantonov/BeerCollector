from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from beer_collector.account.models import Account
from beer_collector.core.utilities import image_upload_location

UserModel = get_user_model()


class CollectorProfile(models.Model):
    username = models.CharField(
        _('username'),
        max_length=20,
        blank=True,
        null=True,
    )
    first_name = models.CharField(
        _('first name'),
        max_length=20,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        _('last name'),
        max_length=20,
        blank=True,
        null=True,
    )
    about = models.CharField(
        _('about'),
        max_length=300,
        blank=True,
        null=True,
    )
    image = models.ImageField(
        _('image'),
        upload_to=image_upload_location,
        blank=True,
        null=True,
    )
    is_complete = models.BooleanField(
        default=False,
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
