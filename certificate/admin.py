from django.contrib import admin
from .models import Certificate, WeldingType, Training, TestType, Test, InterviewType, Interview, Polish


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    pass


@admin.register(WeldingType)
class WeldingTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    pass


@admin.register(InterviewType)
class InterviewTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    pass


@admin.register(TestType)
class TestTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    pass


@admin.register(Polish)
class PolishAdmin(admin.ModelAdmin):
    pass
