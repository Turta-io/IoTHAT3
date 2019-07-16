# Turta IoT HAT 3 Helper for Raspbian.
# Distributed under the terms of the MIT license.

# Python Library for Button.
# Version 1.0.0
# Released: July 16th, 2019

# Visit https://docs.turta.io for documentation.

import RPi.GPIO as GPIO

class ButtonInput(object):
    """Button Input."""

    #Variables
    is_initialized = False

    #Button Pin
    button = 5

    #Initialize

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.button, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        self.is_initialized = True
        return

    #Button Read Methods

    def read(self):
        """Reads the button press state.

        Returns:
        bool: Button press state (True if pressed, False if not)"""

        return not GPIO.input(self.button)

    #Disposal

    def __del__(self):
        """Releases the resources."""

        try:
            if self.is_initialized:
                GPIO.cleanup()
                del self.is_initialized
        except:
            pass
