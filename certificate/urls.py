from django.urls import path, include, re_path
from .views import (
    InterviewCreateView,
    CertificateCreateView,
    TestCreateView,
    TrainingCreateView,
    PolishCreateView,
    InterviewUpdateView,
    CertificateUpdateView,
    TestUpdateView,
    TrainingUpdateView,
    PolishUpdateView
)


app_name = 'certificate'
urlpatterns = [
    re_path(r'^create_interview/(?P<pk>\d+)$', InterviewCreateView.as_view(), name='create_interview'),
    re_path(r'^create_certificate/(?P<pk>\d+)$', CertificateCreateView.as_view(), name='create_certificate'),
    re_path(r'^create_test/(?P<pk>\d+)$', TestCreateView.as_view(), name='create_test'),
    re_path(r'^create_training/(?P<pk>\d+)$', TrainingCreateView.as_view(), name='create_training'),
    re_path(r'^create_polish/(?P<pk>\d+)$', PolishCreateView.as_view(), name='create_polish'),
    re_path(r'^update_interview/(?P<pk>\d+)-(?P<count>\d+)$', InterviewUpdateView.as_view(), name='update_interview'),
    re_path(
        r'^update_certificate/(?P<pk>\d+)-(?P<count>\d+)$',
        CertificateUpdateView.as_view(),
        name='update_certificate'
    ),
    re_path(r'^update_test/(?P<pk>\d+)-(?P<count>\d+)$', TestUpdateView.as_view(), name='update_test'),
    re_path(r'^update_training/(?P<pk>\d+)-(?P<count>\d+)$', TrainingUpdateView.as_view(), name='update_training'),
    re_path(r'^update_polish/(?P<pk>\d+)-(?P<count>\d+)$', PolishUpdateView.as_view(), name='update_polish'),

]
