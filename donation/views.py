from django.shortcuts import render, redirect
from .forms import VolunteerSignUpForm, FoodDonorSignUpForm, LoginForm
from .models import Volunteer, FoodDonor

def volunteer_signup(request):
    if request.method == 'POST':
        form = VolunteerSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if Volunteer.objects.filter(username=username).exists():
                form.add_error('username', 'Username already taken')
            else:
                form.save()
                return redirect('login')  
    else:
        form = VolunteerSignUpForm()
    return render(request, 'volunteer_signup.html', {'form': form})

def fooddonor_signup(request):
    if request.method == 'POST':
        form = FoodDonorSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if FoodDonor.objects.filter(username=username).exists():
                form.add_error('username', 'Username already taken')
            else:
                form.save()
                return redirect('login')  
    else:
        form = VolunteerSignUpForm()
    return render(request, 'volunteer_signup.html', {'form': form})


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
                return redirect('home')  # change to your actual destination
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
    if request.method == 'POST':
        form = DonationTransactionForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            if request.user.is_authenticated:
                try:
                    volunteer = Volunteer.objects.get(username=request.user.username)
                    donation.volunteer = volunteer  
                except Volunteer.DoesNotExist:
                    try:
                        food_donor = FoodDonor.objects.get(username=request.user.username)
                        donation.food_donor = food_donor 
                    except FoodDonor.DoesNotExist:
                        pass

            donation.save()
            return redirect('status_donasi')
    else:
        form = DonationTransactionForm()
    return render(request, 'donation/formdonasi.html', {'form': form})

def riwayat_donasi(request):
    try:
        volunteer = Volunteer.objects.get(username=request.user.username)
        donations = DonationTransaction.objects.filter(volunteer=volunteer)
    except Volunteer.DoesNotExist:
        donations = None  
    return render(request, 'donation/riwayatdonasi.html', {'donations': donations})    

def jadi_relawan(request):
    if request.method == 'POST':
        form = VolunteerSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if Volunteer.objects.filter(username=username).exists():
                form.add_error('username', 'Username already taken')
            else:
                form.save()
                return redirect('login')  
    else:
        form = VolunteerSignUpForm()
    return render(request, 'donation/jadirelawan.html', {'form': form})

def jadi_mitra(request):
    if request.method == 'POST':
        form = FoodDonorSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if FoodDonor.objects.filter(username=username).exists():
                form.add_error('username', 'Username already taken')
            else:
                form.save()
                return redirect('login')  
    else:
        form = FoodDonorSignUpForm()
    return render(request, 'donation/jadimitra.html',{'form':form})
