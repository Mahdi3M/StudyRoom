from django.urls import path
from dictionary import views

urlpatterns = [
    path('', views.dictionary_page, name="dictionary_page"),
]
