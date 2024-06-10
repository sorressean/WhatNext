"""
Django settings for WhatNext project.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
DEBUG = env("DEBUG")
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = env("ALLOWED_HOSTS", cast=[str])
# Application definition

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "crispy_forms",
    "crispy_bootstrap5",
    "bootstrap5",
    "portal",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "portal.middlewares.set_secure_headers",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "cid.context_processors.cid_context_processor",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "WhatNext.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": env.db(),
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
APPEND_SLASH = False
CID_GENERATE = True

LOGGING = {
    "version": 1,
    "formatters": {
        "verbose": {"format": "[cid: %(cid)s] %(levelname)s %(asctime)s %(module)s %(message)s"},
        "simple": {"format": "[cid: %(cid)s] %(levelname)s %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "filters": {},
    "loggers": {
        "portal": {
            "handlers": ["console"],
            "filters": [],
            "propagate": True,
        },
        "root": {
            "handlers": ["console"],
            "level": "WARNING",
        },
    },
}

CACHES = {
    "default": {
        "BACKEND": env("CACHE_BACKEND"),
        "LOCATION": env("CACHE_LOCATION"),
    },
}

CSRF_TRUSTED_ORIGINS = env("CSRF_TRUSTED_ORIGINS", cast=[str])
EMAIL_HOST = env("EMAIL_HOST", cast=str)
EMAIL_PORT = env("EMAIL_PORT", cast=int)
EMAIL_HOST_USER = env("EMAIL_HOST_USER", cast=str)
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", cast=str)
EMAIL_USE_SSL = True
CELERY_BROKER_URL = env("CELERY_BROKER_URL", cast=str)
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND", cast=str)

if DEBUG is True:
    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE.insert(2, "debug_toolbar.middleware.DebugToolbarMiddleware")
    DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": "taskmgr.debug.toolbarcallback"}
