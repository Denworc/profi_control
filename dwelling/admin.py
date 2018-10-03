from django.contrib import admin
from .models import Dwelling


@admin.register(Dwelling)
class DwellingAdmin(admin.ModelAdmin):
    pass
