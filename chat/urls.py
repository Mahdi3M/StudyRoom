from django.urls import path

from . import views

urlpatterns = [
    path('', views.chat, name='rooms'),
    path('<slug:slug>/', views.chat, name='room'),
]