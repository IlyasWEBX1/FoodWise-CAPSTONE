from django.shortcuts import redirect, render

from donation.models import FoodDonor, Volunteer
from landing_page.forms import FoodDonorSignUpForm, LoginForm, VolunteerSignUpForm

# Create your views here.
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

            volunteer = Volunteer.objects.filter(username=username).first()
            if volunteer and password == volunteer.password:
                request.session['username'] = volunteer.username
                request.session['user_id'] = volunteer.id
                request.session['user_role'] = 'Relawan'
                request.session.set_expiry(3600 * 24 * 30)  
                return redirect('home')

            food_donor = FoodDonor.objects.filter(username=username).first()
            if food_donor and password == food_donor.password:
                request.session['username'] = food_donor.username
                request.session['user_id'] = food_donor.id
                request.session['user_role'] = 'Donatur'
                request.session.set_expiry(3600 * 24 * 30)
                return redirect('status_donasi')

            form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'landing_page/login.html', {'form': form})



def landing_page(request):
    funfacts = [
        "1.3 miliar ton makanan terbuang setiap tahunnya",
        "Makanan yang terbuang bisa memberi makan 2 miliar orang",
        "Food waste menyumbang 8% emisi gas rumah kaca global",
        "Indonesia membuang 13 juta ton makanan per tahun",
        "1/3 makanan yang diproduksi dunia terbuang percuma"
    ]

    return render(request, 'landing_page/landing_page.html', {'funfacts': funfacts})

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
    return render(request, 'landing_page/jadirelawan.html', {'form': form})

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
    return render(request, 'landing_page/jadimitra.html',{'form':form})
