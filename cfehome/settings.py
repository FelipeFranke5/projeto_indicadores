import os
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured
from dotenv import dotenv_values

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

if not os.path.exists("secret.env"):
    raise ImproperlyConfigured(
        "A chave secreta em 'SECRET_KEY' é obrigatória! "
        "Crie um arquivo com nome 'secret.env' e armazene a "
        "credencial SECRET_KEY em uma variável de ambiente."
    )

arquivo_secret_key = dotenv_values("secret.env")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = arquivo_secret_key["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "backend",
    "frontend",
    "rest_framework",
    "rest_framework.authtoken",
    "accounts",
    "widget_tweaks",
    "django_recaptcha",
    "django_bootstrap5",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "cfehome.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "cfehome.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

if not os.path.exists("db.env"):
    raise ImproperlyConfigured(
        "O arquivo 'db.env' contendo as variáveis de ambiente relacionadas ao Banco de Dados está ausente. "
        "Por favor, crie esse arquivo na pasta do projeto e defina os parâmetros: "
        "NAME -- USER -- PASSWORD -- HOST -- PORT."
    )

arquivo_db = dotenv_values("db.env")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": arquivo_db["NAME"],
        "USER": arquivo_db["USER"],
        "PASSWORD": arquivo_db["PASSWORD"],
        "HOST": arquivo_db["HOST"],
        "PORT": arquivo_db["PORT"],
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

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

API_BASE_URL = "http://127.0.0.1:8000"
LOGIN_REDIRECT_URL = "main:main"
LOGOUT_REDIRECT_URL = "accounts:login"
LOGIN_URL = "accounts:login"

# Chaves para o reCaptcha
# Criar as chaves no arquivo 'chaves.env'

if not os.path.exists("chaves.env"):
    raise ImproperlyConfigured(
        "Para esse projeto, é necessário obter as chaves do Google Recaptcha. "
        "Por favor, acesse o site do Google Recaptcha, cadastre as chaves "
        "PUBLIC_KEY e PRIVATE_KEY, em seguida registre elas em variáveis "
        "de ambiente, dentro do arquivo 'chaves.env'."
    )

arquivo_chaves_recaptcha = dotenv_values("chaves.env")
RECAPTCHA_PUBLIC_KEY = arquivo_chaves_recaptcha["RECAPTCHA_PUBLIC_KEY"]
RECAPTCHA_PRIVATE_KEY = arquivo_chaves_recaptcha["RECAPTCHA_PRIVATE_KEY"]
