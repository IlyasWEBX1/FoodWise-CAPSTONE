from django.db import models
import datetime

class FoodDonor(models.Model):
    organization_name = models.CharField(max_length=100,null=True, blank=True)  # Nama Perusahaan/Perorangan
    food_type = models.CharField(max_length=100 ,null=True, blank=True)          # Jenis Makanan
    location = models.CharField(max_length=255 ,null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    expiry_date = models.DateField(default='2000-01-01')
    username = models.CharField(max_length=100, unique=True ,null=True, blank=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.organization_name

class Volunteer(models.Model):
    full_name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10 ,null=True, blank=True)
    location = models.CharField(max_length=255 ,null=True, blank=True)
    phone_number = models.CharField(max_length=20 ,null=True, blank=True)
    birth_date = models.DateField(default='2000-01-01')
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100 ,null=True, blank=True)

    def __str__(self):
        return self.full_name

class FoodItem(models.Model):
    name_food = models.CharField(max_length=100)
    expiry_date = models.CharField(max_length=20, null=True, blank=True)
    quantity = models.IntegerField()

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
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    donation_date = models.DateField()

    def __str__(self):
        return f"{self.food_item.name_food} donated on {self.donation_date}"
