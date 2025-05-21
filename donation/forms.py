from django import forms
from .models import Volunteer, FoodDonor, DonationTransaction, FoodItem

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name_food', 'expiry_date', 'quantity', 'img']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date', 'id' : 'tanggal_kadaluwarsa'}),
            'name_food' : forms.TextInput(attrs={'id' : 'nama_makanan'}), 
            'quantity' : forms.TextInput(attrs={'id' : 'kuantitas'}), 
            'img': forms.ClearableFileInput(attrs={'id': 'foto_makanan', 'accept': 'image/*'}),

        }
        
class DonationTransactionForm(forms.ModelForm):
    class Meta:
        model = DonationTransaction
        fields = ['food_item', 'volunteer', 'status', 'donation_date', 'delivery_evidence']
        widgets = {
            'donation_date': forms.DateInput(attrs={'type': 'date'}),
            'delivery_evidence': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }

    def clean_status(self):
        status = self.cleaned_data.get('status')
        if status not in ['Pending', 'Completed']:
            raise forms.ValidationError("Status must be either 'Pending' or 'Completed'.")
        return status

