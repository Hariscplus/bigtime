# home/serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = ('id', 'username', 'email', 'password')
      extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
      user = User.objects.create_user(
          username=validated_data['username'],
          email=validated_data['email'],
          password=validated_data['password']
      )
      return user

class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField(write_only=True)

  def validate(self, data):
      user = authenticate(**data)
      if user and user.is_active:
          return user
      raise serializers.ValidationError("Invalid credentials")