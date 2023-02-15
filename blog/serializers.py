from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog, Comment, Category
from django.utils.text import slugify


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ["id", "title", "slug", "content", "created_on", "updated_on", "status", "f_name", "l_name", "author",
                  "image", "comments"]
        exclude = ["slug"]


        def save(self, commit=True):
            instance = super().save(commit=False)
            instance.slug = slugify(instance.title)
            if commit:
                instance.save()
            return instance


class UserSerializer(serializers.ModelSerializer):
    blogs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "blogs", "comments"]


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Comment
        fields = ["id", "user", "blog", "created", "updated", "body"]


class CategorySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    blogs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "author", "blogs"]

