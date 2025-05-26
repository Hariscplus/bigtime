"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/home', include('home.urls')),  # home app urls for registration and login
    path("admin/", admin.site.urls),  # Django admin site
    path("", include('admin_soft_pro.urls')),  # Include the soft admin dashboard URLs
    path('profiles/', include('profiles.urls')),  # Include the profiles app URLs
    path('payments/', include('payments.urls')),  # Include the payments app URLs
    path('wallets/', include('wallets.urls')),  # Include the wallets app URLs
]
