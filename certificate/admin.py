from django.contrib import admin
from .models import Certificate, WeldingType, Training, TestType, Test, InterviewType, Interview, Polish, \
    QualificationLevel, Other, SpatialPosture, ConnectionType, MetalBrand, WeldMethod, \
    SemiAutomatic, Bulgarian, Candle, DrawReading, PostQualificationLevel


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


@admin.register(DrawReading)
class DrawReadingAdmin(admin.ModelAdmin):
    pass


@admin.register(Candle)
class CandleAdmin(admin.ModelAdmin):
    pass


@admin.register(Bulgarian)
class BulgarianAdmin(admin.ModelAdmin):
    pass


@admin.register(SemiAutomatic)
class SemiAutomaticAdmin(admin.ModelAdmin):
    pass


@admin.register(WeldMethod)
class WeldMethodAdmin(admin.ModelAdmin):
    pass


@admin.register(MetalBrand)
class MetalBrandAdmin(admin.ModelAdmin):
    pass


@admin.register(ConnectionType)
class ConnectionTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(SpatialPosture)
class SpatialPostureAdmin(admin.ModelAdmin):
    pass


@admin.register(Other)
class OtherAdmin(admin.ModelAdmin):
    pass


@admin.register(QualificationLevel)
class QualificationLevelAdmin(admin.ModelAdmin):
    pass


@admin.register(PostQualificationLevel)
class PostQualificationLevelAdmin(admin.ModelAdmin):
    pass


