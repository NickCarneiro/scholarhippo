from django.shortcuts import render_to_response
from django.http import HttpResponse
from search.models import *

def aggregation(request):
    return render_to_response('aggregation.html')
def check_for_scholarship(request):
    url = request.GET.get('url')
    if url is not None:
        # check if this scholarship exists
        scholarship_exists = Scholarship.objects.filter(third_party_url=url).exists()
        return render_json(scholarship_exists)
    else:
        return HttpResponse('{"error": "URL parameter required"}')


def render_json(exists):
    return HttpResponse('{"exists": '+str(exists).lower()+'}', mimetype='application/json')