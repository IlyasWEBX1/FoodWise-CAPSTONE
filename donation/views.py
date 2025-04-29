from django.shortcuts import render

def mitra(request):
    return render(request, 'donation/daftarmitrarelawan.html')

def donatur(request):
    return render(request, 'donation/donasisekarang.html')
  
def status_donasi(request):
    return render(request, 'donation/statusdonasi.html')