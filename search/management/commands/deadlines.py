from django.core.management.base import BaseCommand
from search.models import Scholarship


class Command(BaseCommand):
    help = 'produce csv for histogram of scholarship deadlines'

    def handle(self, *args, **options):
        scholarships = Scholarship.objects.all()
        deadlines = {}
        for scholarship in scholarships:
            if scholarship.deadline:
                deadline = str(scholarship.deadline).replace('2013', '2014')
                if deadline in deadlines:
                    deadlines[deadline] += 1
                else:
                    deadlines[deadline] = 1
            if scholarship.deadline2:
                deadline = str(scholarship.deadline2).replace('2013', '2014')
                if deadline in deadlines:
                    deadlines[deadline] += 1
                else:
                    deadlines[deadline] = 1
            if scholarship.deadline3:
                deadline = str(scholarship.deadline3).replace('2013', '2014')
                if deadline in deadlines:
                    deadlines[deadline] += 1
                else:
                    deadlines[deadline] = 1
        print 'deadline, count'
        for deadline in deadlines:
            print '{}, {}'.format(deadline, deadlines[deadline])