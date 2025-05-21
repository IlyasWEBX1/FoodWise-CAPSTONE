from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.utils import timezone

def mitra(request):
    return render(request, 'donation/daftarmitrarelawan.html')

def dashboardrelawan(request):
    return render(request, 'donation/dashboardrelawan.html')

def donatur(request):
    return render(request, 'donation/donasisekarang.html')

def status_donasi(request):
    username = request.session.get('username')
    role = request.session.get('user_role')

    transactions = DonationTransaction.objects.none()  # kosong tapi tetap queryset

    if role == 'Relawan':
        volunteer = Volunteer.objects.filter(username=username).first()
        if volunteer:
            transactions = DonationTransaction.objects.filter(volunteer=volunteer)

    elif role == 'Donatur':
        donor = FoodDonor.objects.filter(username=username).first()
        if donor:
            transactions = DonationTransaction.objects.filter(food_item__food_donor=donor)
    else: 
        return redirect('login')
    return render(request, 'donation/statusdonasi.html', {
        'transactions': transactions.exclude(status='Selesai'),
    })

def form_donasi(request):
    form = FoodItemForm()
    username = request.session.get('username')
    user_role = request.session.get('user_role')
    food_donor = None
    volunteer = None
    if user_role == 'Donatur' and username:
        food_donor = FoodDonor.objects.filter(username=username).first()
    elif user_role == 'Relawan' and username:
        volunteer = Volunteer.objects.filter(username=username).first()
    else:
        return redirect('login')
    
    if request.method == 'POST':
        form = FoodItemForm(request.POST, request.FILES)
        if form.is_valid():
                if food_donor:
                    donation = form.save(commit=False)
                    donation.food_donor = food_donor 
                    donation.save()
                    DonationTransaction.objects.create(
                    food_item=donation,
                    volunteer=None, 
                    status='Menunggu Diambil',
                    donation_date=timezone.now().date()
                    )
                    return redirect('status_donasi')
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
    username = request.session.get("username")
    user_role = request.session.get("user_role")
    
    if not username or not user_role:
        return redirect('login')
    
    completed_transactions = DonationTransaction.objects.filter(
        status='Selesai',
        food_item__food_donor__username=username
    )
    
    return render(request, 'donation/riwayatdonasi.html', {'completed_transactions': completed_transactions})

def logout_view(request):
    request.session.flush()  
    return redirect('home') 

def confirm_completion(request, transaction_id):
    if request.method == 'POST':
        transaction = get_object_or_404(DonationTransaction, id=transaction_id)
        if transaction.status == 'Telah Disalurkan': 
            transaction.status = 'Selesai' 
            transaction.save()
    return redirect('status_donasi')  