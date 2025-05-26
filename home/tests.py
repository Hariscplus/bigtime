# home/tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthenticationTests(APITestCase):
    def test_register_user(self):
        url = reverse('register')
        data = {
            'username': 'front',
            'email': 'zawar@outlook.com',
            'password': 'admin@112'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        # First, register the user
        self.test_register_user()

        # Then, test login
        url = reverse('login')
        data = {
            'username': 'front',
            'password': 'admin@112'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)