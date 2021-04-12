from rest_framework import serializers
from .models import User,Telemovel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password')

class TelemovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telemovel
        fields = ('nome','link','modelo','negociavel','preco','descricao','site')

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('username','password')