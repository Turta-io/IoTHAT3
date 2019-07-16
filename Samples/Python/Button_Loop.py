#!/usr/bin/env python3

#This sample demonstrates reading onboard button press state.
#Install IoT HAT 3 library with "pip3 install turta-iothat3"

import time
from turta_iothat3 import Turta_Button

#Initialize
button = Turta_Button.ButtonInput()

try:
    while True:
        #Read button state
        button_state = button.read()

        #Print the reading
        print("Button State....: " + ("Pressed." if button_state else "Released."))

        #Wait
        time.sleep(0.5)

#Exit on CTRL+C
except KeyboardInterrupt:
    print('Bye.')
