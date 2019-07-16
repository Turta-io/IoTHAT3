#!/usr/bin/env python3

#This sample demonstrates measuring differential analog inputs from analog ports.
#Install IoT HAT 3 library with "pip3 install turta-iothat3"

from time import sleep
from turta_iothat3 import Turta_Analog

#Initialize
analog = Turta_Analog.ADC()

try:
    while True:
        #Read differential input on left analog port
        a1_2 = analog.read(Turta_Analog.CH.DIFFERENTIAL_1_2)

        #Read differential input on right analog port
        a3_4 = analog.read(Turta_Analog.CH.DIFFERENTIAL_3_4)

        #Read board temperature
        board_temp_c = analog.read_temperature()
        board_temp_f = analog.read_temperature(True)

        #Print the readings
        print("Analog Input 1-2: " + str(a1_2))
        print("Analog Input 3-4: " + str(a3_4))
        print("Board Temp......: " + str(round(board_temp_c, 1)) + "C" + \
              " / " + str(round(board_temp_f, 1)) + "F")

        #Wait
        print("-----")
        sleep(0.5)

#Exit on CTRL+C
except KeyboardInterrupt:
    print('Bye.')
