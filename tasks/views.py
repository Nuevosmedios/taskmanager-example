from django.shortcuts import render
from django.views.generic import CreateView, ListView
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
    success_url = '/tasks/list'
    form_class = TaskForm

    def notify_users(self, task):
        users = task.users.all()
        groups = task.groups.all()
        for g in groups:
            users |= g.user_set.all()
        from_user = task.creator
        actual_users = users.distinct()
        if notification:
            notification.send(actual_users, "task_assigned",
                              {"from_user": from_user}, now=True)
        
        
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        form.save_m2m()
        self.notify_users(obj)
        return HttpResponseRedirect(self.success_url)


class TaskList(ListView):
    model = Task
    paginate_by = 6

    def get_queryset(self):
        return Task.objects.filter(creator=self.request.user).order_by('-id')
