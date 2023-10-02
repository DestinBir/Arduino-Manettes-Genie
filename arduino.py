import pyfirmata
from time import sleep
from playsound import playsound
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mangen.settings")
django.setup()

from django.shortcuts import redirect

def timer(t) : 
    while t!=0:
        t=t-1
        sleep(1)
    False

code = '0001'



port = 'COM8'
try:
    arduino = pyfirmata.Arduino(port)
    print('Arduino conected')
    run = True
except:
    print('Arduino disconected')
    run = False

if run:
    blue = arduino.get_pin('d:2:i')
    red = arduino.get_pin('d:3:i')
    it = pyfirmata.util.Iterator(arduino)
    it.start()

while run:
#    try:
    val_b = blue.read()
    val_r = red.read()
    if val_r:
        redirect("red", code)
        print('Rouge')
        playsound('1.wav')
        
        
    if val_b:
        redirect("blue", code)
        print('Blue')
        playsound('2.wav')
            
#    except:
#       print('Arduino disconnected')
