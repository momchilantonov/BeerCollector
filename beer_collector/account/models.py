import os

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from beer_collector.core.views import get_obj_by_pk


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('You must provide an email.')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


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

    def __str__(self):
        return self.email
