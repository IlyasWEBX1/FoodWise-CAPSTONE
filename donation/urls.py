from django.urls import path
from . import views

urlpatterns = [
    path('mitra/', views.mitra, name='daftar_mitra'),
    # path('', views.mitra, name='home'),
    path('donasi/', views.donatur, name='donasi_sekarang'),
    path('status/', views.status_donasi, name='status_donasi'),
    path('formdonasi/',views.form_donasi, name='form_donasi'),
    path('riwayatdonasi/', views.riwayat_donasi, name='riwayat_donasi'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboardrelawan/', views.dashboardrelawan, name='dashboardrelawan'),
    path('confirm/<int:transaction_id>/', views.confirm_completion, name='confirm_completion'),
]
