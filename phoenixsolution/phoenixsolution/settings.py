from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _  # Import necesario para traducciones

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-0qx1e2z1-lfvd*axbg88tlg!a$zv04uzjqkz+2q&7m1d(6npih"

DEBUG = True

CSRF_TRUSTED_ORIGINS = [
    'https://localhost:8000',
    'http://127.0.0.1:8000',
    "https://urban-space-enigma-5xwg5x7g9gx2vqwp-8000.app.github.dev",
    "https://phoenix-solution-webpage.onrender.com"
]

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "urban-space-enigma-5xwg5x7g9gx2vqwp-8000.app.github.dev",
    "phoenix-solution-webpage.onrender.com",
    "*",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "website",
    "modeltranslation"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",  # 📌 Agregado para cambiar idiomas dinámicamente
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "phoenixsolution.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",  # 📌 Importante para cambiar el idioma dinámicamente
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "phoenixsolution.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

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

# 📌 Configuración de idioma
LANGUAGE_CODE = "es"  # Idioma por defecto

LANGUAGES = [
    ("es", _("Español")),
    ("en", _("English")),
]

# 📌 Ruta donde Django buscará las traducciones
LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

TIME_ZONE = "UTC"

USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'octavioriv02@gmail.com'
EMAIL_HOST_PASSWORD = 'ybjyrbicwnmhkhee'
EMAIL_USE_TLS = True

LANGUAGE_COOKIE_NAME = "django_language"  # 📌 Guarda el idioma seleccionado en una cookie
