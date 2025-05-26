# providerappoptions/models.py

from django.db import models


# main app will have the data about which type of app is it like games,vending machines etc
class MainApp(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=100, unique=True, default='default_value')  # Add value field
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# app subtype will have the data about the options the main type will have like online_casino,onsite_casino
class AppSubType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=100, unique=True, default='default_value')  # Add value field
    main_app = models.ForeignKey(MainApp, on_delete=models.CASCADE, related_name='subtypes')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.main_app.name})"


# app hosting will have the data about the hosting options the app will have like self-hosted, platform hosted etc.cloud,dedicated server etc
class AppHosting(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=100, unique=True, default='default_value')  # Add value field
    subtype = models.ForeignKey(AppSubType, on_delete=models.CASCADE, related_name='hostings')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.subtype.name})"


# listing status will have the data about the status of the listing like active, inactive etc
class ListingStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)
    value = models.CharField(max_length=100, unique=True, default='default_value')  # Add value field
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Listing Statuses"  # Correct pluralization


# listing app status will have the data about the status of the app like active, inactive etc

class ListingAppStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)
    value = models.CharField(max_length=100, unique=True, default='default_value')  # Add value field
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Listing App Statuses"  # Correct pluralization

#for admin to controll the listing process like accepted, in process, approved etc
class ListingStateStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)
    value = models.CharField(max_length=100, unique=True, default='default_value')  # Add value field
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Listing State Statuses"  # Correct pluralization