from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from medicine.models import Insurance
from user_profile.models import User
from .forms import InsuranceCreateForm

# Create your views here.


class InsuranceCreateView(CreateView):
    # model = UkrainianPassport
    form_class = InsuranceCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class InsuranceUpdateView(UpdateView):
    model = Insurance
    pk_url_kwarg = 'count'
    form_class = InsuranceCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))


class InsuranceDeleteView(DeleteView):
    model = Insurance
    pk_url_kwarg = 'count'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.request.META.get('HTTP_REFERER'))