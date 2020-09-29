"""tmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from .views import (
    api_list_photo_view,
    api_detail_photo_view,
    api_create_photo_view,
    api_update_photo_view,
    api_delete_photo_view,
)

urlpatterns = [
    path('photo/', api_list_photo_view, name='test'),
    path('photo/<int:pk>/', api_detail_photo_view),
    path('create/', api_create_photo_view),
    path('photo/<int:pk>/update/', api_update_photo_view),
    path('photo/<int:pk>/delete/', api_delete_photo_view),
]
