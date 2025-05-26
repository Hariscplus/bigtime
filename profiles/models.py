from django.db import models
from django.contrib.auth.models import User  # Use the default User model

class PlayerProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  favorite_game = models.CharField(max_length=100, default="Unknown Game")
  date_of_birth = models.DateField(null=True, blank=True)  # Typically, you don't set a default for dates
  profile_picture = models.ImageField(upload_to='player_pics/', null=True, blank=True)
  bio = models.TextField(max_length=500, blank=True, default="No bio available.")
  level = models.IntegerField(default=1)
  achievements = models.JSONField(default=dict, blank=True)
  social_links = models.JSONField(default=dict, blank=True)
  game_preferences = models.JSONField(default=list, blank=True)
  mobile_number = models.CharField(max_length=15, blank=True, default="Not provided")
  location = models.CharField(max_length=100, blank=True, default="Unknown")
  notifications_enabled = models.BooleanField(default=True)
  is_subscribed = models.BooleanField(default=False)
  receive_newsletter = models.BooleanField(default=False)
  is_invisible = models.BooleanField(default=True)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.user.username