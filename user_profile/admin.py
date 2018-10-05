from django.contrib import admin
from .models import User, Contact, ContactType, Position
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
        'first_name',
        'last_name',
        'patronymic',
        'date_of_birth',
        'position',
        'is_worker',
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


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass
