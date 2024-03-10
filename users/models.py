from typing import Any

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str | None = None):
        if email is None:
            raise TypeError('Необходимо указать почту')

        user: Any = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email: str, password: str | None = "123"):
        user: Any = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

