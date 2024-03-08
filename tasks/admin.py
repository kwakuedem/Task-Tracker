from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'

    list_display = ('get_username', 'title', 'description', 'status', 'deadline')
    
admin.site.register(Task, TaskAdmin)
