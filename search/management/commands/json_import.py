import datetime
from django.core.management.base import BaseCommand
import json
import lxml.html
import sys
from search.models import Scholarship


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
        dupe_count = 0
        for scholarship in scholarships:
            i += 1
            print scholarship['title']
            award_amount = self._extract_max_reward(scholarship['awards'])
            deadline = self._extract_deadline(scholarship['deadlines'])
            requirements = self._clean_html(scholarship['applicationRequirements'])
            high_school_eligible = self._is_high_school_eligible(scholarship['uses'])
            undergraduate_eligible = self._is_undergraduate_eligible(scholarship['uses'])
            graduate_eligible = self._is_graduate_eligible(scholarship['uses'])
            is_essay_required = self._is_essay_required(requirements)
            contact_info = self._clean_html(scholarship['contactInfo'])
            if '<script>' in contact_info or '<script>' in requirements:
                raise Exception('Found a script tag in the html!')

            scholarship_model = Scholarship()
            scholarship_model.title = scholarship['title']
            scholarship_model.amount_usd = award_amount
            scholarship_model.essay_required = is_essay_required
            scholarship_model.organization = scholarship['sponsor']
            scholarship_model.street_address = contact_info
            scholarship_model.third_party_url = scholarship['url']
            scholarship_model.high_school_eligible = high_school_eligible
            scholarship_model.undergrad_eligible = undergraduate_eligible
            scholarship_model.graduate_eligible = graduate_eligible
            scholarship_model.description = requirements
            scholarship_model.deadline = deadline

            if self._is_duplicate(scholarship_model):
                dupe_count += 1
                print 'duplicate. not saving.'
            else:
                print 'saving'
                scholarship_model.save()

            print '{} / {} duplicates: {}'.format(i, len(scholarships), dupe_count)

    def _extract_max_reward(self, awards):
        """
        Takes an array like this: [u'Minimum:$1,000', u'Maximum:$10,000']
        or this: [u'Maximum:$1,000'] and returns an integer of USD
        """
        if len(awards) == 1:
            max_award_string = awards[0]
        elif len(awards) == 2:
            max_award_string = awards[1]
        elif len(awards) == 0:
            return 0
        else:
            print awards
            print 'got unexpected awards array. returning 0'
            sys.exit()
            return 0
        if 'Maximum:$' in max_award_string:
            max_award_string = max_award_string.replace('Maximum:$', '')
        elif 'Minimum:$' in max_award_string:
            max_award_string = max_award_string.replace('Minimum:$', '')
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
                if len(day) > 2:
                    print 'got multiple deadlines. double check this scholarships.'
                    day = day[:2]
                if day == '29' and month == '2':
                    print 'special case for stupid scholarship with nonexistent date.'
                    day = '1'
                    month = '3'
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

    def _is_high_school_eligible(self, eligibility):
        for use in eligibility:
            if use == 'Full-time study':
                return True
            if use == 'Freshman year':
                return True
        return False

    def _is_undergraduate_eligible(self, eligibility):
        for use in eligibility:
            if use in ('Freshman year', 'Sophomore year', 'Junior year', 'Senior year',
                       'Undergraduate certificate program'):
                return True
        return False


    def _is_graduate_eligible(self, eligibility):
        for use in eligibility:
            if use in ('Any graduate study'):
                return True
        return False

    def _is_essay_required(self, requirements):
        if 'no essay' in requirements.lower():
            return False
        elif 'essay' in requirements.lower():
            return True
        else:
            return False

    def _is_duplicate(self, scholarship):
        try:
            dupe = Scholarship.objects.get(title=scholarship.title)
            return True
        except Scholarship.DoesNotExist as e:
            return False