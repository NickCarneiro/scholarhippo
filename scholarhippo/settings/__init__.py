# Django settings for noessay project.
import os
import sys
base = os.path.dirname(os.path.dirname(__file__))
base_parent = os.path.dirname(base)
sys.path.append(base)
sys.path.append(base_parent)
ADMINS = (
# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'scholarhippo',                      # Or path to database file if using sqlite3.
            'USER': 'noessay_dev',                      # Not used with sqlite3.
            'PASSWORD': 'SoySauce',                  # Not used with sqlite3.
            'HOST': 'noessay.com',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
}
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

ROOT_URLCONF = 'scholarhippo.urls'



INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'django.contrib.humanize',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'search',
    'helper',
    'south',
    'raven.contrib.django.raven_compat',
    'report',
    'aggcentral'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    #    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)


#elasticsearch settings
ES_INDEX = 'noessay-prod'
SCHOLARSHIP_TYPE = 'scholarship'

ALLOWED_HOSTS = [
    'scholarhippo.com',
    '.scholarhippo.com',
    ]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/scholarhippo-prod.log',
            },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console', 'file'],
            'level': 'ERROR',
            'propagate': True,
            },
        },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    }
}

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'scholarhippo.wsgi.application'
# DEBUG = False

ES_INDEX = 'noessay-dev'
ENVIRONMENT = 'dev'

STATIC_URL = '/static/'
SECRET_KEY = 'oh god I did not know we needed this!'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

LOGIN_URL = '/admin'

try:
    from .local import *
except ImportError:
    print 'no local settings found'
    pass
