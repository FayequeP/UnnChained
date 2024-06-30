"""
URL configuration for unchained project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from instagram.views import InstagramView, get_token, get_access_token, home_view, get_user_media_view 
from .views import home_view, pw_protetected_view, dashboard, system_prompts, documents

urlpatterns = [
    path('', home_view, name = "home"),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('get_access_token/', get_access_token, name='get_access_token'),
    path('get_token/', get_token, name='get_token'),
    path('media/', get_user_media_view, name='get_media'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('protected/', pw_protetected_view, name='protected'),
    path('dashboard/', dashboard, name = "dashboard" ),
    path('prompts/', system_prompts, name = "prompts" ),
    path('documents/', documents, name = "documents" ),
]
