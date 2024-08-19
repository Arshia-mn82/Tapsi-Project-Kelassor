from django.urls import path
from Customer_app.views import Customer_list , Show_trip_type 
urlpatterns = [
                path( "customer_list/", Customer_list),
                path("customer_list/<str:input>" , Show_trip_type )   
                ]