from django.conf.urls.defaults import *
from link.views import index, user

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', index),
	(r'^date/(?P<urldate>\d{4}\-\d{2}\-\d{2})/$', index),
	(r'^user/(?P<user>[^/]+)/$', user),
	(r'^admin/', include(admin.site.urls)),
)
