from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User


class FoodDonor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE ,null=True, blank=True)
    organization_name = models.CharField(max_length=100, null=True, blank=True)
    food_type = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    expiry_date = models.DateField(default='2000-01-01')
    username = models.CharField(max_length=100, unique=True, null=True, blank=True)
    password = models.CharField(max_length=100)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, password):
        return check_password(password, self.password)

    def __str__(self):
        return self.organization_name

class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    birth_date = models.DateField(default='2000-01-01')
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, null=True, blank=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, password):
        return check_password(password, self.password)

    def __str__(self):
        return self.full_name

class FoodItem(models.Model):
    food_donor = models.ForeignKey(FoodDonor, on_delete=models.CASCADE ,null=True, blank=True)
    name_food = models.CharField(max_length=100, null=True, blank=True)
    expiry_date = models.DateField(default='2000-01-01')
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name_food

class DonationTransaction(models.Model):
    PENDING = 'Pending'
    COMPLETED = 'Completed'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
    ]
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=PENDING)
    donation_date = models.DateField()

    def __str__(self):
        return f"{self.food_item.name_food} donated on {self.donation_date}"
