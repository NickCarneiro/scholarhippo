import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from mixpanel import Mixpanel
from search.models import SubmittedLink
from raven.contrib.django.raven_compat.models import client

@csrf_exempt
def submit_scholarship(req):
    if req.method == 'GET':
        context = {
            'page_title': 'About Scholar Hippo'
        }
        return render_to_response('submit_scholarship.html', context)
    elif req.method == 'POST':
        payload = json.loads(req.body)
        submitted_scholarship = SubmittedLink(title=payload['title'], third_party_url=payload['url'])
        if 'email' in payload:
            submitted_scholarship.email = payload['email']
        submitted_scholarship.save()
        mp = Mixpanel('2871f3b0cb686b7f9fff1ba66d042817')
        mp.track(0, 'submission', {
            'title': payload['title']
        })
        client.captureMessage("New scholarship submitted.", title=payload['title'])
        return HttpResponse(json.dumps({'msg': 'thanks dawg'}))

