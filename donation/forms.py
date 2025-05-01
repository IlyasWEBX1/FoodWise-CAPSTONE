from django import forms
from .models import Volunteer, FoodDonor

# Volunteer Sign Up Form
class VolunteerSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Volunteer
        fields = ['full_name', 'gender', 'location', 'phone_number', 'birth_date', 'username', 'password']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

# Food Donor (Mitra) Sign Up Form
class FoodDonorSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = FoodDonor
        fields = ['organization_name', 'food_type', 'location', 'phone_number', 'expiry_date', 'username', 'password']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }

# Login Form (Shared by Volunteer and FoodDonor)
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
