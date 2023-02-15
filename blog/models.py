from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone

# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    f_name = models.CharField(max_length=100, blank=True)
    l_name = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name='blog')
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        author = self.author
        self.f_name = author.first_name
        self.l_name = author.last_name

        super(Blog, self).save(*args, **kwargs)


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name='comments')
    blog = models.ForeignKey("Blog", on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-created"]


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default=" ")
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name='categories')
    blogs = models.ManyToManyField("Blog", related_name='categories')

    class Meta:
        verbose_name_plural = "Categories"
