from django.contrib import admin

# Register your models here.
from jobs.models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass