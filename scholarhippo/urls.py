from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'search.views.home', name='home'),
    url(r'^search', 'search.views.serp', name='serp'),
    url(r'^about', 'search.views.about', name='about'),
    url(r'^legal', 'search.views.legal', name='legal'),
    url(r'^scholarship/$', 'search.views.scholarship_redirect',
        name='view scholarship redirect'),
    url(r'^scholarship/(?P<scholarship_key>\w{16})', 'search.views.view_scholarship',
        name='view scholarship'),
    url(r'^error', 'search.views.error', name='error'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #SEO canonical urls
    url(r'^no-essay-scholarships', 'search.views.serp', name='serp'),
    url(r'^scholarships-in-([a-zA-Z\-]+)', 'search.views.serp_canonical', name='serp_canonical'),
    url(r'^sitemap.xml', 'search.views.sitemap', name='sitemap'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^404', 'search.views.not_found', name='not_found'),
    url(r'^check', 'search.views.check_for_scholarship', name='check_for_scholarship'),
    url(r'^aggregation', 'search.views.aggregation', name='aggregation'),

    url(r'^helper', 'helper.views.signup', name='helper'),




)
