from django.contrib import admin
from .models import UkrainianPassport, ForeignPassport, Visa, MilitaryRecords, PersonalID
# Register your models here.


@admin.register(UkrainianPassport)
class UkrainianPassportAdmin(admin.ModelAdmin):
    pass


@admin.register(ForeignPassport)
class ForeignPassportAdmin(admin.ModelAdmin):
    pass


@admin.register(Visa)
class VisaAdmin(admin.ModelAdmin):
    pass


@admin.register(MilitaryRecords)
class MilitaryRecordsAdmin(admin.ModelAdmin):
    pass


@admin.register(PersonalID)
class PersonalIDAdmin(admin.ModelAdmin):
    pass
