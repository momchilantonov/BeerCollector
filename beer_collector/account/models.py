from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None, ):
        if not email:
            raise ValueError('You must provide an email.')

        if not username:
            raise ValueError('You must provide username.')

        if not first_name:
            raise ValueError('You must provide first name.')

        if not last_name:
            raise ValueError('You must provide last name.')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, first_name, last_name, password=None, ):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
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
    username = models.CharField(
        _('username'),
        max_length=20,
        unique=True,
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
    registration_date = models.DateTimeField(
        _('registration date'),
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
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = CustomAccountManager()

    def __str__(self):
        return self.username
