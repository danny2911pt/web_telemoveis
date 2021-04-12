from django.shortcuts import render
from rest_framework import generics, status
from .serializers import TelemovelSerializer,UserSerializer,CreateUserSerializer
from .models import Telemovel,User
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TelemovelView(generics.CreateAPIView):
    queryset = Telemovel.objects.all()
    serializer_class = TelemovelSerializer

class CreateUser(APIView):
    serializer_class = CreateUserSerializer
    
    def post(self, request, format=None):
        pass