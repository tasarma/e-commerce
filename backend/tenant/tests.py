import pytest

from django.db import IntegrityError
from django.db import models

from .models import Tenant, TenantAwareModel


@pytest.mark.django_db
class TestTenantModel:
    @pytest.fixture(autouse=True)
    def setup_tenant(self):
        self.tenant = Tenant.objects.create(name="Test Tenant", subdomain="test-tenant")

    def test_create_tenant(self):
        assert self.tenant.name == "Test Tenant"
        assert self.tenant.subdomain == "test-tenant"

    def test_unique_subdomain(self):
        Tenant.objects.create(name="Tenant 1", subdomain="unique-subdomain")
        with pytest.raises(IntegrityError):
            Tenant.objects.create(name="Tenant 2", subdomain="unique-subdomain")

    def test_tenant_str_method(self):
        assert str(self.tenant) == "Test Tenant"


@pytest.mark.django_db
class TestTenantAwareModel:
    def test_tenant_aware_model_abstract(self):
        assert TenantAwareModel._meta.abstract is True

    def test_tenant_field_exists(self):
        tenant_field = TenantAwareModel._meta.get_field("tenant")
        assert isinstance(tenant_field, models.ForeignKey)
        assert tenant_field.remote_field.model == Tenant
        assert tenant_field.remote_field.on_delete == models.CASCADE
