from django.conf.urls import patterns, url, include


urlpatterns = patterns('',
                       url(r'^/manage_deadlines', 'aggcentral.views.manage_deadlines', name='edit_scholarship'),
                       url(r'^/expire', 'aggcentral.views.expire', name='expire_scholarship'),
                       url(r'^/deadline', 'aggcentral.views.deadline', name='update_deadline'),
                       url(r'^/$', 'aggcentral.views.home', name='home'),
                       )