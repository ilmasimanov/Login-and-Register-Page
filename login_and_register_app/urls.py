
from django.urls import path
from login_and_register_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginpage, name='loginpage'),
    path('register/', views.registerpage, name='registerpage'),
    path('logout/', views.logoutuser, name='logoutuser')
]
