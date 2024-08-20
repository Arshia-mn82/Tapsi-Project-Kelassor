from django.http.response import HttpResponse , JsonResponse
from Coupon_app.models import  Coupon

def Coupon_list(request):
    coupons = Coupon.objects.all()
    my_coupon_list = []
    for item in coupons:
        coupon_dic = {
            "title": item.title, 
            "expire_date" : item.expire_date,
            "percent": item.percent, 
            "coupon_availibility" : item.coupon_availability
            
        }
        my_coupon_list.append(coupon_dic)
    return JsonResponse(my_coupon_list , safe=False)
