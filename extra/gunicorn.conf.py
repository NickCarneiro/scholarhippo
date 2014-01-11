bind = "127.0.0.1:8094"
daemon = False
debug = True
workers = 1
logfile = "/var/log/noessay-gunicorn.log"
loglevel = "info"
procname = 'noessay_prod'
pythonpath = "/var/www/noessay_prod"
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'noessay.settings'
import sys
sys.path.append("/var/www/ne_prod")
def when_ready(server):
    from django.core.management import call_command
    call_command('validate')

