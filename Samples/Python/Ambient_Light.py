#!/usr/bin/env python3

#This sample demonstrates reading the ambient light data.
#Install IoT HAT 3 library with "pip3 install turta-iothat3"

from time import sleep
from turta_iothat3 import Turta_Light

#Initialize
light = Turta_Light.LightSensor()

try:
    while True:
        #Read ambient light
        al = light.read_ambient_light()

        #Print the reading
        print("Ambient Light...: " + str(al))

        #Wait
        sleep(0.5)

#Exit on CTRL+C
except KeyboardInterrupt:
    print('Bye.')
