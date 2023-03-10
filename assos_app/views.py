from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.db.models import Avg 
from django.contrib.auth import authenticate,login,logout

# Create your views here.

# class HomeView(View):
#   def get(self,request):
#     return render(request,'header.html')
  
  
class Homeview(View):
  def get(self,request):
    if request.user.is_authenticated:
      data={
        'bolimlar':Bolim.objects.all()[:7],
        'chegirmallilar':Mahsulot.objects.filter(chegirma__gt=0).order_by('-chegirma')[:5]
      }
      return render(request,'page-index.html',data)
    return redirect('login')
  
class Login_View(View):
  def get(self,request):
    return render(request,'page-user-login.html')
  
  def post(self,request):
    n=authenticate(username=request.POST.get('login'),
                    password=request.POST.get('password'))
    if n is None:
      return redirect('login')
    else:
      login(request,n)
      return redirect('page')
    
class LogoutView(View):
  def get(self,request):
    logout(request)
    return redirect('login')

class User_View(View):
  def get(self,request):
    return render(request,'page-user-register.html')
  
  def post(self,request):
    n=User.objects.create_user(
      username=request.POST.get('f_name'),
      password=request.POST.get('p'),
    )
    Profil.objects.create(
      ism=request.POST.get('f_name'),
      famila=request.POST.get('l_name'),
      emile=request.POST.get('email'),
      jinsi=request.POST.get('gender'),
      shaxar=request.POST.get('shaxar'),
      davlat=request.POST.get('davlat'),
      user=n,
    )
    return redirect('login')
  
  
  
class Home2view(View):
  def get(self,request):
    data={
      'mahsulot':Mahsulot.objects.filter(chegirma__gt=1)
    }
    return render(request,'page-index-2.html',data)
  
class BolimlarView(View):
  def get(self,request):
    data={
      'bolimlar':Bolim.objects.all(),
      # 'mahsulotlar':Mahsulot.objects.filter(bolim__nom=soz)
    }
    return render(request,'page-category.html',data)
  
class Bolim_View(View):
  def get(self,request,pk):
    b1=Bolim.objects.get(id=pk)
    data={
      'mahsulotlar':Mahsulot.objects.filter(bolim=b1)
    }
    return render(request,'page-listing-grid.html',data)
  
# class MahsulotView(View):
#   def get(self, request, pk):
#       izoh=Izoh.objects.filter(mahsulot__id=pk)
#       ortacha=izoh.aggregate(Avg('baho')).get('baho__avg')
#       if ortacha:
#         ortacha *= 20
#       else:
#         ortacha = 0
#       data = {
#           'mahsulot': Mahsulot.objects.get(id=pk),
#           'media': Madia.objects.filter(mahsulot__id=pk),
#           'izohlar':izoh.count(),
#           'ortacha':ortacha
#       }
#       return render(request, 'page-detail-product.html', data)
#   def post(self,request,pk):
#     Izoh.objects.create(
#       baho=request.POST.get('rating'),
#       matn=request.POST.get('comment'),
#       maslahat=Mahsulot.objects.get(id=pk),
#       profil=Profil.objects.get(user=request.user),
#     )
#     return redirect( f'assos/mahsulot_1/{pk}/' )

class MahsulotView(View):
  def get(self,request,pk):
    data={
      'mahsulot':Mahsulot.objects.get(id=pk),
      'madiallar':Madia.objects.filter(masulot__id=pk)
    }
    return render(request,'page-detail-product.html',data)
  
  
  def post(self,request,pk):
    Izoh.objects.create(
      baho=request.POST.get('rating'),
      matn=request.POST.get('comment'),
      mahsulot=Mahsulot.objects.get(id=pk),
      profil=Profil.objects.get(user=request.user),
    )
    return redirect('mahsulot')