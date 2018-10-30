from django.urls import path, include, re_path
from .views import (
    InterviewCreateView,

)


app_name = 'certificate'
urlpatterns = [
    re_path(r'^create_interview/(?P<pk>\d+)$', InterviewCreateView.as_view(), name='create_interview'),

]
