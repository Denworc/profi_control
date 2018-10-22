from django.shortcuts import render
from django.views import View


class DashboardView(View):

    def get(self, request):
        context = {
            'name': 'profi',
        }
        return render(request, 'cabinet-base.html', context)
