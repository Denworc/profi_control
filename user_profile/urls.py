from django.urls import path, include, re_path
from .views import (
    AuthView,
    user_logout,
    UserListView,
)


app_name = 'user'
urlpatterns = [
    path('login/', AuthView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('users/', UserListView.as_view(), name='users'),
]
