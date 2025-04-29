from django.urls import path
from . import views

urlpatterns = [
    path('mitra/', views.mitra, name='daftar_mitra'),
    path('donasi/', views.donatur, name='donasi_sekarang'),
    path('status/', views.status_donasi, name='status_donasi'),
]
