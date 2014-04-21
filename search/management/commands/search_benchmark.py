import datetime
from django.core.management import BaseCommand
import requests


class Command(BaseCommand):
    def handle(self, *args, **options):
        if len(args) == 1:
            host = args[0]
        else:
            host = 'localhost:5000'
        base_url = 'http://{}'.format(host)

        urls = ['/search?q=engineering&l=US&ne=false&e=2&g=', # q=engineering ethnicity=black
                '/search?q=&l=US',  # blank q, blank l
                '/search?q=engineering&l=US&ne=true&e=&g=',  # engineering, essay_required=false
                '/search?q=science&l=US&ne=false&e=&g=1',  # science, female
                '/search?q=science&l=US',  # science
                '/search?q=biology&l=US'  # biology
                ]
        total_time = 0
        for url in urls:
            test_url = base_url + url
            print test_url
            start_time = datetime.datetime.now()
            r = requests.get(test_url)
            end_time = datetime.datetime.now()
            elapsed_time = end_time - start_time
            elapsed_time_millis = elapsed_time.microseconds / 1000.0
            print 'elapsed time: {}'.format(elapsed_time_millis)
            total_time += elapsed_time_millis

        print 'total: {}'.format(total_time)
