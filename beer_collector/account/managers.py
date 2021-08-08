from django.contrib.auth.base_user import BaseUserManager


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
