#!/usr/bin/env python3

#This sample demonstrates reading input states of photocoupler using interrupt.
#Install IoT HAT 3 library with "pip3 install turta-iothat3"

from time import sleep
import RPi.GPIO as GPIO

#Photocoupler 1 Event
def pc1_event(ch):
    print ("Photocoupler 1 is " + ("high. " if GPIO.input(pc1) else "low."))

#Photocoupler 2 Event
def pc2_event(ch):
    print ("Photocoupler 2 is " + ("high. " if GPIO.input(pc2) else "low."))

#Photocoupler Pins
pc1, pc2 = 16, 19

#Initialize
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pc1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(pc2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.add_event_detect(pc1, GPIO.BOTH, callback=pc1_event, bouncetime=10)
GPIO.add_event_detect(pc2, GPIO.BOTH, callback=pc2_event, bouncetime=10)
#GPIO Edge detection options: GPIO.BOTH, GPIO.RISING or GPIO.FALLING

#Add your configuration code here

try:
    while True:
        #Add your code here

        #Wait
        sleep(1.0)

#Exit on CTRL+C
except KeyboardInterrupt:
    print('Bye.')
