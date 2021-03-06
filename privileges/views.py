from django.shortcuts import redirect
from django.views.generic.edit import CreateView

from user_profile.models import User
from .forms import QuotaCreateForm

# Create your views here.


class QuotaCreateView(CreateView):
    # model = UkrainianPassport
    form_class = QuotaCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return redirect(self.request.META.get('HTTP_REFERER'))

    def form_invalid(self, form):
        return redirect(self.request.META.get('HTTP_REFERER'))
