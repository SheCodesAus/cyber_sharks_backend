"""
Django settings for cyber_sharks_backend project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv
from django.conf import settings

# Load environment variables from the .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "lr_js@m*jugt(77-o+31kjz6kd9w3(b1zpf=4x(^x26=^czg**",  # is a signature to prevent bad people to get in your website
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG") != "False"

ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
    "users.apps.UsersConfig",
    "search.apps.SearchConfig",
    "locations.apps.LocationsConfig",
    "portfolio.apps.PortfolioConfig",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "EXCEPTION_HANDLER": "rest_framework.views.exception_handler",
}

AUTH_USER_MODEL = "users.CustomUser"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "storages"
]

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "access_key": os.environ.get("AWS_ACCESS_KEY_ID"),
            "secret_key": os.environ.get("AWS_SECRET_ACCESS_KEY"),
            "bucket_name": "shecodes-cyber-sharks",
            "region_name": "us-east-1",
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "access_key": os.environ.get("AWS_ACCESS_KEY_ID"),
            "secret_key": os.environ.get("AWS_SECRET_ACCESS_KEY"),
            "bucket_name": "shecodes-cyber-sharks",
            "region_name": "us-east-1",
        },
    },
}


ROOT_URLCONF = "cyber_sharks_backend.urls"

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

WSGI_APPLICATION = "cyber_sharks_backend.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        'OPTIONS': {
            'timeout': 20,  # Increase timeout to 20 seconds
        }
    }
}
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# AWS S3 settings
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = 'shecodes-cyber-sharks'
AWS_S3_REGION_NAME = 'us-east-1'
AWS_DEFAULT_ACL = None  # Optional, controls default permissions for uploaded files

# Use S3 for storing media files
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Media URL will point to the S3 URL
MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com/'
