from django.contrib import admin
from .models import PlayerProfile

@admin.register(PlayerProfile)
class PlayerProfileAdmin(admin.ModelAdmin):
  list_display = ('user', 'favorite_game', 'level', 'location', 'notifications_enabled', 'is_subscribed')
  search_fields = ('user__username', 'favorite_game', 'location')
  list_filter = ('notifications_enabled', 'is_subscribed', 'receive_newsletter')
  ordering = ('user',)
  readonly_fields = ('user',)

  fieldsets = (
      (None, {
          'fields': ('user', 'favorite_game', 'date_of_birth', 'profile_picture', 'bio')
      }),
      ('Game Details', {
          'fields': ('level', 'achievements', 'game_preferences')
      }),
      ('Contact Information', {
          'fields': ('mobile_number', 'location', 'social_links')
      }),
      ('Preferences', {
          'fields': ('notifications_enabled', 'is_subscribed', 'receive_newsletter')
      }),
  )