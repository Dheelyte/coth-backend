from django.contrib import admin
from .models import Article
from django import forms
from ckeditor.widgets import CKEditorWidget


admin.site.site_header = "City On The Hill Care Admin"        # top-left header
admin.site.site_title = "City On The Hill Care Admin Portal" # browser tab title
admin.site.index_title = "Welcome to City On The Hill Care Dashboard"  # index page title


class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            # Add CKEditor widget for content field
            'content': CKEditorWidget(),
        }

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ('title', 'published', 'created_at', 'updated_at')
    list_filter = ('published', 'created_at')
    search_fields = ('title', 'content',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'thumbnail')
        }),
        ('Content', {
            'fields': ('content',)
        }),
        ('Publication', {
            'fields': ('published',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    actions = ['make_published', 'make_unpublished']
    
    def make_published(self, request, queryset):
        updated = queryset.update(published=True)
        self.message_user(request, f'{updated} articles were successfully published.')
    make_published.short_description = "Mark selected articles as published"
    
    def make_unpublished(self, request, queryset):
        updated = queryset.update(published=False)
        self.message_user(request, f'{updated} articles were successfully unpublished.')
    make_unpublished.short_description = "Mark selected articles as unpublished"

# Register models
admin.site.register(Article, ArticleAdmin)
