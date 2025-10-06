from django.urls import path
from .views import (
    ConsultationApplicationCreateView,
)

urlpatterns = [
    path('', ConsultationApplicationCreateView.as_view(), name="consultation-form"),
]
