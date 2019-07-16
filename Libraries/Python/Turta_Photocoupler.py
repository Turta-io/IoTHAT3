# Turta IoT HAT 3 Helper for Raspbian.
# Distributed under the terms of the MIT license.

# Python Library for Photocouplers.
# Version 1.0.0
# Released: July 16th, 2019

# Visit https://docs.turta.io for documentation.

import RPi.GPIO as GPIO

class PhotocouplerInputs:
    """Photocoupler Inputs"""

    #Variables
    is_initialized = False

    #Photocoupler Pins
    pc1, pc2 = 16, 19

    #Initialize

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pc1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(self.pc2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        self.is_initialized = True
        return

    #Photocoupler Read Methods

    def read(self, ch):
        """Reads the photocoupler input state.

        Parameters:
        ch (byte): Photocoupler channel (1 or 2)

        Returns:
        bool: Photocoupler input state (True for high, False for low)"""

        if (ch == 1):
            return GPIO.input(self.pc1)
        elif (ch == 2):
            return GPIO.input(self.pc2)

    #Disposal

    def __del__(self):
        """Releases the resources."""

        try:
            if self.is_initialized:
                GPIO.cleanup()
                del self.is_initialized
        except:
            pass
