from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='home'),
    path('signup/volunteer/', views.volunteer_signup, name='volunteer_signup'),
    path('signup/fooddonor/', views.fooddonor_signup, name='fooddonor_signup'),
    path('jadirelawan/', views.jadi_relawan, name='jadi_relawan'),
    path('jadimitra/', views.jadi_mitra, name='jadi_mitra'),
    path('login/', views.login_view, name='login'),

]
