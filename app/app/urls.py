"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import re_path as url
from src import views as app_views


urlpatterns = [
    path('admin', admin.site.urls),
    url(r'^api/register', app_views.register, name="register"),
    url(r'^api/users$', app_views.users, name="users"),
    url(r'^api/user$', app_views.user, name="user"),
    url(r'^api/ping', app_views.ping),
    url(r'^', app_views.index),
]
