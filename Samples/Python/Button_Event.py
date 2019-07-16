#!/usr/bin/env python3

#This sample demonstrates reading onboard button press state using interrupt.
#Install IoT HAT 3 library with "pip3 install turta-iothat3"

from time import sleep
import RPi.GPIO as GPIO

#Button Press Event
def button_event(ch):
    print ("Button is " + ("released. " if GPIO.input(button) else "pressed."))

#Button Pin
button = 5

#Initialize
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(button, GPIO.BOTH, callback=button_event, bouncetime=100)
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
