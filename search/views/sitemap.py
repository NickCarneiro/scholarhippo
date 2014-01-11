from django.shortcuts import render_to_response
from search import request_utils


def sitemap(request):
    state_names = request_utils.states_name_to_codes
    pages = []
    for state_name in state_names:
        pages.append({'url': 'http://noessay.com/scholarships-in-' + state_name})
    return render_to_response('sitemap.xml', {'pages': pages}, content_type="application/xml")

