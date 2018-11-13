from django.urls import path, include, re_path
from .views import (
    DismissalCreateView, AssignmentCreateView, AdoptionCreateView,
    TransferCreateView, PermissionCreateView, VnosokCreateView,
    VocationCreateView, ControlCreateView, PrognosisCreateView,
    DisappearanceCreateView, DisappearanceUpdateView, PrognosisUpdateView,
    ControlUpdateView, VocationUpdateView, PermissionUpdateView,
    TransferUpdateView, AdoptionUpdateView, AssignmentUpdateView,
    DismissalUpdateView, DisappearanceDeleteView, PrognosisDeleteView,
    ControlDeleteView, VocationDeleteView, PermissionDeleteView,
    TransferDeleteView, AdoptionDeleteView, AssignmentDeleteView,
    DismissalDeleteView,
)


app_name = 'work'
urlpatterns = [
    re_path(r'^create_dismissal/(?P<pk>\d+)$', DismissalCreateView.as_view(), name='create_dismissal'),
    re_path(r'^create_assignment/(?P<pk>\d+)$', AssignmentCreateView.as_view(), name='create_assignment'),
    re_path(r'^create_adoption/(?P<pk>\d+)$', AdoptionCreateView.as_view(), name='create_adoption'),
    re_path(r'^create_transfer/(?P<pk>\d+)$', TransferCreateView.as_view(), name='create_transfer'),
    re_path(r'^create_dismissal/(?P<pk>\d+)$', PermissionCreateView.as_view(), name='create_permission'),
    # re_path(r'^create_vnosok_list/(?P<pk>\d+)$', VnosokCreateView.as_view(), name='create_vnosok_list'),
    re_path(r'^create_vocation/(?P<pk>\d+)$', VocationCreateView.as_view(), name='create_vocation'),
    re_path(r'^create_incoming_control/(?P<pk>\d+)$', ControlCreateView.as_view(), name='create_incoming_control'),
    re_path(r'^create_prognosis/(?P<pk>\d+)$', PrognosisCreateView.as_view(), name='create_prognosis'),
    re_path(r'^create_disappearance/(?P<pk>\d+)$', DisappearanceCreateView.as_view(), name='create_disappearance'),
    re_path(r'^update_dismissal/(?P<pk>\d+)-(?P<count>\d+)$', DismissalUpdateView.as_view(), name='update_dismissal'),
    re_path(r'^update_assignment/(?P<pk>\d+)-(?P<count>\d+)$', AssignmentUpdateView.as_view(), name='update_assignment'),
    re_path(r'^update_adoption/(?P<pk>\d+)-(?P<count>\d+)$', AdoptionUpdateView.as_view(), name='update_adoption'),
    re_path(r'^update_transfer/(?P<pk>\d+)-(?P<count>\d+)$', TransferUpdateView.as_view(), name='update_transfer'),
    re_path(r'^update_dismissal/(?P<pk>\d+)-(?P<count>\d+)$', PermissionUpdateView.as_view(), name='update_permission'),
    # re_path(r'^update_vnosok_list/(?P<pk>\d+)$', VnosokUpdateView.as_view(), name='update_vnosok_list'),
    re_path(r'^update_vocation/(?P<pk>\d+)-(?P<count>\d+)$', VocationUpdateView.as_view(), name='update_vocation'),
    re_path(r'^update_incoming_control/(?P<pk>\d+)-(?P<count>\d+)$', ControlUpdateView.as_view(), name='update_incoming_control'),
    re_path(r'^update_prognosis/(?P<pk>\d+)-(?P<count>\d+)$', PrognosisUpdateView.as_view(), name='update_prognosis'),
    re_path(r'^update_disappearance/(?P<pk>\d+)-(?P<count>\d+)$', DisappearanceUpdateView.as_view(), name='update_disappearance'),
    re_path(r'^delete_dismissal/(?P<pk>\d+)-(?P<count>\d+)$', DismissalDeleteView.as_view(), name='delete_dismissal'),
    re_path(r'^delete_assignment/(?P<pk>\d+)-(?P<count>\d+)$', AssignmentDeleteView.as_view(),
            name='delete_assignment'),
    re_path(r'^delete_adoption/(?P<pk>\d+)-(?P<count>\d+)$', AdoptionDeleteView.as_view(), name='delete_adoption'),
    re_path(r'^delete_transfer/(?P<pk>\d+)-(?P<count>\d+)$', TransferDeleteView.as_view(), name='delete_transfer'),
    re_path(r'^delete_dismissal/(?P<pk>\d+)-(?P<count>\d+)$', PermissionDeleteView.as_view(), name='delete_permission'),
    # re_path(r'^delete_vnosok_list/(?P<pk>\d+)$', VnosokDeleteView.as_view(), name='delete_vnosok_list'),
    re_path(r'^delete_vocation/(?P<pk>\d+)-(?P<count>\d+)$', VocationDeleteView.as_view(), name='delete_vocation'),
    re_path(r'^delete_incoming_control/(?P<pk>\d+)-(?P<count>\d+)$', ControlDeleteView.as_view(),
            name='delete_incoming_control'),
    re_path(r'^delete_prognosis/(?P<pk>\d+)-(?P<count>\d+)$', PrognosisDeleteView.as_view(), name='delete_prognosis'),
    re_path(r'^delete_disappearance/(?P<pk>\d+)-(?P<count>\d+)$', DisappearanceDeleteView.as_view(),
            name='delete_disappearance'),
]