from django.shortcuts import render, redirect
from .forms import VolunteerSignUpForm, FoodDonorSignUpForm, LoginForm
from .models import Volunteer, FoodDonor

def volunteer_signup(request):
    if request.method == 'POST':
        form = VolunteerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # or your home page
    else:
        form = VolunteerSignUpForm()
    return render(request, 'volunteer_signup.html', {'form': form})

def fooddonor_signup(request):
    if request.method == 'POST':
        form = FoodDonorSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = FoodDonorSignUpForm()
    return render(request, 'fooddonor_signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Basic login check against both models (you can customize this further)
            user = Volunteer.objects.filter(username=username, password=password).first() or \
                   FoodDonor.objects.filter(username=username, password=password).first()
            if user:
                return redirect('dashboard')  # change to your actual destination
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'donation/login.html', {'form': form})

def mitra(request):
    return render(request, 'donation/daftarmitrarelawan.html')

def donatur(request):
    return render(request, 'donation/donasisekarang.html')
  
def status_donasi(request):
    return render(request, 'donation/statusdonasi.html')

def form_donasi(request):
    return render(request, 'donation/formdonasi.html')

def riwayat_donasi(request):
    return render(request, 'donation/riwayatdonasi.html')

def jadi_relawan(request):
    return render(request, 'donation/jadirelawan.html')

def jadi_mitra(request):
    return render(request, 'donation/jadimitra.html')
