from django.urls import path
from .views import (
    PlayerProfileListView,
    player_profile_detail,
    player_profile_update,
    settings_view,  # Import the settings view
    change_password,  # Import the change password view
    ToggleFieldView,
)

urlpatterns = [
    path('profile/', player_profile_detail, name='playerprofile-detail'),
    path('profile/edit/', player_profile_update, name='playerprofile-update'),
    path('players/', PlayerProfileListView.as_view(), name='playerprofile-list'),
    path('profile/toggle/<str:field_name>/', ToggleFieldView.as_view(), name='toggle-field'),
    path('profile/settings/', settings_view, name='settings'),  # Add the settings URL

    path('change-password/', change_password, name='change_password'),  # Add the change password URL
]
