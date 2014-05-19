from django.shortcuts import render
from django.views.generic import CreateView
from .models import Task
from .forms import TaskForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.conf import settings

if "notification" in settings.INSTALLED_APPS:
    from notification import models as notification
else:
    notification = None



class TaskCreate(CreateView):
    model = Task
    success_url = '/admin'
    form_class = TaskForm

    def notify_users(self, task):
        print "notifying..."
        users = task.users.all()
        from_user = task.creator
        print users
        actual_users = (users|g.user_set.all()).distinct()
        #print task.groups.all()
        #for 
        if notification:
            print "sending..."
            notification.send(actual_users, "task_assigned",
                              {"from_user": from_user},
                              now=True)
        
        
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        form.save_m2m()
        self.notify_users(obj)
        return HttpResponseRedirect(self.success_url)
