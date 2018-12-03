from django.contrib import admin
from .models import User, Contact, ContactType, Position, Status, Language, LanguageTitle, LanguageLevel, \
    PsychologicalPortrait, IntelligenceType, ProfessionalismType, SelfDiscipline, SociabilityType, TemperamentType, \
    PersonalityType
from documents.models import UkrainianPassport, ForeignPassport


# TODO Прочитати про TabularInline
class ContactInline(admin.TabularInline):
    extra = 0
    model = Contact


class UkrainianPassportInline(admin.StackedInline):
    extra = 0
    model = UkrainianPassport


class ForeignPassportInline(admin.StackedInline):
    extra = 0
    model = ForeignPassport


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('groups', 'user_permissions')
    list_display = (
        'email',
        'first_name',
        'last_name',
        'patronymic',
        'date_of_birth',
        'is_admin',
    )
    inlines = [
        ContactInline,
        UkrainianPassportInline,
        ForeignPassportInline,
]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'contact',
        'type',
    )


@admin.register(ContactType)
class ContactTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(LanguageTitle)
class LanguageTitleAdmin(admin.ModelAdmin):
    pass


@admin.register(LanguageLevel)
class LanguageLevelAdmin(admin.ModelAdmin):
    pass


@admin.register(PsychologicalPortrait)
class PsychologicalPortraitAdmin(admin.ModelAdmin):
    pass


@admin.register(IntelligenceType)
class IntelligenceTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ProfessionalismType)
class ProfessionalismTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(SelfDiscipline)
class SelfDisciplineAdmin(admin.ModelAdmin):
    pass


@admin.register(SociabilityType)
class SociabilityTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(TemperamentType)
class TemperamentTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(PersonalityType)
class PersonalityTypeAdmin(admin.ModelAdmin):
    pass
