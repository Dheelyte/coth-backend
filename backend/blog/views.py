from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Article
from .serializers import ArticleSerializer


class ArticleListView(ListAPIView):
    queryset = Article.objects.filter(published=True)
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]


class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    lookup_field = 'slug'
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]