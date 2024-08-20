from django.urls import path
from Coupon_app.views import Coupon_list 
urlpatterns = [
                path( "coupon_list/", Coupon_list),
                ]