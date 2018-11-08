from django.urls import path, include, re_path
from .views import (
    InsuranceCreateView,
    InsuranceUpdateView)


app_name = 'medicine'
urlpatterns = [
    re_path(r'^create_insurance/(?P<pk>\d+)$', InsuranceCreateView.as_view(), name='create_insurance'),
    re_path(r'^update_insurance/(?P<pk>\d+)-(?P<count>\d+)$', InsuranceUpdateView.as_view(), name='update_insurance'),
]
