from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog, Comment, Category
from django.utils.text import slugify


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    slug = serializers.ReadOnlyField()
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    read_only_fields = ["author", "first_name", "last_name"]

    class Meta:
        model = Blog
        fields = ["id", "title", "content", "status", "author", "comments",  "image",
                  "created_on", "updated_on", "author_first_name", "author_last_name", "slug"]


    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = self.context["request"].user
        if not user.is_authenticated:
            data.pop("slug")
        return data


    def save_author(self, **kwargs):
        if "author" not in self.validated_data:
            self.validated_data["author"] = self.context["request"].user
            return super().save(**kwargs)
    def save(self,**kwargs):
        self.validated_data["slug"] = slugify(self.validated_data.get("title"))
        return super().save(**kwargs)


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

