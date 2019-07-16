#!/usr/bin/env python3

#This sample demonstrates switching the relays with button press.
#Install IoT HAT 3 library with "pip3 install turta-iothat3"

from time import sleep
from turta_iothat3 import Turta_Button
from turta_iothat3 import Turta_Relay

#Initialize
button = Turta_Button.ButtonInput()
relay = Turta_Relay.RelayController()

try:
    while True:
        #Read button state
        button_state = button.read()

        #Switch the relays according to the button state
        #Relay 1 is activated when the button is pressed
        #Relay 2 is activated when the button is released
        relay.write(1, button_state)
        relay.write(2, not button_state)

        #Print the button state
        print("Button State....: " + ("Pressed." if button_state else "Released."))

        #Wait
        #Do not change the sleep parameter to less than 1.0 seconds
        #to protect the solid state relays
        sleep(2.0)

#Exit on CTRL+C
except KeyboardInterrupt:
    print('Bye.')
