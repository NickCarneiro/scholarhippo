from django.shortcuts import render_to_response


def about(request):
    context = {
        'page_title': 'About Scholar Hippo'
    }
    return render_to_response('about.html', context)


def legal(request):
    context = {
        'page_title': 'Legal'
    }
    return render_to_response('legal.html', context)