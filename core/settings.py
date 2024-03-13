from .cdn.conf import(
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_ENDPOINT,
    AWS_STORAGE_BUCKET_NAME,
    AWS_ENDPOINT_URL,
    AWS_S3_OBJECT_PARAMETERS,
    DEFAULT_FILE_STORAGE,
    STATICFILES_STORAGE,
)
from pathlib import Path
import os
import logging
import environ
from datetime import timedelta
import dj_database_url
import sys
from dotenv import load_dotenv

env = environ.Env()
environ.Env.read_env()

ENVIRONMENT = env

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()


SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

DOMAIN = os.environ.get('DOMAIN')


ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

WEBSITE_URL = os.environ.get('WEBSITE_URL')


DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

APPS = [
    'apps.users',
    'apps.authentication',
    'apps.general',
    'apps.video',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'storages',
]

INSTALLED_APPS = DJANGO_APPS + APPS + THIRD_PARTY_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
SITE_ID = 1

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-width',
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGINS = [
    f"https://{WEBSITE_URL}",
    f"http://{WEBSITE_URL}",
    f"http://localhost:8000",
    f"http://127.0.0.1:8000",

]
CSRF_TRUSTED_ORIGINS = [
    f"https://{WEBSITE_URL}",
    f"http://{WEBSITE_URL},"
]

SESSION_COOKIE_DOMAIN = WEBSITE_URL

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True

SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# database setup
if DEBUG is True:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
}
elif len(sys.argv) > 0 and sys.argv[1] != "collectstatic":
    if os.getenv("DATABASE_URL", None) is None:
        raise Exception("DATABASE_URL environment variable not defined")
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
    }
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'

# POSTGRES_DB = os.environ.get("POSTGRES_DB")
# POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
# POSTGRES_USER = os.environ.get("POSTGRES_USER")
# POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
# POSTGRES_PORT = os.environ.get("POSTGRES_PORT")


# POSTGRES_READY = (
#     POSTGRES_DB is not None
#     and POSTGRES_PASSWORD is not None
#     and POSTGRES_USER is not None
#     and POSTGRES_HOST is not None
#     and POSTGRES_PORT is not None
# )


# if POSTGRES_READY:
#     DATABASES = {
#         "default": {
#             'ENGINE': 'django.db.backends.postgresql',
#             "NAME": POSTGRES_DB,
#             "USER": POSTGRES_USER,
#             "PASSWORD": POSTGRES_PASSWORD,
#             "HOST": POSTGRES_HOST,
#             "PORT": POSTGRES_PORT,
#         }
#     }


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# STATIC
DATA_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 3000
FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 3000


AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME = AWS_STORAGE_BUCKET_NAME
AWS_S3_ENDPOINT_URL = AWS_ENDPOINT_URL
AWS_S3_OBJECT_PARAMETERS = AWS_S3_OBJECT_PARAMETERS
AWS_LOCATION = AWS_STORAGE_BUCKET_NAME
AWS_QUERYSTRING_EXPIRE = 5

STATIC_URL = '/static/'
MEDIA_URL = '/media/'



STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"
STATICFILES_DIR = [os.path.join(BASE_DIR, "static")]

MEDIA_DIR = BASE_DIR / 'media'
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

STORAGES = {
    
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_URL = 'https://%s/%s/' % (AWS_ENDPOINT, AWS_LOCATION)
MEDIA_URL = 'https://%s/%s/' % (AWS_ENDPOINT, AWS_LOCATION)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
MEDIAFILES_DIRS = [
    os.path.join(BASE_DIR, 'media'),
]

STATICFILES_STORAGE = STATICFILES_STORAGE
DEFAULT_FILE_STORAGE = DEFAULT_FILE_STORAGE

AWS_ENABLED = True
AWS_S3_SECURE_URLS = True


# rest-faramework

REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "rest_framework.views.exception_handler",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
}


SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT', ),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10080),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'ROTATE_REFRESFH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_TOKEN_CLASSES': (
        'rest_framework_simplejwt.tokens.AccessToken',
    )
}


# cors

FRONTEND_IP = os.environ.get('FRONTEND_IP')
FRONTEND = os.environ.get('FRONTEND')
BACKEND_IP = os.environ.get('BACKEND_IP')
BACKEND = os.environ.get('BACKEND')

CORS_ORIGIN_WHITELIST = [
    FRONTEND,
    FRONTEND_IP,
    BACKEND,
    BACKEND_IP,
]

CSRF_TRUSTED_ORIGINS = [
    FRONTEND,
    FRONTEND_IP,
    BACKEND,
    BACKEND_IP,
]

CORS_ALLOWED_ORIGINS = [
    FRONTEND,
    FRONTEND_IP,
    BACKEND,
    BACKEND_IP,
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "users.User"


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}