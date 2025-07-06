from django.urls import path
from . import views

app_name = 'user_auth'

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('register/', views.register, name="register"),
    path('authenticate_user/', views.authenticate_user,
         name='authenticate_user'),
    path('show_user', views.show_user, name="show_user"),
]
