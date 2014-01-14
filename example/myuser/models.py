from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from tenancy.models import AbstractTenant, TenantModel

class TenantUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        return self.create_user(email, password, is_superuser=True)


class TenantUser(TenantModel, AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)

    objects = TenantUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        app_label = 'tenancy'

    class TenantMeta:
        related_name = 'users'