from django.db import models
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import AbstractUser

from tenant.models import Tenant

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(gettext_lazy("email address"), unique=True)
    gln = models.CharField(max_length=13, blank=True, null=True, unique=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    tenant = models.ForeignKey(
        Tenant,
        related_name="users",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
