from django.db import models
from PIL import Image
import datetime
import os
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.utils.text import slugify


class FoodDonor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE ,null=True, blank=True)
    organization_name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    username = models.CharField(max_length=100, unique=True, null=True, blank=True)
    password = models.CharField(max_length=100)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, password):
        return check_password(password, self.password)

    def __str__(self):
        return self.organization_name

class Volunteer(models.Model):
    GENDER_CHOICES = [("Male", 'Laki-laki'),("Female", 'Perempuan')]
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
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
    def food_image_upload_path(instance, filename):
        ext = filename.split('.')[-1]
        donor = slugify(instance.food_donor.organization_name or "anon")
        food = slugify(instance.name_food or "makanan")
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{timestamp}_{donor}_{food}.{ext}"
        
        return os.path.join('food_images/', filename)
    
    food_donor = models.ForeignKey(FoodDonor, on_delete=models.CASCADE ,null=True, blank=True)
    name_food = models.CharField(max_length=100, null=True, blank=True)
    expiry_date = models.DateField(default='2000-01-01')
    quantity = models.IntegerField(null=True, blank=True)
    img = models.ImageField(upload_to=food_image_upload_path, null=True, blank=True)
    
    def __str__(self):
        return self.name_food
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.img:
            img_path = self.img.path
            with Image.open(img_path) as image:
                max_size = (800, 800)
                image.thumbnail(max_size)  # Resize in-place (maintain aspect ratio)
                image.save(img_path)


class DonationTransaction(models.Model):
    def delivery_evidence_upload_path(instance, filename):
        ext = filename.split('.')[-1]
        volunteer_id = slugify(instance.volunteer_id or "anon")
        donor_id = slugify(instance.food_item.food_donor.id or "anon")
        id_transaction = slugify(instance.id or "id")
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{timestamp}_{id_transaction}_{volunteer_id}_{donor_id}.{ext}"
        
        return os.path.join('transaction_evidence/', filename)
    
    MENUNGGU_DIAMBIL = 'Menunggu Diambil'
    MENUNGGU_DISALURKAN = 'Menunggu Disalurkan'
    TELAH_DISALURKAN = 'Telah Disalurkan'
    SELESAI = 'Selesai'
    STATUS_CHOICES = [
        (MENUNGGU_DIAMBIL, 'Menunggu Diambil'),
        (MENUNGGU_DISALURKAN, 'Menunggu Disalurkan'),
        (TELAH_DISALURKAN, 'Telah Disalurkan'),
        (SELESAI, 'Selesai')
    ]
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=MENUNGGU_DIAMBIL)
    donation_date = models.DateField()
    delivery_evidence = models.ImageField(upload_to=delivery_evidence_upload_path, null=True, blank=True)


    def __str__(self):
        return f"{self.food_item.name_food} donated on {self.donation_date}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.delivery_evidence:
            img_path = self.delivery_evidence.path
            with Image.open(img_path) as image:
                max_size = (800, 800)
                image.thumbnail(max_size)  # Resize in-place (maintain aspect ratio)
                image.save(img_path)
