"""
Django settings for polaris project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

# Store the dictionary in a variable
bool_dict = {"true": True, "false": False}

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool_dict.get(os.getenv("DEBUG", "False").lower())

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "http://127.0.0.1:8000").split(",")

# Application definition

INSTALLED_APPS = [
    # Default
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Plugin
    "corsheaders",
    "rest_framework",
    "drf_spectacular",
    # Apps
    "account",
    "inventory",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Plugin
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "polaris.urls"

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

WSGI_APPLICATION = "polaris.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# The model to use to represent a User
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-user-model

AUTH_USER_MODEL = "account.User"

# Cache
# https://docs.djangoproject.com/en/5.0/ref/settings/#caches

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PARSER_CLASS": "redis.connection._HiredisParser",  # Use hiredis parser
        },
    }
}

# Login
# https://docs.djangoproject.com/en/5.0/ref/settings/#login-url

LOGIN_URL = "/api/v1/accounts/login"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
    },
    # 'loggers': {
    #     'django.db.backends': {
    #         'handlers': ['console'],
    #         'level': 'DEBUG',
    #     },
    # },
}

# Using cached sessions
# https://docs.djangoproject.com/en/5.0/ref/settings/#session-engine

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
# Admin Login
SESSION_COOKIE_AGE = 86400  # 2 day in seconds
# Api Login
AUTH_TOKEN_TTL = 86400  # 2 day in seconds

# CSRF Cookie
# https://docs.djangoproject.com/en/5.0/ref/settings/#csrf-cookie-samesite

# The value of the SameSite flag on the CSRF cookie.
# This flag prevents the cookie from being sent in cross-site requests.
CSRF_COOKIE_SAMESITE = os.getenv("COOKIE_SAMESITE", "Lax")  # Default: 'Lax'

# Whether to use a secure cookie for the CSRF cookie.
# If this is set to True, the cookie will be marked as “secure”,
# which means browsers may ensure that the cookie is only sent with an HTTPS connection.
CSRF_COOKIE_SECURE = bool_dict.get(os.getenv("COOKIE_SECURE", "False").lower())  # Default: False

# Session Cookie
# https://docs.djangoproject.com/en/5.0/ref/settings/#session-cookie-samesite

# The value of the SameSite flag on the session cookie.
# This flag prevents the cookie from being sent in cross-site requests
# thus preventing CSRF attacks and making some methods of stealing session cookie impossible.
SESSION_COOKIE_SAMESITE = os.getenv("COOKIE_SAMESITE", "Lax")  # Default: 'Lax'

# Whether to use a secure cookie for the session cookie.
# If this is set to True, the cookie will be marked as “secure”,
# which means browsers may ensure that the cookie is only sent under an HTTPS connection.
SESSION_COOKIE_SECURE = bool_dict.get(os.getenv("COOKIE_SECURE", "False").lower())  # Default: False

# Cors
# https://github.com/adamchainz/django-cors-headers

CORS_ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://127.0.0.1:8000").split(",")

CORS_ALLOW_METHODS = (
    "OPTIONS",
    "GET",
    "POST",
    "PATCH",
    "PUT",
    "DELETE",
)

# If True, cookies will be allowed to be included in cross-site HTTP requests.
# This sets the Access-Control-Allow-Credentials header in preflight and normal responses.
CORS_ALLOW_CREDENTIALS = bool_dict.get(os.getenv("CORS_ALLOW_CREDENTIALS", "False").lower())  # Default: False

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "services.auth.CacheTokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_RENDERER_CLASSES": [
        "services.renderer.CustomJSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "services.pagination.CustomPageNumberPagination",
    "PAGE_SIZE": 25,
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Polaris API",
    "DESCRIPTION": "Polaris API",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}
