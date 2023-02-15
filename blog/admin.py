from django.contrib import admin
from .models import *

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_on", "updated_on", "status", "slug", "image")
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Blog)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "blog", "content", "created_on")
    list_filter = ("author",)
    search_fields = ["content"]


admin.site.register(Comment)