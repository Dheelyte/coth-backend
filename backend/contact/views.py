from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.urls import reverse
from rest_framework import generics, permissions
from .models import ContactUs
from .serializers import (
    ContactUsSerializer
)


class ContactUsCreateView(generics.CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     instance = serializer.save()
    #     admin_url = self.request.build_absolute_uri(
    #         reverse("admin:contact_contactus_changelist")
    #     )

    #     context = {
    #         "instance": instance,
    #         "admin_url": admin_url
    #     }

    #     # Render HTML content
    #     text_content = render_to_string('new_contact.txt', context)
    #     html_content = render_to_string('new_contact.html', context)

    #     subject = f"New Contact Request from {instance.full_name}"
    #     from_email=settings.EMAIL_HOST_USER
    #     to_email = [settings.EMAIL_HOST_USER]

    #     # Create email
    #     email = EmailMultiAlternatives(
    #         subject=subject,
    #         body=text_content,
    #         from_email=from_email,
    #         to=to_email
    #     )
    #     email.attach_alternative(html_content, "text/html")
    #     email.send()