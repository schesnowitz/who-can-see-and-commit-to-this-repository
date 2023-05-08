from pathlib import Path
import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# False if not in os.environ because of casting above
DEBUG = env('DEBUG')
# DEBUG = True
print(DEBUG)
SECRET_KEY = env('SECRET_KEY')
# SECRET_KEY = 'asdfasdfasdf'

CSRF_TRUSTED_ORIGINS = ["https://*.https://chesnowitz.herokuapp.com/", "https://*.chesnowitz.com"]
ALLOWED_HOSTS = ["http://localhost:8000/","127.0.0.1", "chesnowitz.herokuapp.com", "localhost", "www.chesnowitz.com", "chesnowitz.com"]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    "whitenoise.runserver_nostatic",
    "accounts.apps.AccountsConfig",
    'projects',
    'aiposts',
    'django_extensions',
    'ckeditor',
    'allauth',
    'allauth.account',
    # 'allauth.socialaccount',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env('PGDATABASE'), 
        "USER": env('PGUSER'),
        "PASSWORD": env('PGPASSWORD'),
        "HOST": env('PGHOST'),
        "PORT": env('PGPORT'),
    }
}





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
TIME_ZONE = 'EST'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles" 
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# python manage.py collectstatic
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "project_list"
LOGOUT_REDIRECT_URL = "project_list"

# allauth settings
AUTH_USER_MODEL = "accounts.CustomUser"
SITE_ID = 1
ACCOUNT_FORMS = {'signup': 'accounts.forms.CustomUserCreationForm'}

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True

# mail settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_HOST_USER = "apikey"
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_API_KEY')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# print(EMAIL_HOST_PASSWORD)
AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    
]

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar_MyCustomToolbar': [
            {'name': 'basic', 'items': [
                'Source',
                '-',
                'Bold',
                'Italic',
                'CodeSnippet'  # add the codesnippet button name
            ]}
        ],

        'codeSnippet_theme': 'monokai',
        # uncomment to restrict only those languages
        'codeSnippet_languages': {
            'python': 'Python',
        },
        'toolbar': 'MyCustomToolbar',
        'extraPlugins': ','.join(
            [
                # add the follow plugins
                'codesnippet',
                # 'widget',
                # 'dialog',
            ]),
    }
}



