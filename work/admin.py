from django.contrib import admin
from .models import AdoptionInState, TransferInState, Permission, Assignment, Vnosok, Dismissal, Vocation, VocationType, \
    Voivodship, Employer, Factory, BasisList


# Register your models here.


@admin.register(AdoptionInState)
class AdoptionInStateAdmin(admin.ModelAdmin):
    pass


@admin.register(TransferInState)
class TransferInStateAdmin(admin.ModelAdmin):
    pass


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    pass


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Vnosok)
class VnosokAdmin(admin.ModelAdmin):
    pass


@admin.register(Dismissal)
class DismissalAdmin(admin.ModelAdmin):
    pass


@admin.register(Vocation)
class VocationAdmin(admin.ModelAdmin):
    pass


@admin.register(VocationType)
class VocationTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Voivodship)
class VoivodshipAdmin(admin.ModelAdmin):
    pass


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    pass


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    pass


@admin.register(BasisList)
class BasisListAdmin(admin.ModelAdmin):
    pass
