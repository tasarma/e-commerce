import pytest
from rest_framework.exceptions import ValidationError

from users.models import CustomUser
from users.serializers import CustomUserSerializer, ProfileSerializer
from tenant.models import Tenant  # Import Tenant model


@pytest.mark.django_db
class TestCustomUserSerializer:
    @pytest.fixture(autouse=True)
    def setup_data(self):
        self.tenant = Tenant.objects.create(name="Test Tenant", subdomain="test-tenant")

    def test_valid_serializer(self):
        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "password": "123465",
            "gln": "",
            "phone_number": "",
            "address": "",
            "tenant": self.tenant.id,
        }
        serializer = CustomUserSerializer(data=user_data)
        assert serializer.is_valid()
        assert serializer.validated_data["email"] == "john.doe@example.com"

    def test_invalid_email(self):
        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "",
            "password": "123465",
            "gln": "1234567890123",
            "phone_number": "1234567890",
            "address": "123 Main St",
            "tenant": self.tenant.id,
        }
        serializer = CustomUserSerializer(data=user_data)
        assert not serializer.is_valid()
        assert "email" in serializer.errors

    # def test_missing_tenant(self):
    #     user_data = {
    #         "first_name": "John",
    #         "last_name": "Doe",
    #         "email": "john.doe@example.com",
    #         "gln": "1234567890123",
    #         "phone_number": "1234567890",
    #         "address": "123 Main St",
    #         "tenant": None,
    #     }
    #     serializer = CustomUserSerializer(data=user_data)
    #     assert not serializer.is_valid()
    #     assert "tenant" in serializer.errors


@pytest.mark.django_db
class TestProfileSerializer:
    def test_valid_profile_serializer(self):
        user = CustomUser.objects.create(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com",
            gln="1234567890123",
            phone_number="0987654321",
            address="456 Elm St",
            tenant=None,
        )
        serializer = ProfileSerializer(instance=user)
        assert serializer.data["email"] == "jane.doe@example.com"

    def test_profile_serializer_update(self):
        user = CustomUser.objects.create(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com",
            gln="1234567890123",
            phone_number="0987654321",
            address="456 Elm St",
            tenant=None,
        )
        update_data = {
            "first_name": "Janet",
            "last_name": "Doe",
            "email": "janet.doe@example.com",
        }
        serializer = ProfileSerializer(instance=user, data=update_data, partial=True)
        assert serializer.is_valid()
        updated_user = serializer.save()
        assert updated_user.first_name == "Janet"
        assert updated_user.email == "janet.doe@example.com"
