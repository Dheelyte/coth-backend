from django.urls import path
from .views import (
    JobApplicationCreateView,
)

urlpatterns = [
    path('', JobApplicationCreateView.as_view(), name="job-application-form"),
]
