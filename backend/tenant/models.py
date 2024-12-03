from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=255)
    subdomain = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta:
        """
        To make the model an abstract base class, meaning it won't create a table in the DB,
        but its fields will be included in any model that inherits from it.
        """

        abstract = True
