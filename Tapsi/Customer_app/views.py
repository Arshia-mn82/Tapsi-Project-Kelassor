from django.http.response import HttpResponse , JsonResponse
from Tapsi.Customer_app.models import  Customer

def Customer_list(request):
    customers = Customer.objects.all()
    my_customer_list = []
    for item in customers:
        customer_dic = {
            "first_name": item.first_name, 
            "last_name": item.last_name, 
            "phone_number" : item.phone_number , 
            "availibility" : item.availibility
            
        }
        my_customer_list.append(customer_dic)
    return JsonResponse(my_customer_list , safe=False)

def Show_trip_type(request , input):
    trips = Customer.objects.filter(trip_type = input)
    return JsonResponse(trips , safe=False)
