bind = "127.0.0.1:8100"
daemon = False
debug = True
workers = 1
logfile = "/var/log/scholarhippo-gunicorn.log"
loglevel = "info"
procname = 'scholarhippo_prod'
pythonpath = "/var/www/scholarhippo_prod"
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'scholarhippo.settings'
import sys
sys.path.append("/var/www/scholarhippo_prod")
def when_ready(server):
    from django.core.management import call_command
    call_command('validate')

