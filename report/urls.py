from django.conf.urls import patterns, url, include


urlpatterns = patterns('',
                       url(r'^$', 'report.views.save_report', {}, 'save_report'),
                       )