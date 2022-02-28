from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('HomePage.urls')),
    path('dashboard/', include('DashboardPage.urls')),
    path('support/', include('SupportPage.urls')),
    path('accounts/', include('Accounts.urls')),
    path('admin/', admin.site.urls),
]