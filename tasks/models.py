from django.db import models
from django.conf import settings
from django.contrib.contenttypes import generic
from attachments.models import Attachment


UserModel = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class Task(models.Model):
    """
    A task is something the user or another user must do by means of
    an evidence.
    """
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    creator = models.OneToOneField(UserModel, related_name='task_user')

    def __unicode__(self):
        return u'<Task: %s>' % self.name


class Evidence(models.Model):
    """
    An evidence stores the user's work on a task.
    """
    task = models.ForeignKey(Task)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True, auto_now=True)
    attachments = generic.GenericRelation(Attachment)

    def __unicode__(self):
        return u'<Evidence: task %s, atts %s>' % (self.task,
                                                  self.attachments.count())
