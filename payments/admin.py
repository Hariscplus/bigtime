from django.contrib import admin
from .models import PaymentGateway

@admin.register(PaymentGateway)
class PaymentGatewayAdmin(admin.ModelAdmin):
    list_display = ('name', 'gateway_type', 'is_active')
    search_fields = ('name',)
    list_filter = ('gateway_type', 'is_active')