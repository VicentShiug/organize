from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.on_list_users, name='on_list_users'),
    path('user/<int:id>', views.get_user, name='get_user'),
    path('data/', views.user_manager)
]
