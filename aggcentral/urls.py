from django.conf.urls import patterns, url, include


urlpatterns = patterns('',
                       url(r'^/edit$', 'aggcentral.views.edit', name='edit_scholarship'),
                       )