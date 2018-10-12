from django import forms
from django.forms import Form
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from .models import User
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
        attrs={'class': 'form-control', 'type': 'email', 'placeholder': _('Email')}), validators=[validators.EmailValidator])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Password')}))

