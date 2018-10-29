from django.urls import path, include, re_path
from .views import (
    UAPassportCreate,
    ForeignPassportCreate,
)


app_name = 'documents'
urlpatterns = [
    re_path(r'^create_ua_passport/(?P<pk>\d+)$', UAPassportCreate.as_view(), name='create_ua_passport'),
    re_path(r'^create_foreign_passport/(?P<pk>\d+)$', ForeignPassportCreate.as_view(), name='create_foreign_passport'),
]
