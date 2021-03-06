from django.contrib import admin
from attachments.admin import AttachmentInlines
from .models import Evidence, Task, TaskCategory


class TaskCategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(TaskCategory, TaskCategoryAdmin)


class TaskAdmin(admin.ModelAdmin):
    pass
#    inlines = [AttachmentInlines]
admin.site.register(Task, TaskAdmin)


class EvidenceAdmin(admin.ModelAdmin):
    inlines = [AttachmentInlines]
admin.site.register(Evidence, EvidenceAdmin)
