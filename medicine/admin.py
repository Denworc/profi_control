from django.contrib import admin
from .models import MedicalReview, MedicalReviewType, Insurance, InsuranceEvent, InsuranceType
# Register your models here.


@admin.register(MedicalReview)
class MedicalReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(MedicalReviewType)
class MedicalReviewTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    pass


@admin.register(InsuranceEvent)
class InsuranceEventAdmin(admin.ModelAdmin):
    pass


@admin.register(InsuranceType)
class InsuranceTypeAdmin(admin.ModelAdmin):
    pass
