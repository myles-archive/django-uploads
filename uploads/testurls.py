from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin

admin.autodiscover()

sitemaps = {}

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	
	# url(r'^uploads/', include('uploads.urls')),
	
	url(r'^sitemap.xml$',
		'django.contrib.sitemaps.views.sitemap',
		{ 'sitemaps': sitemaps },
		name = 'sitemap'
	),
)
