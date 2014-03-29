from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from search.models import Scholarship
from report.models import Report
from request_utils import decrypt_sk, encrypt_sid


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
    scholarship_id = decrypt_sk(form['sk'])
    scholarship = Scholarship.objects.get(id=scholarship_id)
    report.scholarship = scholarship
    report.save()
    return HttpResponse('{"msg": "thanks"}', content_type='application/json')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def view_reports(req):
    reports = Report.objects.values('scholarship')\
        .annotate(scholarship_count=Count('scholarship'))\
        .order_by('-scholarship_count')
    for report in reports:
        report['scholarship'] = Scholarship.objects.get(id=report['scholarship'])
        report['scholarship_key'] = encrypt_sid(str(report['scholarship'].id))
    print reports
    return render_to_response('report/reports.html', {'reports': reports})