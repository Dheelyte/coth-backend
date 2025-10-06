from rest_framework import serializers
from .models import JobApplication

class JobApplicationSerializer(serializers.ModelSerializer):
    cv_resume = serializers.FileField(required=True)

    class Meta:
        model = JobApplication
        fields = "__all__"
        read_only_fields = ["id", "created_at"]