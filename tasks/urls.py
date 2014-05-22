from django.conf.urls import patterns, url
from .views import TaskCreate, TaskList


urlpatterns = patterns('',
                       url(r'^create/$', TaskCreate.as_view(), name='create'),
                       url(r'^list/$', TaskList.as_view(), name='list'),
)
