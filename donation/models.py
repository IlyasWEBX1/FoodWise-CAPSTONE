from django.db import models

# Create your models here.
class FoodDonor(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    name_food = models.CharField(max_length=100)
    expiry_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name_food

class DonationTransaction(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    donation_date = models.DateField()

    def __str__(self):
        return f"{self.food_item.name_food} donated on {self.donation_date}"
