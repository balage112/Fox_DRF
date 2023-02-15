"""Fox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
    path("blogs/", views.BlogList.as_view()),
    path("blogs/<int:pk>/", views.BlogDetail.as_view()),
    path("api-auth/", include("rest_framework.urls")),
    path("comments/", views.CommentList.as_view()),
    path("comments/<int:pk>/", views.CommentDetail.as_view()),
    path("category/", views.CategoryList.as_view()),
    path("category/<int:pk>/", views.CategoryDetail.as_view()),
]

