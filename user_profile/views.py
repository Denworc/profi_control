from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import redirect, reverse, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DeleteView, View, DetailView, CreateView, UpdateView

from certificate.forms import (
    InterviewCreateForm,
    CertificateCreateForm,
    TestCreateForm,
    TrainingCreateForm,
    PolishCreateForm,
    InterviewUpdateForm,
)
from dwelling.forms import DwellingCreateForm
from medicine.forms import InsuranceCreateForm
from privileges.forms import QuotaCreateForm
from work.forms import (
    DismissalCreateForm,
    AssignmentCreateForm,
    AdoptionCreateForm,
    TransferCreateForm,
    PermissionCreateForm,
    VnosokCreateForm,
    VocationCreateForm,
    ControlCreateForm,
    PrognosisCreateForm,
    DisappearanceCreateForm,
)
from user_profile.forms import AuthForm, NewUserForm, NoteCreateForm, ContactCreateForm, LanguageCreateForm, \
    UserEditForm, NoteUpdateForm, ContactUpdateForm, LanguageUpdateForm, ContactTypeCreateForm, LanguageTitleCreateForm, \
    LanguageLevelCreateForm
from django.utils.translation import ugettext as _
from documents.forms import UAPassportCreateForm, ForeignPassportCreateForm, VisaCreateForm, PersonalIDCreateForm

from user_profile.models import User, Contact, Language


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
    ua_passport_form = UAPassportCreateForm
    foreign_passport_form = ForeignPassportCreateForm
    note_create_form = NoteCreateForm
    note_update_form = NoteUpdateForm(initial={'note': user.note})
    contact_create_form = ContactCreateForm
    language_create_form = LanguageCreateForm
    user_edit_form = UserEditForm(pk)
    interview_create_form = InterviewCreateForm
    dwelling_create_form = DwellingCreateForm
    insurance_create_form = InsuranceCreateForm
    quota_create_form = QuotaCreateForm
    dismissal_create_form = DismissalCreateForm
    assignment_create_form = AssignmentCreateForm
    adoption_create_form = AdoptionCreateForm
    transfer_create_form = TransferCreateForm
    permission_create_form = PermissionCreateForm
    # vnosok_create_form = VnosokCreateForm
    vocation_create_form = VocationCreateForm
    control_create_form = ControlCreateForm
    prognosis_create_form = PrognosisCreateForm
    disappearance_create_form = DisappearanceCreateForm
    certificate_create_form = CertificateCreateForm
    test_create_form = TestCreateForm
    training_create_form = TrainingCreateForm
    polish_create_form = PolishCreateForm
    visa_create_form = VisaCreateForm
    id_create_form = PersonalIDCreateForm
    contact_type_create_form = ContactTypeCreateForm
    language_title_create_form = LanguageTitleCreateForm
    language_level_create_form = LanguageLevelCreateForm
    contact_update_form = ContactUpdateForm
    language_update_form = LanguageUpdateForm

    return render(request, 'user_profile/user-detail.html', context={
        'user': user,
        'id_create_form': id_create_form,
        'ua_passport_form': ua_passport_form,
        'foreign_passport_form': foreign_passport_form,
        'note_create_form': note_create_form,
        'contact_create_form': contact_create_form,
        'language_create_form': language_create_form,
        'user_edit_form': user_edit_form,
        'interview_create_form': interview_create_form,
        'dwelling_create_form': dwelling_create_form,
        'insurance_create_form': insurance_create_form,
        'quota_create_form': quota_create_form,
        'dismissal_create_form': dismissal_create_form,
        'assignment_create_form': assignment_create_form,
        'adoption_create_form': adoption_create_form,
        'permission_create_form': permission_create_form,
        'vocation_create_form': vocation_create_form,
        'control_create_form': control_create_form,
        'prognosis_create_form': prognosis_create_form,
        'disappearance_create_form': disappearance_create_form,
        'transfer_create_form': transfer_create_form,
        'certificate_create_form': certificate_create_form,
        'test_create_form': test_create_form,
        'training_create_form': training_create_form,
        'polish_create_form': polish_create_form,
        'visa_create_form': visa_create_form,
        'contact_update_form': contact_update_form,
        'language_update_form': language_update_form,
        'note_update_form': note_update_form,
        'contact_type_create_form': contact_type_create_form,
        'language_title_create_form': language_title_create_form,
        'language_level_create_form': language_level_create_form,

    })

    # def get_context_data(self, *args, **kwargs):
    #     context = super(UserListView, self).get_context_data(*args, **kwargs)
    #     context['ua_passport_form'] = UAPassportForm
    #
    #     return context

# def user_profile(request, pk):
#     user = user_profile.objects.get(pk=pk)
#     return render(request, 'user_profile.html', {'user': user})


class NewUserView(LoginRequiredMixin, CreateView):
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
    #
    # def get_initial(self):
    #     super(NoteCreateView, self).get_initial()
    #     user = User.objects.get(pk=self.kwargs['pk'])
    #     self.initial = {'note': user.note}
    #     return self.initial

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


class ContactTypeCreateView(CreateView):
    # model = UkrainianPassport
    form_class = ContactTypeCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class LanguageTitleCreateView(CreateView):
    # model = UkrainianPassport
    form_class = LanguageTitleCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class LanguageLevelCreateView(CreateView):
    # model = UkrainianPassport
    form_class = LanguageLevelCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
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
    template_name = 'user_profile/add_user.html'
    model = User
    # form_class = UserEditForm
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

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class NoteUpdateView(UpdateView):
    login_url = reverse_lazy('user:note-create')
    model = User
    # form_class = NoteUpdateForm
    fields = (
        'note',
    )

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))


class ContactUpdateView(UpdateView):
    model = Contact
    pk_url_kwarg = 'count'
    context_object_name = 'contact'
    fields = (
        'type',
        'contact',
    )

    def form_valid(self, form):
        contact = form.save(commit=False)
        contact.user = User.objects.get(pk=self.kwargs['pk'])
        contact.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class LanguageUpdateView(UpdateView):
    model = Language
    pk_url_kwarg = 'count'
    fields = (
        'title',
        'level',
    )

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class ContactDeleteView(DeleteView):
    model = Contact
    pk_url_kwarg = 'count'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))

    # context_object_name = 'contact'
    # fields = (
    #     'type',
    #     'contact',
    # )
    #
    # def form_valid(self, form):
    #     contact = self.get_object()
    #     contact.delete()
    #     # contact = form.save(commit=False)
    #     # contact.user = User.objects.get(pk=self.kwargs['pk'])
    #     # contact.save()
    #     return redirect(self.request.META.get('HTTP_REFERER'))
    #
    # def form_invalid(self, form):
    #     return redirect(self.request.META.get('HTTP_REFERER'))
    #
    # def get_success_url(self):
    #     return redirect(self.request.META.get('HTTP_REFERER'))


class LanguageDeleteView(DeleteView):
    model = Language
    pk_url_kwarg = 'count'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))