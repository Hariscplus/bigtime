from django.contrib import admin
from .models import SupportedCurrency, UserWallet

@admin.register(SupportedCurrency)
class SupportedCurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'currency_type', 'is_active')
    list_filter = ('currency_type', 'is_active')
    search_fields = ('name', 'code')

@admin.register(UserWallet)
class UserWalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'currency', 'balance', 'wallet_address', 'created_at')
    search_fields = ('user__username', 'currency__code')
    list_filter = ('currency__currency_type',)