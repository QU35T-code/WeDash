from django.urls import path
from SupportPage.views import SupportPage

urlpatterns = [
    path('', SupportPage, name="SupportPage"),
]