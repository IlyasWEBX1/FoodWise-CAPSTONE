from django.shortcuts import render

def caridonasi(request):
    return render(request, 'relawan/caridonasi.html')

def donasidiambil(request):
    return render(request, 'relawan/donasidiambil.html')

def laporanpembagian(request):
    return render(request, 'relawan/laporanpembagian.html')