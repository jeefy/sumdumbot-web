from django.conf.urls.defaults import *
from link.views import index, user, query, add, channel, message

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', index),
	(r'^date/(?P<urldate>\d{4}\-\d{2}\-\d{2})/$', index),
	(r'^user/(?P<user>[^/]+)/$', user),
	(r'^channel/(?P<channel>[^/]+)/$', channel),
	(r'^q/(?P<q>[^/]+)/$', query),
	(r'^link/add', add),
	(r'^message', message),
	(r'^manage/', include(admin.site.urls)),
)
