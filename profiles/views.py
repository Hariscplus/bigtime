from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import PlayerProfile
from .forms import PlayerProfileForm
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PlayerProfileToggleSerializer
from django.contrib.auth.models import User
from django.contrib import messages
import logging
from django.contrib.sessions.models import Session
from django.utils import timezone
import json


logger = logging.getLogger(__name__)


class PlayerProfileListView(ListView):
    model = PlayerProfile
    template_name = 'profiles/playerprofile_list.html'
    context_object_name = 'player_profiles'


@login_required
def player_profile_detail(request):
    profile = get_object_or_404(PlayerProfile, user=request.user)
    return render(request, 'profiles/playerprofile_detail.html', {'profile': profile})


@login_required
def settings_view(request):
    # Assuming you have a way to get the current user's profile
    player_profile = PlayerProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = PlayerProfileForm(request.POST, request.FILES, instance=player_profile)
        if form.is_valid():
            form.save()
            return redirect(settings_view)  # Redirect to the same view or another page
    else:
        form = PlayerProfileForm(instance=player_profile)

    context = {
        'form': form,
        'player_profile': player_profile,  # Pass the profile to the template
    }
    return render(request, 'profiles/settings.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('settings')  # Redirect to the settings page or wherever you want
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'profiles/settings.html', {'form': form})


@login_required
def player_profile_update(request):
    profile = get_object_or_404(PlayerProfile, user=request.user)
    if request.method == 'POST':
        form = PlayerProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('playerprofile-detail')
    else:
        form = PlayerProfileForm(instance=profile)
    return render(request, 'profiles/playerprofile_form.html', {'form': form})


class ToggleFieldView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Ensure only authenticated users can access

    def patch(self, request, field_name):
        logger.debug(f"User authenticated: {request.user.is_authenticated}")

        # Ensure the user is authenticated
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=401)

        try:
            # Get the user's profile
            profile = PlayerProfile.objects.get(user=request.user)
        except PlayerProfile.DoesNotExist:
            return Response({"detail": "Profile not found."}, status=404)

        # Define valid fields
        valid_fields = ['notifications_enabled', 'is_subscribed', 'receive_newsletter', 'is_active', 'is_invisible']

        # Check if the field name is valid
        if field_name in valid_fields:
            # Toggle the field value
            current_value = getattr(profile, field_name)
            setattr(profile, field_name, not current_value)
            profile.save()

            # Serialize the updated profile
            serializer = PlayerProfileToggleSerializer(profile)
            logger.info(f"{field_name} toggled to {not current_value} for user {request.user.username}.")
            return Response(serializer.data)  # Return the updated data

        logger.error(f"Invalid field name: {field_name}")
        return Response({"detail": "Invalid field name."}, status=400)  # Bad request if field name is invalid
