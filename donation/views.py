from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.utils import timezone

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
                request.session['user_role'] = 'volunteer'
                request.session.set_expiry(3600 * 24 * 30)  
                return redirect('home')

            food_donor = FoodDonor.objects.filter(username=username).first()
            if food_donor and password == food_donor.password:
                request.session['username'] = food_donor.username
                request.session['user_id'] = food_donor.id
                request.session['user_role'] = 'food_donor'
                request.session.set_expiry(3600 * 24 * 30)
                return redirect('home')

            form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'donation/login.html', {'form': form})

def mitra(request):
    return render(request, 'donation/daftarmitrarelawan.html')

def donatur(request):
    return render(request, 'donation/donasisekarang.html')

def status_donasi(request):
    username = request.session.get('username')
    role = request.session.get('user_role')

    transactions = []

    if role == 'volunteer':
        volunteer = Volunteer.objects.filter(username=username).first()
        if volunteer:
            transactions = DonationTransaction.objects.filter(volunteer=volunteer)

    elif role == 'food_donor':
        donor = FoodDonor.objects.filter(username=username).first()
        if donor:
            transactions = DonationTransaction.objects.filter(food_item__food_donor=donor)

    return render(request, 'donation/statusdonasi.html', {
        'pending_transactions': transactions.filter(status='Pending'),
        'completed_transactions': transactions.filter(status='Completed'),
    })

def form_donasi(request):
    form = FoodItemForm()
    username = request.session.get('username')
    user_role = request.session.get('user_role')
    food_donor = None
    volunteer = None
    if user_role == 'food_donor' and username:
        food_donor = FoodDonor.objects.filter(username=username).first()
    elif user_role == 'volunteer' and username:
        volunteer = Volunteer.objects.filter(username=username).first()
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
                if food_donor:
                    donation = form.save(commit=False)
                    donation.food_donor = food_donor 
                    donation.save()
                    DonationTransaction.objects.create(
                    food_item=donation,
                    volunteer=None, 
                    status='Pending',
                    donation_date=timezone.now().date()
                    )
                    return redirect('home')
                else:
                    form.add_error(None, 'Food donor not found.')
    else:
        form = FoodItemForm()

    return render(request, 'donation/formdonasi.html', {
        'form': form,
        'username': request.session.get('username'),
        'food_donor':food_donor,
        'volunteer' : volunteer
    })

def riwayat_donasi(request):
    pending_transactions = DonationTransaction.objects.filter(status='Pending')
    completed_transactions = DonationTransaction.objects.filter(status='Completed')

    context = {
        'pending_transactions': pending_transactions,
        'completed_transactions': completed_transactions,
    }
    return render(request, 'donation/riwayatdonasi.html', context)

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

def logout_view(request):
    request.session.flush()  
    return redirect('login') 