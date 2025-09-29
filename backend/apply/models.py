from django.db import models

class JobApplication(models.Model):
    WORK_AVAILABILITY_CHOICES = [
        ("full_time", "Full-time"),
        ("part_time", "Part-time"),
        ("weekends", "Weekends"),
        ("overnights", "Overnights"),
        ("live_in", "Live-in care"),
    ]

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    role_applied_for = models.CharField(max_length=255, blank=True, null=True)
    preferred_location = models.CharField(max_length=255, blank=True, null=True)

    has_experience = models.BooleanField(default=False)
    experience_summary = models.TextField(blank=True, null=True)

    certifications = models.TextField(
        blank=True, 
        null=True,
        help_text="E.g., First Aid, NVQ"
    )

    availability = models.CharField(
        max_length=20,
        choices=WORK_AVAILABILITY_CHOICES,
        blank=True,
        null=True,
    )

    eligible_to_work = models.BooleanField(default=False)
    start_date = models.DateField(blank=True, null=True)

    additional_info = models.TextField(blank=True, null=True)
    cv_resume = models.FileField(upload_to="applications/cv/")

    consent_given = models.BooleanField(
        default=False,
        help_text="Applicant agreed to processing of their data for recruitment purposes"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.role_applied_for or 'Unspecified Role'}"
