import datetime
import json
import subprocess
from django import template
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from search.models import Scholarship
from pytz import timezone

register = template.Library()

@login_required
@permission_required('is_superuser')
def manage_deadlines(req):

    scholarships = Scholarship.objects.filter(deadline__lt=datetime.datetime.now())
    result_count = len(scholarships)
    paginator = Paginator(scholarships, 200)  # Show 200 scholarships per page

    page = req.GET.get('page')
    try:
        scholarships = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        scholarships = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        scholarships = paginator.page(paginator.num_pages)
    one_week_ago = datetime.datetime.now(tz=timezone('US/Central')) - datetime.timedelta(days=7)
    context = {
        'scholarships': scholarships,
        'result_count': result_count,
        'one_week_ago': one_week_ago
    }
    return render(req, 'expired_deadlines.html', context)

# expires the given scholarship
@login_required
@permission_required('is_superuser')
@csrf_exempt
def expire(req):
    if req.method != 'POST':
        return HttpResponse('{"msg": "must be post request"}', content_type='application/json')
    expire_request = json.loads(req.body)
    scholarship_id = expire_request['scholarshipId']
    scholarship = Scholarship.objects.get(pk=scholarship_id)
    if scholarship.status == 1:
        scholarship.status = 0
    else:
        scholarship.status = 1
    scholarship.save()
    return HttpResponse(json.dumps({'msg': 'ok',
                                    'scholarshipId': scholarship_id,
                                    'status': scholarship.status}), content_type='application/json')


#  updates deadline for specified scholarship
@login_required
@permission_required('is_superuser')
@csrf_exempt
def deadline(req):
    if req.method != 'POST':
        return HttpResponse('{"msg": "must be post request"}', content_type='application/json')
    deadline_request = json.loads(req.body)
    deadline_number = deadline_request['deadlineNumber']
    deadline_number = '' if deadline_number == 1 else str(deadline_number)
    new_deadline = deadline_request['newDeadline']
    if new_deadline == '' or new_deadline == 'none':
        new_deadline = None
    scholarship_id = deadline_request['scholarshipId']
    scholarship = Scholarship.objects.get(pk=scholarship_id)
    deadline_field_name = 'deadline{}'.format(deadline_number)
    setattr(scholarship, deadline_field_name, new_deadline)
    scholarship.save()
    return HttpResponse(json.dumps({'msg': 'ok', 'scholarshipId': scholarship_id}), content_type='application/json')

@login_required
@permission_required('is_superuser')
def home(req):
    version_info = get_version_info()
    print version_info
    context = {
        'git_info': version_info
    }
    return render(req, 'aggcentral.html', context)


def get_version_info():
    process = subprocess.Popen(['git', 'show', '--quiet'], stdout=subprocess.PIPE)
    git_info, err = process.communicate()
    return git_info

