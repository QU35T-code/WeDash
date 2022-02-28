from django.urls import path
from django.urls.conf import include
from HomePage.views import HomePage

urlpatterns = [
    path('', HomePage, name="HomePage"),
]
