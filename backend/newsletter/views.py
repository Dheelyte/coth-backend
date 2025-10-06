from rest_framework.generics import ListCreateAPIView
from rest_framework import permissions
from rest_framework.response import Response
from .models import Newsletter
from .serializers import NewsletterSerializer


class NewsletterListCreateView(ListCreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        # Example: Prevent duplicate email subscriptions
        email = serializer.validated_data.get("email")
        if not Newsletter.objects.filter(email=email).exists():
            serializer.save()

    def list(self, request, *args, **kwargs):
        """
        Return a flat list of emails instead of objects.
        """
        queryset = self.get_queryset()
        emails = queryset.values_list("email", flat=True)
        return Response(list(emails))