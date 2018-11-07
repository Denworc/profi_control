from django.shortcuts import redirect
from django.views.generic.edit import CreateView

# from documents.models import UkrainianPassport
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
