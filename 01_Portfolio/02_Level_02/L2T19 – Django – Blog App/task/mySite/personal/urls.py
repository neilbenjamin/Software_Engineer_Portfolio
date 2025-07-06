from django.urls import path
from . import views

app_name = "personal"

urlpatterns = [
    path('', views.index, name="index"),
    path('resume/', views.resume, name="resume"),
    path('contact/', views.contact, name="contact"),
    ]
