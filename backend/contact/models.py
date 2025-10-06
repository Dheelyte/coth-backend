from django.db import models

class ContactUs(models.Model):
    CARE_CHOICES = [
        ("self", "For Myself"),
        ("loved_one", "For a Loved One"),
    ]

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    best_time_to_call = models.CharField(max_length=20)
    town_city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    how_did_you_hear_about_us = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Optional: Let us know how you found us",
    )
    message_subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    care_for = models.CharField(max_length=20, choices=CARE_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.message_subject or 'No Subject'}"
