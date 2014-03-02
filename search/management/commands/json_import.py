import datetime
from django.core.management.base import BaseCommand
import json
import lxml.html


class Command(BaseCommand):
    help = 'import scholarships from a json file'

    def handle(self, *args, **options):
        if len(args) != 1:
            print 'usage: python manage.py json_import filename.json'
            return
        file_path = args[0]
        f = open(file_path)
        scholarships = json.loads(f.read())
        i = 0
        for scholarship in scholarships:
            i += 1
            print scholarship['title']
            award_amount = self._extract_max_reward(scholarship['awards'])
            print 'award amount {}'.format(award_amount)
            print 'sponsor: {}'.format(scholarship['sponsor'])
            deadline = self._extract_deadline(scholarship['deadlines'])
            print 'deadline: {}'.format(deadline)
            print 'url: {}'.format(scholarship['url'])
            requirements = self._clean_html(scholarship['applicationRequirements'])
            print 'requirements: {}'.format(requirements)
            contact_info = self._clean_html(scholarship['contactInfo'])
            if '<script>' in contact_info or '<script>' in requirements:
                raise Exception('Found a script tag in the html!')


            if i > 10:
                break

    def _extract_max_reward(self, awards):
        """
        Takes an array like this: [u'Minimum:$1,000', u'Maximum:$10,000']
        or this: [u'Maximum:$1,000'] and returns an integer of USD
        """
        if len(awards) == 1:
            max_award_string = awards[0]
        elif len(awards) == 2:
            max_award_string = awards[1]
        else:
            raise Exception('got unexpected awards array', awards)
        max_award_string = max_award_string.replace('Maximum:$', '')
        max_award_string = max_award_string.replace(',', '')
        max_award_int = int(max_award_string)
        return max_award_int

    def _extract_deadline(self, deadlines):
        """
        input like '2/1', '7/1'
        assumes that all dates are in 2014
        """
        for deadline in deadlines:
            if 'Application deadline:' in deadline:
                #convert a string like '2/1' to a date object
                year = 2014
                date_string = deadline['Application deadline:']
                if date_string == '':
                    return None
                split_date = date_string.split('/')
                month = split_date[0]
                day = split_date[1]
                deadline = datetime.date(year, int(month), int(day))
                return deadline
        return None

    def _clean_html(self, html_string):
        """
        removes all classes but keeps dom structure
        """
        # Our html string we want to remove the class attribute from

        # Parse the html
        html = lxml.html.fromstring(html_string)

        # .xpath below gives us a list of all elements that have a class attribute
        # xpath syntax explained:
        # // = select all tags that match our expression regardless of location in doc
        # * = match any tag
        # [@class] = match all class attributes
        for tag in html.xpath('//*[@class]'):
            # For each element with a class attribute, remove that class attribute
            tag.attrib.pop('class')

        # Print out our "After"
        return lxml.html.tostring(html)
