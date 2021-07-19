from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db import models

UserModel = get_user_model()


class CollectorProfile(models.Model):
    image = models.ImageField(
        _('image'),
        upload_to='profile/%Y/%m/%d',
        blank=True,
    )
    about = models.TextField(
        _('about'),
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
