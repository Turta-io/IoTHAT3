#!/usr/bin/env python3

#This sample demonstrates detecting hand gestures.
#Install IoT HAT 3 library with "pip3 install turta-iothat3"

from time import sleep
from turta_iothat3 import Turta_Light
from turta_iothat3 import Turta_Buzzer

#Initialize
light = Turta_Light.LightSensor(Turta_Light.MODES.PROX_GES)
buzzer = Turta_Buzzer.BuzzerDriver()

try:
    while True:
        #Check gestures
        g = light.read_gesture()
        if g is not None:
            print("Gesture Detected: " + str(g))
            buzzer.beep()

        #Wait
        sleep(0.05)

#Exit on CTRL+C
except KeyboardInterrupt:
    print('Bye.')
