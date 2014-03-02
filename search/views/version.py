from django.http import HttpResponse
import subprocess


def version(req):
    label = subprocess.check_output(['git', 'describe', '--long', '--all'])
    return HttpResponse(label)