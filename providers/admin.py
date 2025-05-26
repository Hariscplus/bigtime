from django.contrib import admin
from django.contrib.auth.models import Group
from .models import ProviderProfile


@admin.register(ProviderProfile)
class ProviderProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'contact_email', 'is_active', 'is_invisible')
    search_fields = ('user__username', 'company_name', 'contact_email')
    list_filter = ('is_active', 'is_invisible', 'created_at')