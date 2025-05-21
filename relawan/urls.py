from django.urls import path
from . import views

urlpatterns = [
  path('caridonasi/', views.caridonasi, name='caridonasi'),
  path('donasidiambil/', views.donasidiambil, name='donasidiambil'),
  path('riwayatpembagian/', views.riwayatpembagian, name='riwayatpembagian'),
  path('aksi/<int:transaction_id>/', views.aksi_donasi, name='aksi_donasi'),
  path('upload-bukti-distribusi/<int:transaction_id>/', views.upload_bukti_distribusi, name='upload_bukti_distribusi'),


]