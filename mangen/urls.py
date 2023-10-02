from django.contrib import admin
from django.urls import path
from arduino.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start, name='start'),
    path('compt/<str:slug>', compt, name='compt'),
    path('blue/<str:slug>', blue, name='blue'),
    path('red/<str:slug>', red, name='red'),
    path('points/<str:slug>/<int:pt>', points, name='points'),
    path('jury/<str:slug>', jury, name='jury'),
]
