"""profi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from profi.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

from user_profile.views import UserListView
from .views import DashboardView


urlpatterns = [
    re_path(r'^jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('cabinet/', include([
        path('user/', include('user_profile.urls')),
        path('', DashboardView.as_view(), name='dashboard'),
    ])),
    path('documents/', include('documents.urls')),
    path('work/', include('work.urls')),
    path('privileges/', include('privileges.urls')),
    path('medicine/', include('medicine.urls')),
    path('dwelling/', include('dwelling.urls')),
    path('certificate/', include('certificate.urls')),
    # path('', DashboardView.as_view(), name='dashboard'),
    path('', UserListView.as_view(), name='users'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
