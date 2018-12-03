import re

from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from user_profile.models import User, Status
from work.models import Dismissal, Assignment, AdoptionInState, Permission, TransferInState, Vnosok, Vocation, \
    IncomingControl, Prognosis, Disappearance
from .forms import (
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
    VoivodshipCreateForm, EmployerCreateForm, FactoryCreateForm)

# Create your views here.


class DismissalCreateView(CreateView):
    form_class = DismissalCreateForm

    def form_valid(self, form):
        # form.fields['dismissal_date'].value = re.sub('[^0-9]', '.', form.fields['dismissal_date'].value)
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class AssignmentCreateView(CreateView):
    form_class = AssignmentCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class AdoptionCreateView(CreateView):
    form_class = AdoptionCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        user = User.objects.get(pk=self.kwargs['pk'])
        user.status = Status.objects.get(pk=4)
        user.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class VoivodshipCreateView(CreateView):
    form_class = VoivodshipCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class EmployerCreateView(CreateView):
    form_class = EmployerCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class FactoryCreateView(CreateView):
    form_class = FactoryCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class TransferCreateView(CreateView):
    form_class = TransferCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class PermissionCreateView(CreateView):
    form_class = PermissionCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class VnosokCreateView(CreateView):
    form_class = VnosokCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class VocationCreateView(CreateView):
    form_class = VocationCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class ControlCreateView(CreateView):
    form_class = ControlCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class PrognosisCreateView(CreateView):
    form_class = PrognosisCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class DisappearanceCreateView(CreateView):
    form_class = DisappearanceCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class DismissalUpdateView(UpdateView):
    form_class = DismissalCreateForm
    pk_url_kwarg = 'count'
    model = Dismissal

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class AssignmentUpdateView(UpdateView):
    form_class = AssignmentCreateForm
    pk_url_kwarg = 'count'
    model = Assignment

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class AdoptionUpdateView(UpdateView):
    form_class = AdoptionCreateForm
    pk_url_kwarg = 'count'
    model = AdoptionInState

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        user = User.objects.get(pk=self.kwargs['pk'])
        user.status = Status.objects.get(pk=4)
        user.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class TransferUpdateView(UpdateView):
    form_class = TransferCreateForm
    pk_url_kwarg = 'count'
    model = TransferInState

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class PermissionUpdateView(UpdateView):
    form_class = PermissionCreateForm
    pk_url_kwarg = 'count'
    model = Permission

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class VnosokUpdateView(UpdateView):
    form_class = VnosokCreateForm
    pk_url_kwarg = 'count'
    model = Vnosok

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class VocationUpdateView(UpdateView):
    form_class = VocationCreateForm
    pk_url_kwarg = 'count'
    model = Vocation

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class ControlUpdateView(UpdateView):
    form_class = ControlCreateForm
    pk_url_kwarg = 'count'
    model = IncomingControl

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class PrognosisUpdateView(UpdateView):
    form_class = PrognosisCreateForm
    pk_url_kwarg = 'count'
    model = Prognosis

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class DisappearanceUpdateView(UpdateView):
    form_class = DisappearanceCreateForm
    pk_url_kwarg = 'count'
    model = Disappearance

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class DismissalDeleteView(DeleteView):
    pk_url_kwarg = 'count'
    model = Dismissal

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))


class AssignmentDeleteView(DeleteView):
    pk_url_kwarg = 'count'
    model = Assignment

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))


class AdoptionDeleteView(DeleteView):
    pk_url_kwarg = 'count'
    model = AdoptionInState

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))


class TransferDeleteView(DeleteView):
    pk_url_kwarg = 'count'
    model = TransferInState

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))


class PermissionDeleteView(DeleteView):
    pk_url_kwarg = 'count'
    model = Permission

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))


class VnosokDeleteView(DeleteView):
    pk_url_kwarg = 'count'
    model = Vnosok

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))


class VocationDeleteView(DeleteView):
    pk_url_kwarg = 'count'
    model = Vocation

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))


class ControlDeleteView(DeleteView):
    pk_url_kwarg = 'count'
    model = IncomingControl

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))


class PrognosisDeleteView(DeleteView):
    pk_url_kwarg = 'count'
    model = Prognosis

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))


class DisappearanceDeleteView(DeleteView):
    pk_url_kwarg = 'count'
    model = Disappearance

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))