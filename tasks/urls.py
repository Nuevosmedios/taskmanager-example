from django.conf.urls import patterns, url
from .views import TaskCreate


urlpatterns = patterns('',
                       url(r'^create/$', TaskCreate.as_view(), name='create'),
)
