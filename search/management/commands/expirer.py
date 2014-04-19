# expires scholarships
from django.core.management import BaseCommand
from search.operations.expiration_checker import expire


class Command(BaseCommand):
    help = 'checks for dead links and marks scholarships as expired'

    def handle(self, *args, **options):
        expire()