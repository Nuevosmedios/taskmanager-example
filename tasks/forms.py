from django import forms
from .models import Task
from ajax_select import make_ajax_field


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('creator',)

    def __init__(self, *args, **kwargs):
        print "EN FORM"
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['users'] = make_ajax_field(Task, 'users', 'userlookup', help_text="")
        self.fields['groups'] = make_ajax_field(Task, 'groups', 'grouplookup', help_text="")
