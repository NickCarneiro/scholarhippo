from django.shortcuts import render_to_response

#attempt to render nonexistent file to cause 500 error to make sure logs work
def error(request):
    return render_to_response('error.html')
