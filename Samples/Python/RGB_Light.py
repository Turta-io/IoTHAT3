#!/usr/bin/env python3

#This sample demonstrates reading RGB light.
#Install IoT HAT 3 library with "pip3 install turta-iothat3"

from time import sleep
from turta_iothat3 import Turta_Light

#Initialize
light = Turta_Light.LightSensor()

try:
    while True:
        #Read clear & RGB light values
        crgb = light.read_crgb_light()

        #Print the readings
        print("Clear...........: " + str(crgb[0]))
        print("Red.............: " + str(crgb[1]))
        print("Green...........: " + str(crgb[2]))
        print("Blue............: " + str(crgb[3]))

        #Wait
        print("-----")
        sleep(0.5)

#Exit on CTRL+C
except KeyboardInterrupt:
    print('Bye.')
