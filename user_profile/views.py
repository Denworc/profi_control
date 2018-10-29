from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, reverse, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DeleteView, View, DetailView, CreateView, UpdateView
from user_profile.forms import AuthForm, NewUserForm, NoteCreateForm, ContactCreateForm, LanguageCreateForm, \
    UserEditForm
from django.utils.translation import ugettext as _
from documents.forms import UAPassportForm, ForeignPassportForm

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
                return redirect('users')

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


# class UserDetailView(LoginRequiredMixin, DetailView):
#     template_name = 'user_profile/user-detail.html'
#     context_object_name = 'users_list'
#     model = User
#     login_url = reverse_lazy('user:login')


def user_detail_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    ua_passport_form = UAPassportForm
    foreign_passport_form = ForeignPassportForm
    note_create_form = NoteCreateForm
    contact_create_form = ContactCreateForm
    language_create_form = LanguageCreateForm
    user_edit_form = UserEditForm
    return render(request, 'user_profile/user-detail.html', context={
        'user': user,
        'ua_passport_form': ua_passport_form,
        'foreign_passport_form': foreign_passport_form,
        'note_create_form': note_create_form,
        'contact_create_form': contact_create_form,
        'language_create_form': language_create_form,
        'user_edit_form': user_edit_form,
    })


    # def get_context_data(self, *args, **kwargs):
    #     context = super(UserListView, self).get_context_data(*args, **kwargs)
    #     context['ua_passport_form'] = UAPassportForm
    #
    #     return context

# def user_profile(request, pk):
#     user = user_profile.objects.get(pk=pk)
#     return render(request, 'user_profile.html', {'user': user})


class NewUserView(CreateView):
    login_url = reverse_lazy('user:login')
    template_name = 'user_profile/add_user.html'
    form_class = NewUserForm

    def get_success_url(self):
        return reverse('user:user-detail', kwargs={'pk': self.object.pk})

# def new_user(request):
#
#     if request.method == 'POST':
#         email = request.POST['email']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         patronymic = request.POST['patronymic']
#         position = request.POST['position']
#         is_worker = request.POST['is_worker']
#
#         user = User.objects.create(
#             email=email,
#             first_name=first_name,
#             last_name=last_name,
#             patronymic=patronymic,
#             position=position,
#             is_worker=is_worker,
#         )
#
#         return redirect('user:user-detail', pk=user.pk)
#
#     return render(request, 'user_profile/add_user.html')


class NoteCreateView(UpdateView):
    login_url = reverse_lazy('user:note-create')
    # template_name = 'user_profile/add_user.html'
    model = User
    form_class = NoteCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))


class ContactCreateView(CreateView):
    # model = UkrainianPassport
    form_class = ContactCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class LanguageCreateView(CreateView):
    # model = UkrainianPassport
    form_class = LanguageCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class UserEditView(UpdateView):
    login_url = reverse_lazy('user:user-edit')
    # template_name = 'user_profile/add_user.html'
    model = User
    form_class = UserEditForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))