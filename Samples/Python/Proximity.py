#!/usr/bin/env python3

#This sample demonstrates measuring proximity.
#Install IoT HAT 3 library with "pip3 install turta-iothat3"

from time import sleep
from turta_iothat3 import Turta_Light

#Initialize
light = Turta_Light.LightSensor(Turta_Light.MODES.PROX)

try:
    while True:
        #Read proximity
        proximity = light.read_proximity()

        #Print the reading
        print("Proximity.......: " + str(proximity))

        #Wait
        sleep(0.5)

#Exit on CTRL+C
except KeyboardInterrupt:
    print('Bye.')
