from django.contrib import admin
from attachments.admin import AttachmentInlines
from .models import Evidence, Task


class TaskAdmin(admin.ModelAdmin):
    pass
admin.site.register(Task, TaskAdmin)


class EvidenceAdmin(admin.ModelAdmin):
    inlines = [AttachmentInlines]
admin.site.register(Evidence, EvidenceAdmin)
