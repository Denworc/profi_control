from django.urls import path, include, re_path
from .views import (
        InsuranceCreateView
)


app_name = 'medicine'
urlpatterns = [
    re_path(r'^create_insurance/(?P<pk>\d+)$', InsuranceCreateView.as_view(), name='create_insurance'),
]
