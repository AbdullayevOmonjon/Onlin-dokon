from django.urls import path
from .views import *


urlpatterns=[
path('page/',Homeview.as_view(),name='page'),
path('login/',Login_View.as_view(),name='login'),
path('logout/',LogoutView.as_view(),name='logout'),
path('register/',User_View.as_view(),name='register'),
path('bolimlar/',BolimlarView.as_view(),name='bolimlar'),
path('bolim_1/<int:pk>/',Bolim_View.as_view(),name='bolim_1'),
path('mahsulot/<int:pk>/',MahsulotView.as_view(),name='mahsulot'),
]