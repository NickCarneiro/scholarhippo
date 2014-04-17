import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.shortcuts import render
from search.models import Scholarship

@login_required
@permission_required('is_superuser')
def edit(req):

    scholarships = Scholarship.objects.filter(deadline__lt=datetime.datetime.now(), status=0)
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

    context = {
        'scholarships': scholarships,
        'result_count': result_count
    }
    return render(req, 'expired_deadlines.html', context)