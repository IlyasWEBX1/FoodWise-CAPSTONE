from django import forms
from .models import Volunteer, FoodDonor, DonationTransaction, FoodItem

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name_food', 'expiry_date', 'quantity']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date', 'id' : 'tanggal_kadaluwarsa'}),
            'name_food' : forms.TextInput(attrs={'id' : 'nama_makanan'}), 
            'quantity' : forms.TextInput(attrs={'id' : 'kuantitas'}), 
        }
        
class DonationTransactionForm(forms.ModelForm):
    class Meta:
        model = DonationTransaction
        fields = ['food_item', 'volunteer', 'status', 'donation_date']
        widgets = {
            'donation_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_status(self):
        status = self.cleaned_data.get('status')
        if status not in ['Pending', 'Completed']:
            raise forms.ValidationError("Status must be either 'Pending' or 'Completed'.")
        return status

