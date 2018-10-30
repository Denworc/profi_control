from django.urls import path, include, re_path
from .views import (
    DismissalCreateView,
    AssignmentCreateView,
    AdoptionCreateView,
    TransferCreateView,
    PermissionCreateView,
    VnosokCreateView,
    VocationCreateView,
    ControlCreateView,
    PrognosisCreateView,
    DisappearanceCreateView,
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
]
