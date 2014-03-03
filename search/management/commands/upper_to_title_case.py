from django.core.management import BaseCommand
from search.models import Scholarship


class Command(BaseCommand):
    help = 'look for all caps scholarship titles and convert to title case'

    def handle(self, *args, **options):
        scholarships = Scholarship.objects.all()
        i = 0
        upper_count = 0
        for scholarship in scholarships:
            if scholarship.title.isupper():
                print scholarship.title
                title_case_title = scholarship.title.title()
                print title_case_title
                scholarship.title = title_case_title
                scholarship.save()
                upper_count += 1
                # remove 'Scholarships for College'
            elif ' - Scholarships for College' in scholarship.title:
                print 'removing  - Scholarships for College'
                scholarship.title = scholarship.title.replace(' - Scholarships for College', '')
                scholarship.save()
            i += 1
            print '{} / {} uppers: {}'.format(i, len(scholarships), upper_count)