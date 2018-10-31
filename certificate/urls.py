from django.urls import path, include, re_path
from .views import (
    InterviewCreateView,
    CertificateCreateView,
    TestCreateView,
    TrainingCreateView,
    PolishCreateView,
)


app_name = 'certificate'
urlpatterns = [
    re_path(r'^create_interview/(?P<pk>\d+)$', InterviewCreateView.as_view(), name='create_interview'),
    re_path(r'^create_certificate/(?P<pk>\d+)$', CertificateCreateView.as_view(), name='create_certificate'),
    re_path(r'^create_test/(?P<pk>\d+)$', TestCreateView.as_view(), name='create_test'),
    re_path(r'^create_training/(?P<pk>\d+)$', TrainingCreateView.as_view(), name='create_training'),
    re_path(r'^create_polish/(?P<pk>\d+)$', PolishCreateView.as_view(), name='create_polish'),

]
