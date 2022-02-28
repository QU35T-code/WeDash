from django.urls import path
from DashboardPage.views import DashboardPage, SettingsPage, ShopPage, ProfilePage, InstallWidget, UninstallWidget, RunWidget, DeleteUser

urlpatterns = [
    path('', DashboardPage, name="DashboardPage"),
    path('settings/', SettingsPage, name="SettingsPage"),
    path('profile/', ProfilePage, name="ProfilePage"),
    path('shop/', ShopPage, name="ShopPage"),
    path('shop/install/<int:id>/', InstallWidget, name="InstallWidget"),
    path('shop/uninstall/<int:id>/', UninstallWidget, name="UnistallWidget"),
    path('widgets/<str:name>/activate/', RunWidget, name="RunWidget"),
    path('settings/delete/<int:id>', DeleteUser, name="DeleteUser")

]