from django.db import models
from django.contrib.auth.models import User
from user_app.models import *

# Create your models here.

class Bolim(models.Model):
  nom=models.CharField(("bolim nomi"), max_length=50)
  rasm=models.FileField(upload_to='bolimlar')
  def __str__(self) -> str:
    return self.nom
  


class Mahsulot(models.Model):
  nom=models.CharField(("mahsulot nomi"), max_length=50)
  narx=models.FloatField()
  brend=models.CharField(max_length=50)
  davlat=models.CharField(max_length=50)
  kafolat=models.CharField(max_length=100)
  bolim=models.ForeignKey(Bolim,on_delete=models.CASCADE)
  min_miqdor=models.IntegerField(default=2)
  tasqilangan=models.BooleanField(default=True)
  yetkazish=models.CharField(max_length=50)
  mavjud=models.BooleanField(default=True)
  chegirma=models.PositiveSmallIntegerField()
  def __str__(self) -> str:
    return f"{self.nom},  {self.brend}"
  
class Izoh(models.Model):
  baho=models.PositiveSmallIntegerField()
  matn=models.CharField(max_length=50)
  mahsulot=models.ForeignKey(Mahsulot,on_delete=models.CASCADE)
  profil=models.ForeignKey(Profil,on_delete=models.CASCADE)
  sana=models.DateTimeField(auto_now_add=True)
  def __init__(self) -> int:
    return self.baho
  

class Madia(models.Model):
  rasim=models.FileField(upload_to='madia')
  masulot=models.ForeignKey(Mahsulot,on_delete=models.CASCADE)
  
