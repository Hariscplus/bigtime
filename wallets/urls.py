from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_wallets, name='user_wallets'),
]