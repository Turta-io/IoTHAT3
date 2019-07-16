#!/usr/bin/env python3

#This sample demonstrates toggling the solid state relays.
#Do not toggle dc motors or solenoids frequently.
#Install IoT HAT 3 library with "pip3 install turta-iothat3"

from time import sleep
from turta_iothat3 import Turta_Relay

#Initialize
relay = Turta_Relay.RelayController()

try:
    while True:
        #Option one: Toggle the relays with 'write' method
        
        #Turn relay 1 on
        relay.write(1, True)

        #Print relay 1 state
        print("Relay 1 State...: " + ("On." if relay.read(1) else "Off."))

        #Wait
        sleep(2.0)

        #Turn relay 1 off
        relay.write(1, False)

        #Print relay 1 state
        print("Relay 1 State...: " + ("On." if relay.read(1) else "Off."))

        #Wait
        sleep(2.0)

        #Option two: Toggle the relays with 'toggle' method
        #Each method call inverts the relay's state

        #Toggle relay 2
        relay.toggle(2)

        #Print relay 2 state
        print("Relay 2 State...: " + ("On." if relay.read(2) else "Off."))

        #Wait
        sleep(2.0)

#Exit on CTRL+C
except KeyboardInterrupt:
    print('Bye.')
