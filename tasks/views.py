from django.views.generic import CreateView, ListView, UpdateView
from .models import Task
from .forms import TaskForm
from django.http import HttpResponseRedirect
from django.conf import settings


if "notification" in settings.INSTALLED_APPS:
    from notification import models as notification
else:
    notification = None


def notify_users(task):
    users = task.users.all()
    groups = task.groups.all()
    for g in groups:
        users |= g.user_set.all()
    from_user = task.creator
    actual_users = users.distinct()
    if notification:
        notification.send(actual_users, "task_assigned",
                          {"from_user": from_user}, now=True)
    

class TaskCreate(CreateView):
    model = Task
    success_url = '/tasks/'
    form_class = TaskForm        
    extra_context = {'success_url': success_url}

    def get_context_data(self, *args, **kwargs):
        context = super(TaskCreate, self).get_context_data(*args, **kwargs)
        if self.extra_context:
            context.update(self.extra_context)
        return context
        
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        form.save_m2m()
        notify_users(obj)
        return HttpResponseRedirect(self.success_url)


class TaskList(ListView):
    model = Task
    paginate_by = 6

    def get_queryset(self):
        return Task.objects.filter(creator=self.request.user).order_by('-id')


class TaskUpdate(UpdateView):
    model = Task
    success_url = '/tasks/'
    form_class = TaskForm
    extra_context = {'success_url': success_url}

    def get_context_data(self, *args, **kwargs):
        context = super(TaskUpdate, self).get_context_data(*args, **kwargs)
        if self.extra_context:
            context.update(self.extra_context)
        return context
