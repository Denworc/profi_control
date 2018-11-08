from django.urls import path, include, re_path
from .views import (
    AuthView,
    user_logout,
    UserListView,
    # UserDetailView,
    NewUserView,
    # new_user,
    user_detail_view,
    NoteCreateView,
    ContactCreateView,
    LanguageCreateView,
    UserEditView,
    NoteUpdateView,
    ContactUpdateView,
    LanguageUpdateView)


app_name = 'user'
urlpatterns = [
    path('login/', AuthView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('users/', UserListView.as_view(), name='users'),
    path('new/', NewUserView.as_view(), name='new-user'),
    re_path(r'^note_create/(?P<pk>\d+)$', NoteCreateView.as_view(), name='note-create'),
    re_path(r'^contact_create/(?P<pk>\d+)$', ContactCreateView.as_view(), name='contact-create'),
    re_path(r'^language_create/(?P<pk>\d+)$', LanguageCreateView.as_view(), name='language-create'),
    re_path(r'^note_update/(?P<pk>\d+)$', NoteUpdateView.as_view(), name='note-update'),
    re_path(r'^contact_update/(?P<pk>\d+)-(?P<count>\d+)$', ContactUpdateView.as_view(), name='contact-update'),
    re_path(r'^language_update/(?P<pk>\d+)-(?P<count>\d+)$', LanguageUpdateView.as_view(), name='language-update'),
    re_path(r'^user_edit/(?P<pk>\d+)$', UserEditView.as_view(), name='user-edit'),
    # path('new/', new_user, name='new-user'),
    # re_path(r'^(?P<pk>\d+)$', UserDetailView.as_view(), name='user-detail'),
    re_path(r'^(?P<pk>\d+)$', user_detail_view, name='user-detail'),
    # path('new_user/', UserListView.as_view(), name='new_user'),
]
