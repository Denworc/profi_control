from django.urls import path, include, re_path
from .views import (
    AuthView,
    user_logout,
    UserListView,
    # UserDetailView,
    NewUserView,
    # new_user,
    user_detail_view,
)


app_name = 'user'
urlpatterns = [
    path('login/', AuthView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('users/', UserListView.as_view(), name='users'),
    path('new/', NewUserView.as_view(), name='new-user'),
    # path('new/', new_user, name='new-user'),
    # re_path(r'^(?P<pk>\d+)$', UserDetailView.as_view(), name='user-detail'),
    re_path(r'^(?P<pk>\d+)$', user_detail_view, name='user-detail'),
    # path('new_user/', UserListView.as_view(), name='new_user'),
]
