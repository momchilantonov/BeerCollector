from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db import models

UserModel = get_user_model()


class CollectorProfile(models.Model):
    username = models.CharField(
        _('username'),
        max_length=20,
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
        upload_to='profile/%Y/%m/%d',
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

    def __str__(self):
        return self.username
