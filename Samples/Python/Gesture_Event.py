#!/usr/bin/env python3

#This sample demonstrates detecting hand gestures using GPIO interrupt.
#Install IoT HAT 3 library with "pip3 install turta-iothat3"

from time import sleep
import RPi.GPIO as GPIO
from turta_iothat3 import Turta_Light
from turta_iothat3 import Turta_Buzzer

#Gesture Event
def gesture_event(ch):
    g = light.read_gesture()
    if g is not None:
        print("Gesture Detected: " + str(g))
        buzzer.beep()

#Interrupt Pin
gesture_int = 4

#Initialize
light = Turta_Light.LightSensor(Turta_Light.MODES.PROX_GES, True)
buzzer = Turta_Buzzer.BuzzerDriver()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(gesture_int, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(gesture_int, GPIO.FALLING, callback=gesture_event, bouncetime=1)

#Add your configuration code here

try:
    while True:
        #Add your code here

        #Wait
        sleep(1.0)

#Exit on CTRL+C
except KeyboardInterrupt:
    GPIO.cleanup()
    print('Bye.')
