from django.contrib import admin
from .models import PrivilegesType, QuotaType, Quota


@admin.register(PrivilegesType)
class PrivilegesTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Quota)
class QuotaTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(QuotaType)
class QuotaTypeTypeAdmin(admin.ModelAdmin):
    pass
