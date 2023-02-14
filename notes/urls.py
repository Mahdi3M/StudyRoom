from django.urls import path
from notes import views

urlpatterns = [
    path('', views.notes_page, name="notes_page"),
    path('delete_document/<int:docid>/', views.delete_document, name='delete_document')
]