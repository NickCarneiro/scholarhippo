from django.http import HttpResponse, HttpResponseRedirect
import json
from django.views.decorators.csrf import csrf_exempt
from report.models import Report

@csrf_exempt
def save_report(req):
    if req.method != 'POST':
        return HttpResponse('ya gotta send a post request')
    form = json.loads(req.body)

    problem = form['problem']
    explanation = form['explanation']
    report = Report()
    report.problem = problem
    report.explanation = explanation
    report.ip_address = get_client_ip(req)
    report.save()
    return HttpResponse('{"msg": "thanks"}', content_type='application/json')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip