from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.db.models import Sum
# Create your views here.

class Savat_View(View):
  def get(self,request):
    m=Savat.objects.filter(user__user=request.user)
    summa=m.aggregate(Sum('umumiy')).get('umumiy__sum')
    chegirma=m.aggregate()
    data={
      'mahsulot':m,
      "summa":summa,
      'chegmali_sum':chegirma
    }
    return render(request,'page-shopping-cart.html',data)
  
class QoshView(View):
    def get(self, request, pk):
        savat = Savat.objects.get(id=pk)
        narx = savat.mahsulot.narx
        savat.umumiy += narx
        savat.soni += 1
        savat.save()
        return redirect('/buyurtma/savat/')

class AyirView(View):
    def get(self, request, pk):
        savat = Savat.objects.get(id=pk)
        narx = savat.mahsulot.narx
        if savat.soni !=1:
            savat.soni -= 1
            savat.umumiy -= narx
        else:
            savat.soni = 1
            savat.umumiy = narx
        savat.save()
        return redirect('/buyurtma/savat/')