from django.urls import path

from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register_user/',views. register_user, name="register_user"),
    path('about/', views.about, name='about'),
    # path('contact', views.contact)
  
    
]