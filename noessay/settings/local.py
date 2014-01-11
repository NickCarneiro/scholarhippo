import sys
globals().update(vars(sys.modules['noessay.settings']))

DEBUG = True
TEMPLATE_DIRS = ('/Users/burt/development/ne/templates',)
SECRET_KEY = '*wv)4a&amp;wd7cgf1v*8rbq2bhx8u^$a+i6s8l)nlt&amp;q@7%fb5veq'
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    'NAME': 'ne_search_dev',                      # Or path to database file if using sqlite3.
    'USER': 'noessay_dev',                      # Not used with sqlite3.
    'PASSWORD': 'SoySauce',                  # Not used with sqlite3.
    'HOST': 'noessay.com',                      # Set to empty string for localhost. Not used with sqlite3.
    'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

LOGGING['handlers']['file']['filename'] = '/var/log/noessay-dev.log'