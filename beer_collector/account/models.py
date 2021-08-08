from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from beer_collector.account.managers import CustomAccountManager


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _('email address'),
        max_length=60,
        unique=True,
    )
    date_joined = models.DateTimeField(
        _('date joined'),
        auto_now_add=True,
    )
    last_login = models.DateTimeField(
        _('last login'),
        auto_now=True,
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
    )
    is_staff = models.BooleanField(
        _('staff'),
        default=False,
    )
    is_superuser = models.BooleanField(
        _('superuser'),
        default=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomAccountManager()
