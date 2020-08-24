"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('ENVIRONMENT') == "development"

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.herokuapp.com', '0.0.0.0', 'testserver' ]


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'backend.apps.BackendConfig',
    'api.apps.ApiConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graphene_django',
    'rest_framework',
    'rest_framework.authtoken',
    'anymail',
    'debug_toolbar',
]

GRAPHENE = {
    'SCHEMA': 'base.schema.schema' # Where your Graphene schema lives
}

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'backend/templates')],
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

WSGI_APPLICATION = 'base.wsgi.application'

# Celery
CELERY_BROKER_URL = 'amqp://%s:%s@rabbit:5672' % (os.environ.get('RABBITMQ_DEFAULT_USER'), os.environ.get('RABBITMQ_DEFAULT_PASS'))
CELERY_RESULT_BACKEND = 'redis://redis'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DEFAULT_DB'),
        'USER': os.environ.get('POSTGRES_DEFAULT_USER'),
        'PASSWORD': os.environ.get('POSTGRES_DEFAULT_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_DEFAULT_HOST'),
        'PORT': os.environ.get('POSTGRES_DEFAULT_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_THOUSAND_SEPARATOR=True

THOUSAND_SEPARATOR=','

DECIMAL_SEPARATOR='.'

NUMBER_GROUPING=3

ANYMAIL = {
    # (exact settings here depend on your ESP...)
    "MAILGUN_API_KEY": os.environ.get('MAILGUN_API_KEY'),
    "MAILGUN_SENDER_DOMAIN": os.environ.get('MAILGUN_SENDER_DOMAIN'),  # your Mailgun domain, if needed
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"  # or sendgrid.SendGridBackend, or...
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')  # if you don't already have this in settings

# You can use a shortcut version
TEMPLATED_EMAIL_BACKEND = 'templated_email.backends.vanilla_django'
TEMPLATED_EMAIL_FILE_EXTENSION = 'html'

# https://devcenter.heroku.com/articles/django-assets
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Location that collectstatic will store file
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser'
    ],
    # 'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

def show_toolbar(request):
    return DEBUG

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
}

AUTH_USER_MODEL = 'backend.User'

# jazzmin configuration
JAZZMIN_SETTINGS = {
    # title of the window
    'site_title': 'Base Admin',

    # Title on the brand, and the login screen (19 chars max)
    'site_header': 'Base Admin',

    # square logo to use for your site, must be present in static files, used for favicon and brand on top left
    # 'site_logo': 'https://via.placeholder.com/50x50.png?text=BDA',

    # Welcome text on the login screen
    'welcome_sign': 'Welcome to Base Django Administration',

    # Copyright on the footer
    'copyright': 'ICTS',

    # The model admin to search from the search bar, search bar omitted if excluded
    # 'search_model': 'auth.User',

    # Field name on user model that contains avatar image
    'user_avatar': None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    # 'topmenu_links': [

    #     # Url that gets reversed (Permissions can be added)
    #     {'name': 'Home',  'url': 'admin:index', 'permissions': ['auth.view_user']},

    #     # external url that opens in a new window (Permissions can be added)
    #     {'name': 'Support', 'url': 'https://github.com/farridav/django-jazzmin/issues', 'new_window': True},

    #     # model admin to link to (Permissions checked against model)
    #     {'model': 'auth.User'},

    #     # App with dropdown menu to all its models pages (Permissions checked against models)
    #     {'app': 'polls'},
    # ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ('app' url type is not allowed)
    # 'usermenu_links': [
    #     {'name': 'Support', 'url': 'https://github.com/farridav/django-jazzmin/issues', 'new_window': True},
    #     {'model': 'auth.user'}
    # ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    'show_sidebar': True,

    # Whether to aut expand the menu
    'navigation_expanded': True,

    # Hide these apps when generating side menu e.g (auth)
    'hide_apps': [],

    # Hide these models when generating side menu (e.g auth.user)
    'hide_models': [],

    # List of apps to base side menu ordering off of (does not need to contain all apps)
    'order_with_respect_to': ['accounts', 'polls'],

    # Custom links to append to app groups, keyed on app name
    'custom_links': {
        'polls': [{
            'name': 'Make Messages',
            'url': 'make_messages',
            'icon': 'fas fa-comments',
            'permissions': ['polls.view_poll']
        }]
    },

    # Custom icons for side menu apps/models See https://www.fontawesomecheatsheet.com/font-awesome-cheatsheet-5x/
    # for a list of icon classes
    'icons': {
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',
    },
    # Icons that are used when one is not manually specified
    'default_icon_parents': 'fas fa-chevron-circle-right',
    'default_icon_children': 'fas fa-circle',

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs",},
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-info",
    "accent": "accent-info",
    "navbar": "navbar-cyan navbar-dark",
    "no_navbar_border": False,
    "sidebar": "sidebar-light-info",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False
}