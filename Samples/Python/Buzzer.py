#!/usr/bin/env python3

#This sample demonstrates using the piezo sounder.
#Install IoT HAT 3 library with "pip3 install turta-iothat3"

from time import sleep
from turta_iothat3 import Turta_Buzzer

#Initialize
buzzer = Turta_Buzzer.BuzzerDriver()

try:
    while True:
        #Generate sound
        #You can change the frequency between 1000 to 10000 Hz
        buzzer.start(1000)
        sleep(0.2)
        buzzer.start(2000)
        sleep(0.1)
        buzzer.stop()

        #Wait
        sleep(2.0)

        #Alternatively, beep method generates a 'be-beep' tone
        buzzer.beep()

        #Wait
        sleep(2.0)

#Exit on CTRL+C
except KeyboardInterrupt:
    print('Bye.')
