from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView

from dwelling.models import Dwelling
from user_profile.models import User
from .forms import DwellingCreateForm

# Create your views here.


class DwellingCreateView(CreateView):
    # model = UkrainianPassport
    form_class = DwellingCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class DwellingUpdateView(UpdateView):
    model = Dwelling
    form_class = DwellingCreateForm
    pk_url_kwarg = 'count'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))