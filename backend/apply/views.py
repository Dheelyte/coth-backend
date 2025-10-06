from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.urls import reverse
from rest_framework import generics, permissions
from .models import JobApplication
from .serializers import (
    JobApplicationSerializer
)


class JobApplicationCreateView(generics.CreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        instance = serializer.save()
        admin_url = self.request.build_absolute_uri(
            reverse("admin:apply_jobapplication_changelist")
        )

        context = {
            "instance": instance,
            "admin_url": admin_url
        }
        # Build admin link dynamically
        

        # Render HTML content
        text_content = render_to_string('job_application.txt', context)
        html_content = render_to_string('job_application.html', context)

        subject = "New Job Application"
        from_email=settings.EMAIL_HOST_USER
        to_email = [settings.EMAIL_HOST_USER]

        # Create email
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=from_email,
            to=to_email
        )
        email.attach_alternative(html_content, "text/html")
        email.send()