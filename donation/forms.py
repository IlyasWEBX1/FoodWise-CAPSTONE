from django import forms
from .models import Volunteer, FoodDonor, DonationTransaction

# Volunteer Sign Up Form
class VolunteerSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Volunteer
        fields = ['full_name', 'gender', 'location', 'phone_number', 'birth_date', 'username', 'password']
        widgets = {
            'full_name': forms.TextInput(attrs={'id': 'nama'}),
            'gender': forms.TextInput(attrs={'id': 'gender'}),
            'location': forms.TextInput(attrs={'id': 'alamat'}),
            'phone_number': forms.TextInput(attrs={'id': 'telepon'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'id': 'tanggal_lahir'}),
            'username': forms.TextInput(attrs={'id': 'username'}),
        }

# Food Donor (Mitra) Sign Up Form
class FoodDonorSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = FoodDonor
        fields = ['organization_name', 'food_type', 'location', 'phone_number', 'expiry_date', 'username', 'password']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date', 'id' : 'tanggal_kadaluwarsa'}),
            'organization_name': forms.TextInput(attrs={'id' : 'nama'}), 
            'food_type' : forms.TextInput(attrs={'id' : 'jenis_makanan'}), 
            'location' : forms.TextInput(attrs={'id' : 'alamat'}), 
            'phone_number' : forms.TextInput(attrs={'id' : 'telepon'}), 
            'username' : forms.TextInput(attrs={'id' : 'username'}), 
        }

# Login Form (Shared by Volunteer and FoodDonor)
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

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