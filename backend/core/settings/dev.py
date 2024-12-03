from .base import *

INSTALLED_APPS.append("drf_spectacular")

REST_FRAMEWORK["DEFAULT_SCHEMA_CLASS"] = "drf_spectacular.openapi.AutoSchema"

ALLOWED_HOSTS = ["example.com", ".example.com", "localhost", "127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}


SPECTACULAR_SETTINGS = {
    "TITLE": "EWAREHOUSE API",
    "DESCRIPTION": "Test description",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_SETTINGS": {
        "persistAuthorization": True,  # Keeps token across sessions in Swagger UI
    },
    "COMPONENT_SPLIT_REQUEST": True,
    "COMPONENT_NO_REQUEST": False,
}
