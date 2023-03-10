from django.db import models
from django.contrib.auth.models import *
# Create your models here.

class Profil(models.Model):
  ism=models.CharField(max_length=50)
  famila=models.CharField(max_length=50)
  emile=models.CharField(max_length=60)
  jinsi=models.BooleanField(null=True)
  shaxar=models.CharField(max_length=50)
  davlat=models.CharField(max_length=50)
  user=models.OneToOneField(User,on_delete=models.CASCADE)
  def __str__(self) -> str:
    return self.ism