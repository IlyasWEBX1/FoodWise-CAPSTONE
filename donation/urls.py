from django.urls import path
from . import views

urlpatterns = [
    # path('mitra/', views.mitra, name='daftar_mitra'),
    path('', views.mitra, name='home'),
    path('signup/volunteer/', views.volunteer_signup, name='volunteer_signup'),
    path('signup/fooddonor/', views.fooddonor_signup, name='fooddonor_signup'),
    path('login/', views.login_view, name='login'),
    path('donasi/', views.donatur, name='donasi_sekarang'),
    path('status/', views.status_donasi, name='status_donasi'),
    path('formdonasi/',views.form_donasi, name='form_donasi'),
    path('riwayatdonasi/', views.riwayat_donasi, name='riwayat_donasi'),
    path('jadirelawan/', views.jadi_relawan, name='jadi_relawan'),
    path('jadimitra/', views.jadi_mitra, name='jadi_mitra'),
    path('logout/', views.logout_view, name='logout'),
]
