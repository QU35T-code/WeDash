from django.urls import path
from Accounts.views import RegisterPage, LoginPage, LogoutPage

urlpatterns = [
    path('register', RegisterPage, name="RegisterPage"),
    path('login', LoginPage, name="LoginPage"),
    path('logout', LogoutPage, name="LogoutPage"),
]