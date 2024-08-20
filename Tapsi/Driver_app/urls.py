from django.urls import path
from Driver_app.views import Driver_list
urlpatterns = [
                path( "driver_list/", Driver_list),
                ]