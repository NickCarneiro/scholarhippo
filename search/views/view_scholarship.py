from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.utils.html import linebreaks
from search import request_utils
from search.models import Scholarship
from scholarhippo import settings


def scholarship_redirect(request):
    sk = request.GET.get('sk')
    title = request.GET.get('title')
    if title:
        safe_title = title.encode('ascii', 'ignore')
    else:
        safe_title = ''
    redirect_url = '/scholarship/{}/?title={}'.format(sk, safe_title)
    return redirect(redirect_url, permanent=True)


def view_scholarship(request, scholarship_key):
    if not scholarship_key:
        scholarship_key = request.GET.get('sk')
    scholarship_id = request_utils.decrypt_sk(scholarship_key)

    scholarship = Scholarship.objects.get(id=scholarship_id)
    # get description html ready
    if '<div>' in scholarship.description:
        description = scholarship.description
    else:
        description = linebreaks(scholarship.description)
    if scholarship.additional_restriction and '<div>' in scholarship.additional_restriction:
        additional_restriction = scholarship.additional_restriction
    else:
        additional_restriction = linebreaks(scholarship.additional_restriction)

    context = {'scholarship_model': scholarship,
               'scholarship_key': scholarship_key,
               'page_title': scholarship.title,
               'description': description,
               'additional_restriction': additional_restriction,
               'environment': settings.ENVIRONMENT
    }
    return render_to_response('view_scholarship.html',
                              context,
                              context_instance=RequestContext(request))