from django.contrib import admin
from .models import Task

#to show the readonly field on my admin page
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)

# Register your models here.
admin.site.register(Task, TaskAdmin)
