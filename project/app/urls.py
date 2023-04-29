from app import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('about', views.about, name="about"),
    path('resume', views.resume, name="resume"),
    path('contact', views.contact, name="contact"),

]
