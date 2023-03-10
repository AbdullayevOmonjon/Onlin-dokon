from django.urls import path
from .views import *


urlpatterns=[
  path('',Savat_View.as_view(),name='savat'),
  path('qoshish/<int:pk>',QoshView.as_view(),name='qoshish'),
  path('ayrish/<int:pk>',AyirView.as_view(),name='ayrish'),
]