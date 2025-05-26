from django.db import models
from django.contrib.auth.models import User


class ProviderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, default='Unnamed Company')
    company_website = models.URLField(max_length=200, blank=True, default='')
    contact_email = models.EmailField(max_length=254, default='contact@example.com')
    phone_number = models.CharField(max_length=15, blank=True, default='')
    address = models.TextField(blank=True, default='')
    apps_offered = models.JSONField(default=list, blank=True)
    business_registration_number = models.CharField(max_length=50, blank=True, default='')
    logo = models.ImageField(upload_to='provider_logos/', null=True, blank=True)
    portfolio = models.JSONField(default=list, blank=True)
    api_access_key = models.CharField(max_length=100, blank=True, default='')
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    support_contact = models.EmailField(max_length=254, blank=True, default='')
    compliance_status = models.CharField(max_length=100, blank=True, default='Pending')
    app_store_links = models.JSONField(default=list, blank=True)
    certifications = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_invisible = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username