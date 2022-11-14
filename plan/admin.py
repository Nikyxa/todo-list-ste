from django.contrib import admin

from plan.models import Task, Tag

admin.site.register(Task)
admin.site.register(Tag)