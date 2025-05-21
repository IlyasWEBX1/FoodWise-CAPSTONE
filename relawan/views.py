from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from donation.models import DonationTransaction, FoodDonor, Volunteer

def caridonasi(request):
    username = request.session.get('username')
    user_role = request.session.get('user_role')

    if user_role == 'Relawan' and username:
        transactions = DonationTransaction.objects.filter(status = 'Menunggu Diambil')
        return render(request, 'relawan/caridonasi.html', {'transactions':transactions})
    else:
        return redirect('login')

def donasidiambil(request):
    username = request.session.get('username')
    user_role = request.session.get('user_role')
    user_id = request.session.get('user_id')

    if user_role == 'Relawan' and username:
        transactions = DonationTransaction.objects.filter(volunteer_id = user_id)
        transactions = transactions.exclude(status = 'Selesai')
        
        return render(request, 'relawan/donasidiambil.html', {'transactions':transactions})    
    else:
        return redirect('login')


def riwayatpembagian(request):
    username = request.session.get('username')
    user_role = request.session.get('user_role')
    user_id = request.session.get('user_id')
    
    if user_role == 'Relawan' and username:
        transactions = DonationTransaction.objects.filter(volunteer_id = user_id)
        completed_transaction = transactions.filter(status = "Selesai")
        return render(request, 'relawan/riwayatpembagian.html', {'completed_transactions':completed_transaction})
    else:
        return redirect("login")
    
def aksi_donasi(request, transaction_id):
    if request.method == 'POST':
        transaction = get_object_or_404(DonationTransaction, id=transaction_id)
        if transaction.status == 'Menunggu Diambil': 
            if transaction.volunteer_id is None:
                transaction.volunteer_id = request.session.get('user_id')
            else:
                transaction.status = 'Menunggu Disalurkan' 
            transaction.save()
        elif transaction.status == 'Menunggu Disalurkan':
            # Memastikan bukti distribusi sudah diunggah sebelum mengubah status
            if transaction.delivery_evidence:
                transaction.status = 'Telah Disalurkan' 
                transaction.save()
        elif transaction.status == 'Telah Disalurkan':
            transaction.status = 'Selesai' 
            transaction.save()

    return redirect('donasidiambil')

def upload_bukti_distribusi(request, transaction_id):
    """
    View untuk menangani unggahan bukti distribusi
    """
    username = request.session.get('username')
    user_role = request.session.get('user_role')
    
    if user_role != 'Relawan' or not username:
        return redirect('login')
    
    if request.method == 'POST' and request.FILES.get('distribution_img'):
        transaction = get_object_or_404(DonationTransaction, id=transaction_id)
        
        # Pastikan transaksi milik relawan yang sedang login
        if transaction.volunteer_id == request.session.get('user_id'):
            # Simpan gambar ke field delivery_evidence
            transaction.delivery_evidence = request.FILES['distribution_img']
            transaction.save()
            
    return redirect('donasidiambil')