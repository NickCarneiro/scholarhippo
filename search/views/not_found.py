from django.shortcuts import render_to_response


def not_found(request):
    return render_to_response('404.html')