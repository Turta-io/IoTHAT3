#!/usr/bin/env python3

#This sample demonstrates most of the IoT HAT's functionality together.
#Install IoT HAT 3 library with "pip3 install turta-iothat3"

from time import sleep
from turta_iothat3 import Turta_Accel
from turta_iothat3 import Turta_Analog
from turta_iothat3 import Turta_Button
from turta_iothat3 import Turta_Buzzer
from turta_iothat3 import Turta_Light
from turta_iothat3 import Turta_Photocoupler

#Initialize
accel = Turta_Accel.AccelTiltSensor()
analog = Turta_Analog.ADC()
button = Turta_Button.ButtonInput()
buzzer = Turta_Buzzer.BuzzerDriver()
light = Turta_Light.LightSensor(Turta_Light.MODES.ALS_RGB_PROX)
photohocpler = Turta_Photocoupler.PhotocouplerInputs()

try:
    while True:
        #Read X, Y and Z-Axis G values in one shot
        accel_xyz = accel.read_accel_xyz()

        #Read tilt states in one shot
        tilt_xyz = accel.read_tilt_xyz()

        #Read analog inputs
        a1 = analog.read(Turta_Analog.CH.SINGLE_1) #Ch1

        #Read board temperature
        board_temp_c = analog.read_temperature()
        board_temp_f = analog.read_temperature(True)

        #Read button state
        button_state = button.read()

        #Read CRGB light values
        crgb = light.read_crgb_light()

        #Read proximity
        proximity = light.read_proximity()

        #Read photocoupler input states
        pc1 = photohocpler.read(1) #Ch1
        pc2 = photohocpler.read(2) #Ch2

        #Print the readings
        print("X-Axis..........: " + str(round(accel_xyz[0], 2)) + "G")
        print("Y-Axis..........: " + str(round(accel_xyz[1], 2)) + "G")
        print("Z-Axis..........: " + str(round(accel_xyz[2], 2)) + "G")

        print("X-Tilt..........: " + ("Tilt detected." if tilt_xyz[0] else "No tilt."))
        print("Y-Tilt..........: " + ("Tilt detected." if tilt_xyz[1] else "No tilt."))
        print("Z-Tilt..........: " + ("Tilt detected." if tilt_xyz[2] else "No tilt."))

        print("Ambient Light...: " + str(crgb[0])) #Ambient light = CRGB clear channel
        print("Red.............: " + str(crgb[1]))
        print("Green...........: " + str(crgb[2]))
        print("Blue............: " + str(crgb[3]))
        print("Proximity.......: " + str(proximity))

        print("Analog Input 1..: " + str(a1))
        print("Board Temp......: " + str(round(board_temp_c, 1)) + "C" + \
              " / " + str(round(board_temp_f, 1)) + "F")

        print("Button State....: " + ("Pressed." if button_state else "Released."))
        print("Photocoupler 1..: " + ("High." if pc1 else "Low."))
        print("Photocoupler 2..: " + ("High." if pc2 else "Low."))

        print("-----")
        
        #Generate sound if button is pressed
        if button.read():
            buzzer.beep()

        #Wait
        sleep(1.0)

#Exit on CTRL+C
except KeyboardInterrupt:
    print('Bye.')