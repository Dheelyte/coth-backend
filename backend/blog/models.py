from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
from .utils import article_thumbnail_path


class Article(models.Model):
    """
    Article model for blog posts
    """
    title = models.CharField(
        max_length=255
    )
    slug = models.SlugField(max_length=265, editable=False, unique=True, blank=True)
    content = RichTextField()
    thumbnail = models.ImageField(
        upload_to=article_thumbnail_path,
        blank=True,
        null=True,
        help_text="Upload a thumbnail image for this article (recommended: 1200x630px)",
        max_length=500
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    published_at = models.DateTimeField(editable=False, null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['published']),
        ]
        permissions = [
            ('can_publish', 'Can publish articles'),
        ]
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        """
        Auto-generate slug from title if not provided
        Set published_at timestamp when article is published
        """
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Article.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
        
        # Set published_at time when article is first published
        if self.published and not self.published_at:
            self.published_at = timezone.now()
        elif not self.published:
            self.published_at = None
            
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})
    
    @property
    def is_published(self):
        """Check if article is published and published date is not in future"""
        if self.published and self.published_at:
            return self.published_at <= timezone.now()
        return False
    
    @property
    def reading_time(self):
        """Estimate reading time based on word count"""
        words_per_minute = 200
        word_count = len(self.content.split())
        reading_time = max(1, round(word_count / words_per_minute))
        return f"{reading_time} min read"
    
    @property
    def thumbnail_url(self):
        """Return thumbnail URL or default image if not available"""
        if self.thumbnail:
            return self.thumbnail.url
        return None