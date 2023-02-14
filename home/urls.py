from django.urls import path
from home import views

urlpatterns = [
    path('', views.home_page, name="home_page"), #front_page
    path('register/', views.register_page, name="register_page"), #sign_up
    path('logout', views.log_out, name="logout"),
]
