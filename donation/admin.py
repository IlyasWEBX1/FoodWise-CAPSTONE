from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Volunteer)
admin.site.register(FoodDonor)
admin.site.register(FoodItem)
admin.site.register(DonationTransaction)

