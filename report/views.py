from django.http import HttpResponse, HttpResponseRedirect
from report.models import Report


def save_report(req):
    if req.method != 'POST':
        return HttpResponse('ya gotta send a post request')
    problem = req.POST.get('problem')
    explanation = req.POST.get('explanation')
    source_page = req.POST.get('next')
    report = Report()
    report.problem = problem
    report.explanation = explanation
    report.ip_address = get_client_ip(req)
    report.save()
    return HttpResponseRedirect(source_page)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip