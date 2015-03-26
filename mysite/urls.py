from django.conf.urls.defaults import patterns, include, url
#import sys, os
#sys.path.insert(0, '/home/yong/mysite')
from mysite.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail
from mysite.books.models import Publisher, Book
from mysite.myfeeds import *

admin.autodiscover()

publisher_info = {
    'queryset': Publisher.objects.all(),
    'template_name':'publisher_list_page.html',
    'template_object_name':'publishers',
    'extra_context':{'book_list':Book.objects.all()},#specify a callback could ease the impact of buffering
}
book_info = {
	'queryset': Book.objects.order_by('-publication_date'),
}

feeds = {
    'latest': LatestEntries,
    #'categories': LatestEntriesByCategory, #no code yet
}

urlpatterns = patterns('',
	(r'^hello/$',hi),
	(r'^time/$', current_datetime),
	(r'^time/plus/[-]{0,1}(\d{1,2})/$', hours_ahead),
	(r'^search-form',search_form),
	(r'^search/$',search),
	(r'^dismeta/$',display_meta),
	(r'^contact/$',contact),\
	(r'^contactf/$',contact_f),
	(r'^about/$', direct_to_template, {'template':'about.html'}),#generic views
	(r'^about/(\w+)$', about_pages),#generic views
	(r'^publishers/$', list_detail.object_list, publisher_info),
	(r'^csv/$', unruly_passengers_csv),
	(r'^pdf/$', hello_pdf),
	(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',    
		{'feed_dict': feeds}),#not work since no model yet

    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
