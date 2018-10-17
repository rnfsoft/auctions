from django.contrib import admin
from .models import *

# Register your models here.
class ManagementAdmin(admin.ModelAdmin):
    list_display = ['task', 'count', 'started', 'finished', 'state']


admin.site.register(ManagementLog, ManagementAdmin)