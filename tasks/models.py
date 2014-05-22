from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext as _
from attachments.models import Attachment


UserModel = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class TaskCategory(models.Model):
    """
    A category is a way to classify tasks
    """
    name = models.CharField(max_length=30, unique=True,
                            verbose_name=_('Name'))
    parent = models.ForeignKey('self', blank=True, null=True,
                               verbose_name=_('Parent'))

    class Meta:
        verbose_name_plural = 'task categories'
    
    def __unicode__(self):
        return unicode(self.name)


class Task(models.Model):
    """
    A task is something the user or another user must do by means of
    an evidence.
    """
    name = models.CharField(max_length=30, verbose_name=_('Name'))
    description = models.TextField(blank=True, null=True,
                                   verbose_name=_('Description'))
    category = models.ForeignKey(TaskCategory, blank=True, null=True,
                                 verbose_name=_('Category'))
    created_date = models.DateTimeField(auto_now_add=True,
                                        verbose_name=_('Creation date'))
    due_date = models.DateTimeField(blank=True, null=True,
                                    verbose_name=_('Date'))
    creator = models.ForeignKey(UserModel, related_name='task_created_set',
                                verbose_name=_('Creator'))
    users = models.ManyToManyField(UserModel, blank=True, null=True, related_name='task_users_set', verbose_name=_('Users'))
    groups = models.ManyToManyField(Group, blank=True, null=True,
                                    verbose_name=_('Groups'))
    details_file = models.FileField(blank=True, null=True, upload_to='files',
                                    verbose_name=_('Attached file'))

    def __unicode__(self):
        return u'<Task: %s>' % self.name


class Evidence(models.Model):
    """
    An evidence stores the user's work on a task.
    """
    task = models.ForeignKey(Task, verbose_name=_('Task'))
    created_date = models.DateTimeField(auto_now_add=True,
                                        verbose_name=_('Creation date'))
    updated_date = models.DateTimeField(auto_now_add=True, auto_now=True,
                                        verbose_name=_('Updated on'))
    attachments = generic.GenericRelation(Attachment,
                                          verbose_name=_('Attachments'))

    def __unicode__(self):
        return u'<Evidence: task %s, atts %s>' % (self.task,
                                                  self.attachments.count())
