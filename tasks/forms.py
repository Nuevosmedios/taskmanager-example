from django import forms
from .models import Task
from ajax_select import make_ajax_field
from bootstrap3_datetime.widgets import DateTimePicker


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('creator',)

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['users'] = make_ajax_field(Task, 'users', 'userlookup', help_text="")
        self.fields['groups'] = make_ajax_field(Task, 'groups', 'grouplookup', help_text="")
        self.fields['details_file'].widget.attrs = {'class': 'btn btn-sm'}
        self.fields['due_date'].widget = DateTimePicker(options={"format": "YYYY-MM-DD",
                                                                 "pickTime": False})
