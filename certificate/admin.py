from django.contrib import admin
from .models import Certificate, WeldingType


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    pass


@admin.register(WeldingType)
class WeldingTypeAdmin(admin.ModelAdmin):
    pass
