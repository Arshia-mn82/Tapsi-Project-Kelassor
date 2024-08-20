from django.db import models
#from Tapsi.Coupon_app import Coupon

class Driver(models.Model):
    first_name = models.CharField(max_length=50 , help_text= "should be 50 chars")
    last_name = models.CharField(max_length=50 , help_text= "should be 50 chars")
    phone_number = models.CharField(max_length=11)
    car_color = models.CharField(max_length=50)
    car_plate = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    wallet = models.FloatField()