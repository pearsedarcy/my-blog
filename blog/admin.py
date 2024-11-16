from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ("published", "title", "slug", "author", "created", "updated")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    date_hierarchy = "created"
    ordering = ("created",)
    published = ("Published",)
    summernote_fields = ('body',)
    list_filter = ("published",)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("approved", "body", "post", "author", "created", "updated")
    search_fields = ("author", "body")
    raw_id_fields = ("author",)
    date_hierarchy = "created"
    ordering = ("created",)
    approved = ("Approved",)
    list_filter = ("approved",)