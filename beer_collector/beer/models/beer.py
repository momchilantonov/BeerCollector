from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from beer_collector.beer.models.beer_style import BeerStyle

UserModel = get_user_model()


class Beer(models.Model):
    label = models.CharField(
        _('beer label'),
        max_length=30,
    )
    type = models.ForeignKey(
        BeerStyle,
        on_delete=models.CASCADE,
    )
    description = models.CharField(
        _('beer description'),
        max_length=300,
        blank=True,
        null=True,
    )
    image = models.ImageField(
        _('beer image'),
        upload_to='beers',
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class BeerLike(models.Model):
    beer = models.ForeignKey(
        Beer,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class BeerComment(models.Model):
    comment = models.TextField(
        blank=True,
        null=True,
    )
    beer = models.ForeignKey(
        Beer,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
