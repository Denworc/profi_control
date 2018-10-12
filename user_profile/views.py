from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DeleteView, View
from user_profile.forms import AuthForm
from django.utils.translation import ugettext as _

from user_profile.models import User


class AuthView(FormView):
    form_class = AuthForm
    template_name = 'user_profile/authentication-signin.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')

        return super(AuthView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('dashboard')

        messages.error(self.request, _('Не верный адрес почты или пароль'), 'danger')
        return redirect(self.request.META.get('HTTP_REFERER'))


def user_logout(request):
    logout(request)
    return redirect('user:login')


class UserListView(LoginRequiredMixin, ListView):
    template_name = 'user_profile/users-list.html'
    context_object_name = 'users'
    model = User
    login_url = reverse_lazy('user:login')
    # queryset = User.objects.all()

    # <- QuerySet read docs
    # def get_queryset(self):
    #     print('-'*80)
    #     print(self.request.GET.get('param'))
    #     return User.objects.filter(id=self.request.user.id)

    # def get_context_data(self, *args, **kwargs):
    #     context = super(UserListView, self).get_context_data(*args, **kwargs)
    #     context['superpuper'] = 'Blalaasdfdsfsfd'
    #     print('-'*80)
    #     print(context)
    #     return context
