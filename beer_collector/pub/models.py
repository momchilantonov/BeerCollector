from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class Pub(models.Model):
    name = models.CharField(
        _('pub name'),
        max_length=30,
    )
    address = models.CharField(
        _('pub address'),
        max_length=60,
        blank=True,
        null=True,
    )
    description = models.CharField(
        _('pub description'),
        max_length=300,
        blank=True,
        null=True,
    )
    image = models.ImageField(
        _('pub image'),
        upload_to='pubs/%Y/%m/%d',
        blank=True,
        null=True,
    )
    longitude = models.DecimalField(
        _('longitude'),
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
    )
    latitude = models.DecimalField(
        _('latitude'),
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class PubLike(models.Model):
    pub = models.ForeignKey(
        Pub,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class PubComment(models.Model):
    comment = models.TextField(
        blank=True,
        null=True,
    )
    pub = models.ForeignKey(
        Pub,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
