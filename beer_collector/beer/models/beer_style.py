from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class BeerStyle(models.Model):
    type = models.CharField(
        _('beer type'),
        max_length=30,
    )
    description = models.CharField(
        _('description'),
        max_length=300,
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.type


class BeerStyleLike(models.Model):
    beer_style = models.ForeignKey(
        BeerStyle,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class BeerStyleComment(models.Model):
    comment = models.TextField(
        blank=True,
        null=True,
    )
    beer_style = models.ForeignKey(
        BeerStyle,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
