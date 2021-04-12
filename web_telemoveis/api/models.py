from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30, default="", unique="true" )
    password = models.CharField(max_length =50, default="", unique="false")

class Telemovel(models.Model):
    nome  = models.CharField(max_length=8000  , default="",unique="false")
    link  = models.CharField(max_length=8000  , default="",unique="true",primary_key=True)
    modelo = models.CharField(max_length=30 , default="",unique="false")
    negociavel = models.BooleanField(default=False)
    preco = models.IntegerField()
    descricao = models.CharField(max_length=8000  , default="",unique="false")
    site = models.CharField(max_length=8000  , default="",unique="false")
