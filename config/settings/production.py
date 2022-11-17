from .base import *
import os
import environ
from decouple import config
from dj_database_url import parse as dburl

DEBUG = False

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))


# INSTALLED_APPS += [
#     "debug_toolbar",
#     "drf_spectacular",
#     "django_extensions",
# ]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
SECRET_KEY = env("SECRET_KEY")
SUPERUSER_NAME = env("SUPERUSER_NAME")
SUPERUSER_EMAIL = env("SUPERUSER_EMAIL")
SUPERUSER_PASSWORD = env("SUPERUSER_PASSWORD")

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # 追加
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

default_dburl = "sqlite:///" + str(BASE_DIR / "db.sqlite3")

DATABASES = {
    "default": config("DATABASE_URL", default=default_dburl, cast=dburl),
}


# REST_FRAMEWORK = {
#     # # "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
#     # "DEFAULT_PERMISSION_CLASSES": [
#     #     "rest_framework.permissions.IsAuthenticated",
#     # ],
#     # "DEFAULT_AUTHENTICATION_CLASSES": (
#     #     # "rest_framework.authentication.SessionAuthentication",
#     #     # "rest_framework.authentication.BasicAuthentication"
#     #     # "rest_framework.authentication.TokenAuthentication",
#     #     "rest_framework_simplejwt.authentication.JWTAuthentication",
#     # ),
#     # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
#     # "PAGE_SIZE": 10,
# }

CORS_ORIGIN_WHITELIST = [
    #     "http://localhost:3000",
]


ALLOWED_HOSTS = [
    "example.com",
]