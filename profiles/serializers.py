# serializers.py
from rest_framework import serializers
from .models import PlayerProfile

class PlayerProfileToggleSerializer(serializers.ModelSerializer):
  class Meta:
      model = PlayerProfile
      fields = ['notifications_enabled', 'is_subscribed', 'receive_newsletter','is_active','is_invisible']