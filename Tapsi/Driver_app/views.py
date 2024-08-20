from django.http.response import HttpResponse , JsonResponse
from Driver_app.models import  Driver

def Driver_list(request):
    drivers = Driver.objects.all()
    my_driver_list = []
    for item in drivers:
        driver_dic = {
            "first_name" : item.first_name, 
            "last_name" : item.last_name, 
            "phone_number" : item.phone_number , 
            "car_color" : item.car_color,
            "car_plate" : item.car_plate,
            "car_model" : item.car_model,


        }
        my_driver_list.append(driver_dic)
    return JsonResponse(my_driver_list , safe=False)
