from django.contrib import admin
from .models import PrivilegesType


@admin.register(PrivilegesType)
class PrivilegesTypeAdmin(admin.ModelAdmin):
    pass
