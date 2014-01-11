from django.http import HttpResponsePermanentRedirect
from search import request_utils
from search.views import serp


def serp_canonical(request, state_param):
    if request.GET.get('l') is None and request.GET.get('q') is None:
        request_utils.determine_search_terms(request, state_param)
        if request.GET.get('l') is None and request.GET.get('q') is None:
            return HttpResponsePermanentRedirect('/404')
    return serp(request)