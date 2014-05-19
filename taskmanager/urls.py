from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       (r'^attachments/', include('attachments.urls')),
                       (r'^tasks/', include('tasks.urls')),
                   )
