from django.conf.urls import patterns, url, include


urlpatterns = patterns('',
                       url(r'^/view$', 'report.views.view_reports', {}, 'view_reports'),
                       url(r'^$', 'report.views.save_report', {}, 'save_report'),

                       )