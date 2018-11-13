from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from certificate.models import Interview, Certificate, Training, Polish, Test
from user_profile.models import User
from .forms import (
    InterviewCreateForm,
    CertificateCreateForm,
    TestCreateForm,
    TrainingCreateForm,
    PolishCreateForm,
)

# Create your views here.


class InterviewCreateView(CreateView):
    form_class = InterviewCreateForm
    model = Interview

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class CertificateCreateView(CreateView):
    form_class = CertificateCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class TestCreateView(CreateView):
    form_class = TestCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class TrainingCreateView(CreateView):
    form_class = TrainingCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class PolishCreateView(CreateView):
    form_class = PolishCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class InterviewUpdateView(UpdateView):
    form_class = InterviewCreateForm
    model = Interview
    pk_url_kwarg = 'count'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class CertificateUpdateView(UpdateView):
    form_class = CertificateCreateForm
    pk_url_kwarg = 'count'
    model = Certificate

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class TestUpdateView(UpdateView):
    form_class = TestCreateForm
    pk_url_kwarg = 'count'
    model = Test

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class TrainingUpdateView(UpdateView):
    form_class = TrainingCreateForm
    pk_url_kwarg = 'count'
    model = Training

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class PolishUpdateView(UpdateView):
    form_class = PolishCreateForm
    pk_url_kwarg = 'count'
    model = Polish

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class InterviewDeleteView(DeleteView):
    model = Interview
    pk_url_kwarg = 'count'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))


class CertificateDeleteView(DeleteView):
    pk_url_kwarg = 'count'
    model = Certificate

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))


class TestDeleteView(DeleteView):
    pk_url_kwarg = 'count'
    model = Test

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))


class TrainingDeleteView(DeleteView):
    pk_url_kwarg = 'count'
    model = Training

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))


class PolishDeleteView(DeleteView):
    pk_url_kwarg = 'count'
    model = Polish

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))
