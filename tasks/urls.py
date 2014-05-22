from django.conf.urls import patterns, url
from .views import TaskCreate, TaskList, TaskUpdate


urlpatterns = patterns('',
                       url(r'^$', TaskList.as_view(), name='list'),
                       url(r'^create/$', TaskCreate.as_view(), name='create'),
                       url('^update/(?P<pk>[\w-]+)$',
                           TaskUpdate.as_view(), name='update'),
                   )
