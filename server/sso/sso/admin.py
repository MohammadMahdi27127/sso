from django.contrib import admin
from . import models

@admin.register(models.SMS)
class SMSAdmin(admin.ModelAdmin):
    pass