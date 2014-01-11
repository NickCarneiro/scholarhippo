# MySQL is the master set of scholarships
# This script coeps them all into elasticsearch
import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scholarhippo.settings")

from pyes import *
from search.models import *
from search.elasticsearch_fields import EsFields as es

conn = ES('scholarhippo.com:9200')
DEV_INDEX = 'noessay-dev'
PROD_INDEX = 'noessay-prod'
SCHOLARSHIP_TYPE = 'scholarship'

if len(sys.argv) >= 2 and sys.argv[1] == 'prod':
    index = PROD_INDEX
else:
    index = DEV_INDEX

print 'building ' + index


def create_index():
    try:
        conn.indices.delete_index(index)
    except:
        pass

    conn.indices.create_index(index)

    mapping = {
        es.django_id: {
            'index': 'no',
            'store': 'yes',
            'type': 'long'
        },
        es.title: {
            'index': 'analyzed',
            'store': 'yes',
            'type': 'string'
        },
        es.third_party_url: {
            'index': 'no',
            'store': 'yes',
            'type': 'string'
        },
        es.description: {
            'index': 'analyzed',
            'store': 'yes',
            'type': 'string',
            'term_vector': 'with_positions_offsets'
        },
        es.date_added: {
            'index': 'analyzed',
            'store': 'yes',
            'type': 'date'
        },
        es.deadline: {
            'index': 'analyzed',
            'store': 'yes',
            'type': 'date'
        },
        es.essay_required: {
            'index': 'analyzed',
            'store': 'yes',
            'type': 'boolean'
        },
        es.amount_usd: {
            'index': 'analyzed',
            'store': 'yes',
            'type': 'integer'
        },
        es.organization: {
            'index': 'analyzed',
            'store': 'yes',
            'type': 'string'
        },
        es.min_age_restriction: {
            'index': 'analyzed',
            'store': 'yes',
            'type': 'integer'
        },
        es.state_restriction: {  # 2 letter postal code like TX
            'index': 'not_analyzed',
            'store': 'yes',
            'type': 'string'
        },
        es.essay_length_words: {
            'index': 'analyzed',
            'store': 'yes',
            'type': 'integer'
        },
        es.gpa_restriction: {
            'index': 'analyzed',
            'store': 'yes',
            'type': 'float'
        },
        es.additional_restriction: {
            'index': 'no',
            'store': 'yes',
            'type': 'string'
        },
        es.major_restriction: {
            'index': 'analyzed',
            'store': 'yes',
            'type': 'string'
        },
        # ensure that these values always come from the universities table
        es.university_restriction: {
            'index': 'analyzed',
            'store': 'yes',
            'type': 'string'
        },
        # ensure that these values always come from the Choices in models
        es.ethnicity_restriction: {
            'index': 'analyzed',
            'store': 'yes',
            'type': 'string'
        },
        # ensure that these values always come from the Choices in models
        es.gender_restriction: {
            'index': 'analyzed',
            'store': 'yes',
            'type': 'string'
        },
        es.sponsored: {
            'index': 'analyzed',
            'store': 'yes',
            'type': 'boolean'
        }
    }

    conn.indices.put_mapping(SCHOLARSHIP_TYPE, {'properties': mapping}, [index])


def populate_index():
    #iterate over all the scholarships and put them in es index
    scholarships = Scholarship.objects.filter(status=0)
    for s in scholarships:
        print s.title
        university_name = None
        gender_restriction = None
        ethnicity_restriction = None
        universities = s.university_restriction.all()
        if universities:
            university_name = universities[0].name
        if s.gender_restriction:
            gender_restriction = GENDER[s.gender_restriction]
        if s.ethnicity_restriction:
            ethnicity_restriction = ETHNICITIES[s.ethnicity_restriction]
        scholarship_es = {
            'django_id': s.id,
            'title': s.title,
            'third_party_url': s.third_party_url,
            'description': s.description,
            'date_added': s.date_added,
            'deadline': s.deadline,
            'essay_required': s.essay_required,
            'amount_usd': s.amount_usd,
            'organization': s.organization,
            'min_age_restriction': s.min_age_restriction,
            'state_restriction': s.state_restriction,
            'essay_length_words': s.essay_length_words,
            'gpa_restriction': s.gpa_restriction,
            'additional_restriction': s.additional_restriction,
            'major_restriction': s.major_restriction,
            'university_restriction': university_name,
            'ethnicity_restriction': ethnicity_restriction,
            'gender_restriction': gender_restriction,
            'sponsored': s.sponsored
        }
        conn.index(scholarship_es, index, SCHOLARSHIP_TYPE)


def query_index():
    q = TermQuery('description', 'black')
    results = conn.search(query=q)
    for r in results:
        print r


create_index()
populate_index()
