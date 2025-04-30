from django.urls import path
from . import views

urlpatterns = [
    # path('mitra/', views.mitra, name='daftar_mitra'),
    path('', views.mitra, name='home'),
    path('donasi/', views.donatur, name='donasi_sekarang'),
    path('status/', views.status_donasi, name='status_donasi'),
    path('formdonasi/',views.form_donasi, name='form_donasi'),
    path('riwayatdonasi/', views.riwayat_donasi, name='riwayat_donasi')
]
