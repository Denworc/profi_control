from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# from documents.models import UkrainianPassport
from documents.models import PersonalID, ForeignPassport, Visa, UkrainianPassport
from user_profile.models import User
from .forms import UAPassportCreateForm, ForeignPassportCreateForm, VisaCreateForm, PersonalIDCreateForm


class UAPassportCreate(CreateView):
    # model = UkrainianPassport
    form_class = UAPassportCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))
    #
    # def get_success_url(self):
    #     return reverse('user:user-detail', kwargs={'pk': self.object.pk})


class ForeignPassportCreate(CreateView):
    # model = UkrainianPassport
    form_class = ForeignPassportCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class VisaCreateView(CreateView):
    # model = UkrainianPassport
    form_class = VisaCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class PersonalIDCreateView(CreateView):
    # model = UkrainianPassport
    form_class = PersonalIDCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class UAPassportUpdate(UpdateView):
    model = UkrainianPassport
    form_class = UAPassportCreateForm
    pk_url_kwarg = 'count'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))
    #
    # def get_success_url(self):
    #     return reverse('user:user-detail', kwargs={'pk': self.object.pk})


class ForeignPassportUpdate(UpdateView):
    model = ForeignPassport
    form_class = ForeignPassportCreateForm
    pk_url_kwarg = 'count'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class VisaUpdateView(UpdateView):
    model = Visa
    form_class = VisaCreateForm
    pk_url_kwarg = 'count'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class PersonalIDUpdateView(UpdateView):
    model = PersonalID
    form_class = PersonalIDCreateForm
    pk_url_kwarg = 'count'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class UAPassportDelete(DeleteView):
    model = UkrainianPassport
    pk_url_kwarg = 'count'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))


class ForeignPassportDelete(DeleteView):
    model = ForeignPassport
    pk_url_kwarg = 'count'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))


class VisaDeleteView(DeleteView):
    model = Visa
    pk_url_kwarg = 'count'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))


class PersonalIDDeleteView(DeleteView):
    model = PersonalID
    pk_url_kwarg = 'count'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))

