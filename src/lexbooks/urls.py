"""lexbooks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from pages.views import home_view, ephemera_view, about_view
from episodes.views import episode_library, episode_detail, book_detail, book_library

urlpatterns = [
    path('', home_view, name='home'),

    path('library/', book_library, name='books'),
    path('library/<int:pk>/', book_detail, name='book_detail'),

    path('episodes/', episode_library, name='episodes'),
    path('episodes/<int:pk>/', episode_detail, name='episode_detail'),

    path('ephemera/', ephemera_view, name='ephemera'),

    path('about/', about_view, name='about'),
    path('admin/', admin.site.urls),
]
