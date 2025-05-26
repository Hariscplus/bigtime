from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import PlayerProfile

class ToggleFieldViewTests(APITestCase):

  def setUp(self):
      # Create a user with a known password
      self.user = User.objects.create_user(username='testuser', password='testpassword')

      # Create a player profile for the user
      self.profile = PlayerProfile.objects.create(
          user=self.user,
          notifications_enabled=False,
          is_subscribed=False,
          receive_newsletter=False
      )

      # Define the URLs for toggling fields
      self.url_notifications = reverse('toggle-field', kwargs={'field_name': 'notifications_enabled'})
      self.url_subscribed = reverse('toggle-field', kwargs={'field_name': 'is_subscribed'})
      self.url_newsletter = reverse('toggle-field', kwargs={'field_name': 'receive_newsletter'})

  def test_toggle_notifications_enabled(self):
      # Log in the user
      login_success = self.client.login(username='testuser', password='testpassword')
      self.assertTrue(login_success, "Login failed for user testuser")  # Assert login success

      # Check initial value
      self.assertFalse(self.profile.notifications_enabled)

      # Send PATCH request to toggle notifications_enabled
      response = self.client.patch(self.url_notifications)

      # Check response status
      self.assertEqual(response.status_code, status.HTTP_200_OK)

      # Refresh the profile from the database
      self.profile.refresh_from_db()

      # Check that the value has been toggled
      self.assertTrue(self.profile.notifications_enabled)

  def test_unauthorized_access(self):
      # Send PATCH request without logging in
      response = self.client.patch(self.url_notifications)

      # Check response status
      self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_invalid_field_name(self):
      # Log in the user
      login_success = self.client.login(username='testuser', password='testpassword')
      self.assertTrue(login_success, "Login failed for user testuser")  # Assert login success

      # Define an invalid field name
      invalid_url = reverse('toggle-field', kwargs={'field_name': 'invalid_field'})

      # Send PATCH request to toggle an invalid field
      response = self.client.patch(invalid_url)

      # Check response status
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_toggle_is_subscribed(self):
      # Log in the user
      login_success = self.client.login(username='testuser', password='testpassword')
      self.assertTrue(login_success, "Login failed for user testuser")  # Assert login success

      # Check initial value
      self.assertFalse(self.profile.is_subscribed)

      # Send PATCH request to toggle is_subscribed
      response = self.client.patch(self.url_subscribed)

      # Check response status
      self.assertEqual(response.status_code, status.HTTP_200_OK)

      # Refresh the profile from the database
      self.profile.refresh_from_db()

      # Check that the value has been toggled
      self.assertTrue(self.profile.is_subscribed)

  def test_toggle_receive_newsletter(self):
      # Log in the user
      login_success = self.client.login(username='testuser', password='testpassword')
      self.assertTrue(login_success, "Login failed for user testuser")  # Assert login success

      # Check initial value
      self.assertFalse(self.profile.receive_newsletter)

      # Send PATCH request to toggle receive_newsletter
      response = self.client.patch(self.url_newsletter)

      # Check response status
      self.assertEqual(response.status_code, status.HTTP_200_OK)

      # Refresh the profile from the database
      self.profile.refresh_from_db()

      # Check that the value has been toggled
      self.assertTrue(self.profile.receive_newsletter)