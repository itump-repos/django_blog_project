"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.views.generic.base import View
from blog_project.blogs.views import PostUpdateView
from blogs.views import PostListView, PostDetailView, PostCreateView, PostUpdateView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('posts/<int:pk>/', PostDetailView.as_view(), name='PostDetail'),
    path('', PostListView.as_view(), name='PostList'),
    path('admin/', admin.site.urls),
    path('create/', PostCreateView.as_view(), name='CreatePost'),
    path('update/<int:pk', PostUpdateView.as_view(), name='PostUpdate'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
