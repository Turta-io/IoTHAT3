#!/usr/bin/env python3

#This sample demonstrates reading input states of photocoupler.
#Install IoT HAT 3 library with "pip3 install turta-iothat3"

from time import sleep
from turta_iothat3 import Turta_Photocoupler

#Initialize
photohocpler = Turta_Photocoupler.PhotocouplerInputs()

try:
    while True:
        #Read photocoupler input states
        pc1 = photohocpler.read(1)
        pc2 = photohocpler.read(2)

        #Print the readings
        print("Photocoupler 1..: " + ("High." if pc1 else "Low."))
        print("Photocoupler 2..: " + ("High." if pc2 else "Low."))

        #Wait
        print("-----")
        sleep(0.5)

#Exit on CTRL+C
except KeyboardInterrupt:
    print('Bye.')
