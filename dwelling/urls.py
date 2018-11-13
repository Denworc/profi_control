from django.urls import path, include, re_path
from .views import (
    DwellingCreateView,
    DwellingUpdateView,
    DwellingDeleteView,
)


app_name = 'dwelling'
urlpatterns = [
    re_path(r'^create_dwelling/(?P<pk>\d+)$', DwellingCreateView.as_view(), name='create_dwelling'),
    re_path(r'^update_dwelling/(?P<pk>\d+)-(?P<count>\d+)$', DwellingUpdateView.as_view(), name='update_dwelling'),
    re_path(r'^delete_dwelling/(?P<pk>\d+)-(?P<count>\d+)$', DwellingDeleteView.as_view(), name='delete_dwelling'),
]
