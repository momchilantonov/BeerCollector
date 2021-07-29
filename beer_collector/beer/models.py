from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db import models

UserModel = get_user_model()


class BeerStyle(models.Model):
    type = models.CharField(
        _('beer type'),
        max_length=20,
        blank=True,
        null=True,
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


class Beer(models.Model):
    label = models.CharField(
        _('beer label'),
        max_length=60,
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
        upload_to='beer/%Y/%m/%d',
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.label


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
