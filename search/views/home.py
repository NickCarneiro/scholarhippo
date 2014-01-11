from django.shortcuts import render_to_response
from django.conf import settings
from search.models import Scholarship


def home(request):
    scholarship_count = Scholarship.objects.count()
    return render_to_response('index.html', {'scholarship_count': scholarship_count,
                                             'environment': settings.ENVIRONMENT})