from django import forms
from donation.models import Volunteer, FoodDonor

# Volunteer Sign Up Form
class VolunteerSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    gender = forms.ChoiceField(
        choices=Volunteer.GENDER_CHOICES,
        widget=forms.RadioSelect(attrs={'id': 'gender'}),
        required=True
    )

    class Meta:
        model = Volunteer
        fields = ['full_name', 'gender', 'location', 'phone_number', 'birth_date', 'username', 'password']
        widgets = {
            'full_name': forms.TextInput(attrs={'id': 'nama'}),
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
        fields = ['organization_name', 'location', 'phone_number', 'username', 'password']
        widgets = {
            'organization_name': forms.TextInput(attrs={'id' : 'nama'}), 
            'location' : forms.TextInput(attrs={'id' : 'alamat'}), 
            'phone_number' : forms.TextInput(attrs={'id' : 'telepon'}), 
            'username' : forms.TextInput(attrs={'id' : 'username'}), 
        }

# Login Form (Shared by Volunteer and FoodDonor)
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

