from django.urls import path
from . import views

urlpatterns = [
  path('caridonasi/', views.caridonasi, name='caridonasi'),
  path('donasidiambil/', views.donasidiambil, name='donasidiambil'),
  path('laporanpembagian/', views.laporanpembagian, name='laporanpembagian'),
  path('aksi/<int:transaction_id>/', views.aksi_donasi, name='aksi_donasi'),

]