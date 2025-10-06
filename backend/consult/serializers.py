from rest_framework import serializers
from .models import ConsultationApplication


class ConsultationApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultationApplication
        fields = "__all__"
        read_only_fields = ["id", "created_at"]