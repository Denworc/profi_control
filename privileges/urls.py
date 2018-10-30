from django.urls import path, include, re_path
from .views import (
        QuotaCreateView
)


app_name = 'privileges'
urlpatterns = [
    re_path(r'^create_quota/(?P<pk>\d+)$', QuotaCreateView.as_view(), name='create_quota'),
]
