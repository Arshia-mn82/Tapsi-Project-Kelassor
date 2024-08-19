from django.db import models
#from Tapsi.Coupon_app import Coupon

class Customer(models.Model):
    first_name = models.CharField(max_length=50 , help_text= "should be 50 chars")
    last_name = models.CharField(max_length=50 , help_text= "should be 50 chars")
    phone_number = models.IntegerField(max_length=11)
    source_x = models.FloatField()
    source_y = models.FloatField()
    destination_x = models.FloatField()
    destination_y = models.FloatField()
    trip_type = models.CharField(max_length= 50 , help_text= "should be 50 chars")
    #coupons = models.ForeignKey(coupon , on_delete = models.PROTECT)
    availibility = models.BooleanField()
    
