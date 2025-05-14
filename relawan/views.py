from django.shortcuts import get_object_or_404, redirect, render

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
        inprogress_transactions = transactions.exclude(status = 'Selesai')
        completed_transaction = transactions.filter(status = "Selesai")
        return render(request, 'relawan/donasidiambil.html', {'inprogress_transactions':inprogress_transactions,
                                                              'completed_transactions':completed_transaction})    
    else:
        return redirect('login')


def laporanpembagian(request):
    return render(request, 'relawan/laporanpembagian.html')

def aksi_donasi(request, transaction_id):
    if request.method == 'POST':
        transaction = get_object_or_404(DonationTransaction, id=transaction_id)
        if transaction.status == 'Menunggu Diambil': 
            transaction.volunteer_id = request.session.get('user_id')
            transaction.status = 'Menunggu Disalurkan' 
            transaction.save()
        elif transaction.status == 'Menunggu Disalurkan':
            transaction.status = 'Telah Disalurkan' 
            transaction.save()
        elif transaction.status == 'Telah Disalurkan':
            transaction.status = 'Selesai' 
            transaction.save()

    return redirect('donasidiambil')  