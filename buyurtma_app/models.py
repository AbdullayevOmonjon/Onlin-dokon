from django.db import models
from django.contrib.auth.models import User
from assos_app.models import *
from user_app.models import *
# Create your models here.


class Savat(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    soni = models.SmallIntegerField()
    umumiy = models.SmallIntegerField(blank=True, null=True)
    user = models.ForeignKey(Profil, on_delete=models.SET_NULL, null=True)
