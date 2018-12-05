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
    PolishUpdateView,
    InterviewDeleteView,
    TestDeleteView,
    TrainingDeleteView,
    PolishDeleteView,
    LocksmithCreateView, WelderCreateView, OtherCreateView, LocksmithUpdateView, WelderUpdateView, OtherUpdateView,
    OtherDeleteView, WelderDeleteView, LocksmithDeleteView, PostOtherDeleteView, PostWelderDeleteView,
    PostLocksmithDeleteView, PostOtherUpdateView, PostWelderUpdateView, PostLocksmithUpdateView, PostOtherCreateView,
    PostWelderCreateView, PostLocksmithCreateView)


app_name = 'certificate'
urlpatterns = [
    re_path(r'^create_interview/(?P<pk>\d+)$', InterviewCreateView.as_view(), name='create_interview'),
    re_path(r'^create_certificate/(?P<pk>\d+)$', CertificateCreateView.as_view(), name='create_certificate'),
    re_path(r'^create_test/(?P<pk>\d+)$', TestCreateView.as_view(), name='create_test'),
    re_path(r'^create_training/(?P<pk>\d+)$', TrainingCreateView.as_view(), name='create_training'),
    re_path(r'^create_polish/(?P<pk>\d+)$', PolishCreateView.as_view(), name='create_polish'),
    re_path(r'^create_locksmith/(?P<pk>\d+)$', LocksmithCreateView.as_view(), name='create_locksmith'),
    re_path(r'^create_welder/(?P<pk>\d+)$', WelderCreateView.as_view(), name='create_welder'),
    re_path(r'^create_other/(?P<pk>\d+)$', OtherCreateView.as_view(), name='create_other'),
    re_path(r'^create_locksmith_post/(?P<pk>\d+)$', PostLocksmithCreateView.as_view(), name='create_locksmith_post'),
    re_path(r'^create_welder_post/(?P<pk>\d+)$', PostWelderCreateView.as_view(), name='create_welder_post'),
    re_path(r'^create_other_post/(?P<pk>\d+)$', PostOtherCreateView.as_view(), name='create_other_post'),
    re_path(r'^update_interview/(?P<pk>\d+)-(?P<count>\d+)$', InterviewUpdateView.as_view(), name='update_interview'),
    re_path(
        r'^update_certificate/(?P<pk>\d+)-(?P<count>\d+)$',
        CertificateUpdateView.as_view(),
        name='update_certificate'
    ),
    re_path(r'^update_test/(?P<pk>\d+)-(?P<count>\d+)$', TestUpdateView.as_view(), name='update_test'),
    re_path(r'^update_training/(?P<pk>\d+)-(?P<count>\d+)$', TrainingUpdateView.as_view(), name='update_training'),
    re_path(r'^update_polish/(?P<pk>\d+)-(?P<count>\d+)$', PolishUpdateView.as_view(), name='update_polish'),
    re_path(r'^update_locksmith/(?P<pk>\d+)-(?P<count>\d+)$', LocksmithUpdateView.as_view(), name='update_locksmith'),
    re_path(r'^update_welder/(?P<pk>\d+)-(?P<count>\d+)$', WelderUpdateView.as_view(), name='update_welder'),
    re_path(r'^update_other/(?P<pk>\d+)-(?P<count>\d+)$', OtherUpdateView.as_view(), name='update_other'),
    re_path(r'^update_locksmith_post/(?P<pk>\d+)-(?P<count>\d+)$', PostLocksmithUpdateView.as_view(), name='update_locksmith_post'),
    re_path(r'^update_welder_post/(?P<pk>\d+)-(?P<count>\d+)$', PostWelderUpdateView.as_view(), name='update_welder_post'),
    re_path(r'^update_other_post/(?P<pk>\d+)-(?P<count>\d+)$', PostOtherUpdateView.as_view(), name='update_other_post'),
    re_path(r'^delete_interview/(?P<pk>\d+)-(?P<count>\d+)$', InterviewDeleteView.as_view(), name='delete_interview'),
    re_path(
        r'^delete_certificate/(?P<pk>\d+)-(?P<count>\d+)$',
        CertificateUpdateView.as_view(),
        name='delete_certificate'
    ),
    re_path(r'^delete_test/(?P<pk>\d+)-(?P<count>\d+)$', TestDeleteView.as_view(), name='delete_test'),
    re_path(r'^delete_training/(?P<pk>\d+)-(?P<count>\d+)$', TrainingDeleteView.as_view(), name='delete_training'),
    re_path(r'^delete_polish/(?P<pk>\d+)-(?P<count>\d+)$', PolishDeleteView.as_view(), name='delete_polish'),
    re_path(r'^delete_locksmith/(?P<pk>\d+)-(?P<count>\d+)$', LocksmithDeleteView.as_view(), name='delete_locksmith'),
    re_path(r'^delete_welder/(?P<pk>\d+)-(?P<count>\d+)$', WelderDeleteView.as_view(), name='delete_welder'),
    re_path(r'^delete_other/(?P<pk>\d+)-(?P<count>\d+)$', OtherDeleteView.as_view(), name='delete_other'),
    re_path(r'^delete_locksmith_post/(?P<pk>\d+)-(?P<count>\d+)$', PostLocksmithDeleteView.as_view(), name='delete_locksmith_post'),
    re_path(r'^delete_welder_post/(?P<pk>\d+)-(?P<count>\d+)$', PostWelderDeleteView.as_view(), name='delete_welder_post'),
    re_path(r'^delete_other_post/(?P<pk>\d+)-(?P<count>\d+)$', PostOtherDeleteView.as_view(), name='delete_other_post'),

]
