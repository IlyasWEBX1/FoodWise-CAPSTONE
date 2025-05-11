from django.urls import path
from . import views

urlpatterns = [
  path('caridonasi/', views.caridonasi, name='caridonasi'),
  path('donasidiambil/', views.donasidiambil, name='donasidiambil'),
  path('laporanpembagian/', views.laporanpembagian, name='laporanpembagian'),
]