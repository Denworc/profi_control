from django.urls import path, include, re_path
from .views import (
        DwellingCreateView
)


app_name = 'dwelling'
urlpatterns = [
    re_path(r'^create_dwelling/(?P<pk>\d+)$', DwellingCreateView.as_view(), name='create_dwelling'),
]
