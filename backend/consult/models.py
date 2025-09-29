from django.db import models

class ConsultationApplication(models.Model):
    CONTACT_METHOD_CHOICES = [
        ("phone", "Phone"),
        ("email", "Email"),
        ("whatsapp", "WhatsApp"),
    ]

    CONSULTATION_FOR_CHOICES = [
        ("self", "Myself"),
        ("family", "Family Care"),
        ("client", "Client"),
    ]

    HEAR_ABOUT_CHOICES = [
        ("google", "Google Search"),
        ("social_media", "Social Media"),
        ("friend", "Friend / Word of Mouth"),
        ("advertisement", "Advertisement"),
        ("other", "Other"),
    ]

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    preferred_contact = models.CharField(max_length=20, choices=CONTACT_METHOD_CHOICES)
    consultation_for = models.CharField(max_length=20, choices=CONSULTATION_FOR_CHOICES)

    type_of_care = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Optional, if known"
    )

    description = models.TextField(
        blank=True,
        null=True,
        help_text="Brief description of needs or questions"
    )

    preferred_datetime = models.DateTimeField(
        blank=True,
        null=True,
        help_text="Preferred consultation date & time"
    )

    how_did_you_hear = models.CharField(
        max_length=50,
        choices=HEAR_ABOUT_CHOICES,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.consultation_for}"
