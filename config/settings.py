import os
from urllib.request import CacheFTPHandler
from django.urls import reverse_lazy

def get_secret(settings):
    try:
        return os.environ[settings]
    except ValueError as key_e:
        key_e(f'В окружении нет такой переменной {settings}')




BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



DEBUG = True



if DEBUG:
    ALLOWED_HOSTS = ['*']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    
    INTERNAL_IPS = ["127.0.0.1",]

    # EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    # EMAIL_HOST = "localhost"

else:
    ALLOWED_HOSTS = ['192.168.2.64']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': get_secret('DATABASE_NAME'),
            'USER': get_secret('DATABASE_USER'),
            'PASSWORD': get_secret('DATABASE_PASSWORD'),
            'HOST': 'db',
            'PORT': '5432',
        }
    }
    
    
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT =  465
EMAIL_HOST_USER = get_secret('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_secret('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CONN_MAX_AGE = 60


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": get_secret('REDIS_PASSWORD')
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"





TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media'

                
            ],
        },
    },
]

STATICFILES_DIRS = [
        os.path.join( BASE_DIR, 'static'),
    ]
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


SECRET_KEY = get_secret('SECRET_KEY')


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainapp.apps.MainappConfig',
    "bootstrap5",
    'authapp.apps.AuthappConfig',
    'imagekit',
    "debug_toolbar",




]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'


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




LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = "authapp.User"
LOGOUT_REDIRECT_URL = '/'

CACHE_TIME = 300


CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"