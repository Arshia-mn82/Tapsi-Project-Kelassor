from django.db import models

class Coupon(models.Model):
    title = models.CharField(max_length=50 , help_text= "should be 50 chars")
    expire_date = models.DateField()
    percent = models.FloatField()
    coupon_availability = models.BooleanField()
