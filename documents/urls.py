from django.urls import path, include, re_path
from .views import (
    UAPassportCreate,
    ForeignPassportCreate,
    VisaCreateView,
    PersonalIDCreateView,
    PersonalIDUpdateView,
    VisaUpdateView,
    ForeignPassportUpdate,
    UAPassportUpdate,
    UAPassportDelete,
    ForeignPassportDelete,
    VisaDeleteView,
    PersonalIDDeleteView,
)


app_name = 'documents'
urlpatterns = [
    re_path(r'^create_ua_passport/(?P<pk>\d+)$', UAPassportCreate.as_view(), name='create_ua_passport'),
    re_path(r'^create_foreign_passport/(?P<pk>\d+)$', ForeignPassportCreate.as_view(), name='create_foreign_passport'),
    re_path(r'^create_visa/(?P<pk>\d+)$', VisaCreateView.as_view(), name='create_visa'),
    re_path(r'^create_id/(?P<pk>\d+)$', PersonalIDCreateView.as_view(), name='create_id'),
    re_path(r'^update_ua_passport/(?P<pk>\d+)-(?P<count>\d+)$', UAPassportUpdate.as_view(), name='update_ua_passport'),
    re_path(r'^update_foreign_passport/(?P<pk>\d+)-(?P<count>\d+)$', ForeignPassportUpdate.as_view(), name='update_foreign_passport'),
    re_path(r'^update_visa/(?P<pk>\d+)-(?P<count>\d+)$', VisaUpdateView.as_view(), name='update_visa'),
    re_path(r'^update_id/(?P<pk>\d+)-(?P<count>\d+)$', PersonalIDUpdateView.as_view(), name='update_id'),
    re_path(r'^delete_ua_passport/(?P<pk>\d+)-(?P<count>\d+)$', UAPassportDelete.as_view(), name='delete_ua_passport'),
    re_path(r'^delete_foreign_passport/(?P<pk>\d+)-(?P<count>\d+)$', ForeignPassportDelete.as_view(),
            name='delete_foreign_passport'),
    re_path(r'^delete_visa/(?P<pk>\d+)-(?P<count>\d+)$', VisaDeleteView.as_view(), name='delete_visa'),
    re_path(r'^delete_id/(?P<pk>\d+)-(?P<count>\d+)$', PersonalIDDeleteView.as_view(), name='delete_id'),
]
