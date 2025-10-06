from django.urls import path
from .views import (
    ContactUsCreateView
)

urlpatterns = [
    path('', ContactUsCreateView.as_view(), name="contact-form"),
]
