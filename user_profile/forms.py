from django import forms
from django.forms import Form
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from .models import User, Language, Contact, ContactType, LanguageLevel, LanguageTitle
from django.contrib.auth.hashers import check_password


names_validator = validators.RegexValidator('^[a-zA-Zа-яА-Я]+$', message=_(
        'Допускаются только латинские и кирилические символы нижнего и верхнего регистра'
    ))

phone_validator = validators.RegexValidator('^[0-9]+')
password_validator = validators.MinLengthValidator(10)


# class ForgotPasswordForm(Form):
#     """
#     Форма востановления пароля
#     """
#
#     error_css_class = 'is-invalid'
#     errors_class = 'is-invalid'
#
#     email = forms.EmailField(label=_('Email'), widget=forms.TextInput(
#         attrs={'class': 'form-control'},
#     ), validators=[validators.EmailValidator])
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if User.objects.filter(email__contains=email).exists():
#             return email
#         raise forms.ValidationError(_('Такой адрес електронной почты не используется'))


class AuthForm(Form):
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'email',
               'placeholder': _('Email')}), validators=[validators.EmailValidator])
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': _('Password')}))


class NewUserForm(forms.ModelForm):
    # polygon = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'patronymic',
            'position',
        )


class NoteCreateForm(forms.ModelForm):
    # polygon = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = User
        fields = (
            'note',
        )

    # def __init__(self, pk, *args, **kwargs):
    #     super(NoteCreateForm, self).__init__(*args, **kwargs)
    #     user = User.objects.get(pk=pk)
    #     self.fields['note'].initial = user.note

    # def get_initial_for_field(self, field, field_name):
    #     user = User.objects.get(pk=kwargs.pop('pk'))


class ContactCreateForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            'type',
            'contact',
        )


class LanguageCreateForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = (
            'title',
            'level',
        )


class ContactTypeCreateForm(forms.ModelForm):

    class Meta:
        model = ContactType
        fields = (
            'title',
        )


class LanguageTitleCreateForm(forms.ModelForm):

    class Meta:
        model = LanguageTitle
        fields = (
            'title',
        )


class LanguageLevelCreateForm(forms.ModelForm):

    class Meta:
        model = LanguageLevel
        fields = (
            'title',
        )


class UserEditForm(forms.ModelForm):
    # polygon = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = User
        fields = (
            'avatar',
            'email',
            'first_name',
            'last_name',
            'patronymic',
            'position',
            'status',
            'date_of_birth',
            'registration',
            'residence_address',
        )

    def __init__(self, pk, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        user = User.objects.get(pk=pk)
        self.fields['avatar'].initial = user.avatar
        self.fields['email'].initial = user.email
        self.fields['first_name'].initial = user.first_name
        self.fields['last_name'].initial = user.last_name
        self.fields['position'].initial = user.position
        self.fields['patronymic'].initial = user.patronymic
        self.fields['status'].initial = user.status
        self.fields['date_of_birth'].initial = user.date_of_birth
        self.fields['registration'].initial = user.registration
        self.fields['residence_address'].initial = user.residence_address


class NoteUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'note',
        )


class ContactUpdateForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            'type',
            'contact',
        )

    # def __init__(self, pk, *args, **kwargs):
    #     super(ContactUpdateForm, self).__init__(*args, **kwargs)
    #     user = User.objects.get(pk=pk)
    #     contact = user.contacts.first()
    #     # print('-' * 80)
    #     # print(contact)
    #     # print('-' * 80)
    #     if contact:
    #         self.fields['type'].initial = contact.type
    #         self.fields['contact'].initial = contact.contact


class LanguageUpdateForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = (
            'title',
            'level',
        )

    # def __init__(self, pk, *args, **kwargs):
    #     super(LanguageUpdateForm, self).__init__(*args, **kwargs)
    #     user = User.objects.get(pk=pk)
    #     language = user.languages.first()
    #     if language:
    #         self.fields['title'].initial = language.title
    #         self.fields['level'].initial = language.level
