from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import UserSerializer, LoginSerializer

# Create your views here.


def index(request):

    # Page from the theme 
    return render(request, 'pages/dashboards/default.html')

class RegisterView(generics.CreateAPIView):
  queryset = User.objects.all()
  permission_classes = (AllowAny,)
  serializer_class = UserSerializer

class LoginView(generics.GenericAPIView):
  permission_classes = (AllowAny,)
  serializer_class = LoginSerializer

  def post(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      user = serializer.validated_data
      token, created = Token.objects.get_or_create(user=user)
      return Response({"token": token.key})
