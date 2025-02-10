
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Регистрация и вход
    path('', include('apps.services.urls')),
    path('', include('apps.accounts.urls')),
]
