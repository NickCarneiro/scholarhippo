from django.shortcuts import render_to_response
from haystack.inputs import Exact
from haystack.query import SearchQuerySet
from search import request_utils
from search.search_request import SearchRequest
from search.serp_result import SerpResult
from search.request_utils import *
from django.conf import settings
from HTMLParser import HTMLParser

DESCRIPTION_LENGTH = 300
RESULTS_PER_PAGE = 10


def serp(request):

    location = parse_string_param(request.GET.get('l'), '')

    keyword = parse_string_param(request.GET.get('q'), '')

    # refine params
    start = parse_int_param(request.GET.get('start'), 0)
    if start % RESULTS_PER_PAGE != 0:
        start = 0
    no_essay_required = parse_boolean_param(request.GET.get('ne'))
    deadline = parse_string_param(request.GET.get('d'), None)
    ethnicity = parse_int_param(request.GET.get('e'), None)
    gender = parse_int_param(request.GET.get('g'), None)

    search_req = SearchRequest(keyword, location, no_essay_required,
        deadline, ethnicity, gender)

    # got a keyword
    filters = []

    query_arguments = {
        'content': keyword
    }
    if location and location != 'US':
        query_arguments['state_restriction'] = location
    if no_essay_required:
        query_arguments['essay_required'] = 'true'
    if ethnicity:
        query_arguments['ethnicity_restriction'] = ethnicity
    if gender:
        query_arguments['gender_restriction'] = gender

    results = SearchQuerySet().filter(**query_arguments)
    total_result_count = len(results)
    scholarships = []
    for schol in results[start:start + RESULTS_PER_PAGE]:
        sk = request_utils.encrypt_sid(str(schol.pk))
        result = SerpResult(sk, schol, to_highlight=keyword)

        scholarships.append(result)
    page_links = build_pagination_objects(total_result_count, start, search_req)
    is_first_page = start == 0
    is_last_page = RESULTS_PER_PAGE + start >= total_result_count
    next_page_href = search_req.get_base_url(start + RESULTS_PER_PAGE)
    prev_page_href = search_req.get_base_url(start - RESULTS_PER_PAGE)
    canonical_url = search_req.get_canonical_url(keyword, location)
    meta_keywords = get_meta_keywords(query=keyword, location=location)
    meta_description = get_meta_description(total_result_count=total_result_count, query=keyword, location=location)
    if location == 'US':
        title_location = 'the United States'
    else:
        title_location = location
    page_title = '{} scholarships in {} | ScholarHippo.com'.format(keyword, title_location)
    return render_to_response('serp.html',
                              {
                                  'scholarship_list': scholarships,
                                  'search_request': search_req,
                                  'result_count': total_result_count,
                                  'page_links': page_links,
                                  'is_first_page': is_first_page,
                                  'is_last_page': is_last_page,
                                  'prev_page_href': prev_page_href,
                                  'next_page_href': next_page_href,
                                  'start_index': start + 1,
                                  'end_index': min(start + RESULTS_PER_PAGE, total_result_count),
                                  'results_per_page': RESULTS_PER_PAGE,
                                  'environment': settings.ENVIRONMENT,
                                  'canonical_url': canonical_url,
                                  'meta_description': meta_description,
                                  'meta_keywords': meta_keywords,
                                  'page_title': page_title
                                  }
    )


def description_to_snippet(desc):
    no_html = strip_tags(desc)
    return no_html[:DESCRIPTION_LENGTH].rsplit(' ', 1)[0] + '...'



class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def strip_non_em_tags(html):
    html = html.replace('<div>', '')
    html = html.replace('</div>', '')
    html = html.replace('<p>', '')
    html = html.replace('</p>', '')
    html = html.replace('<ul>', '')
    html = html.replace('</ul>', '')
    html = html.replace('<li>', '')
    html = html.replace('</li>', '')
    html = html.replace('<span>', '')
    html = html.replace('</span>', '')
    return html

def build_pagination_objects(result_count, start, search_req):
    if result_count == 0:
        return []
    if start % RESULTS_PER_PAGE != 0:
        start = 0
    # page numbers have to start at 1 because users are human
    current_page_number = start / RESULTS_PER_PAGE + 1
    # add non-link for current page
    links = [{'current_page': True, 'page_number': current_page_number, 'start': start}]
    # try to add up to 5 forward pages
    for i in range(1, 6):
        page_start = start + i * RESULTS_PER_PAGE
        if page_start >= result_count:
            break
        href = search_req.get_base_url(page_start)
        links.append({'current_page': False,
                      'page_number': current_page_number + i,
                      'start': page_start,
                      'href': href
        })
    # try to prepend 5 pages backward
    for i in range(1, 6):
        page_start = start - i * RESULTS_PER_PAGE
        if page_start < 0:
            break
        href = search_req.get_base_url(page_start)
        links.insert(0, {'current_page': False,
                         'page_number': current_page_number - i,
                         'start': page_start,
                         'href': href
                        })
    return links


def get_meta_description(total_result_count, query, location):
    meta_description = str(total_result_count)

    if query:
        meta_description += " " + query

    if total_result_count == 0:
        #Don't add a description for ZRPs
        return None
    elif total_result_count == 1:
        meta_description += " scholarship"
    else:
        meta_description += " scholarships"

    if location and location != "US":
        meta_description += " found in " + request_utils.states_codes_to_names[location]

    meta_description += " on ScholarHippo.com."

    return meta_description


def get_meta_keywords(query, location):
    keywords = ["Scholarships"]
    if query:
        keywords.append(query + " scholarships")

    if location and location != "US":
        friendly_location = request_utils.states_codes_to_names[location]
        keywords.append("Scholarships in " + friendly_location)
        keywords.append(friendly_location + " scholarships")
        if query:
            keywords.append(query + " scholarships in " + friendly_location)
    return ', '.join(keywords)