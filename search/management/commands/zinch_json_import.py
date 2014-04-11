import datetime
from django.core.exceptions import MultipleObjectsReturned
from django.core.management.base import BaseCommand
import json
import lxml.html
import sys
from search.models import Scholarship


class Command(BaseCommand):
    help = 'import zinch scholarships from a json file'

    def handle(self, *args, **options):
        if len(args) != 1:
            print 'usage: python manage.py zinch_json_import filename.json'
            return
        file_path = args[0]
        f = open(file_path)
        scholarships = json.loads(f.read())
        i = 0
        dupe_count = 0
        for scholarship in scholarships:
            i += 1
            print scholarship['title']
            award_amount = self._extract_award_amount(scholarship['amount'])
            deadline = self._extract_deadline(scholarship['deadline'])
            requirements = scholarship['eligibility'] + '<br />' + scholarship['application_overview']
            description = scholarship['purpose'] + '<br />' + scholarship['background']
            is_essay_required = self._is_essay_required(requirements) or self._is_essay_required(description)
            if '<script>' in requirements or '<script>' in description:
                raise Exception('Found a script tag in the html!')

            scholarship_model = Scholarship()
            scholarship_model.title = scholarship['title']
            scholarship_model.amount_usd = award_amount
            scholarship_model.essay_required = is_essay_required
            scholarship_model.organization = scholarship['provider_name']
            scholarship_model.third_party_url = scholarship['third_party_url']
            scholarship_model.high_school_eligible = True
            scholarship_model.description = description
            scholarship_model.additional_requirements = requirements
            scholarship_model.deadline = deadline

            if self._is_duplicate(scholarship_model):
                dupe_count += 1
                print 'duplicate. not saving.'
            else:
                print 'saving'
                scholarship_model.save()

            print '{} / {} duplicates: {}'.format(i, len(scholarships), dupe_count)

    def _extract_award_amount(self, amount):
        """
        Takes an amount like "$1000" and returns an integer 1000
        """
        clean_amount = amount.replace('$', '').strip()
        return int(clean_amount)

    def _extract_deadline(self, deadline_str):
        """
        July 31, 2014 -> datetime.date
        """
        return datetime.datetime.strptime(deadline_str, '%B %d, %Y')

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
        except MultipleObjectsReturned as e:
            return True