# Turta IoT HAT 3 Helper for Raspbian.
# Distributed under the terms of the MIT license.

# Python Library for Solid State Relays.
# Version 1.0.0
# Released: July 16th, 2019

# Visit https://docs.turta.io for documentation.

import RPi.GPIO as GPIO

class RelayController:
    """Solid State Relays."""

    #Variables
    is_initialized = False

    #Relay Pins
    relay1, relay2 = 20, 12

    #Initialize

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.relay1, GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(self.relay2, GPIO.OUT, initial = GPIO.LOW)
        self.is_initialized = True
        return

    #Relay Write Methods

    def write(self, ch, st):
        """Controls the relay.

        Parameters:
        ch (byte): Relay channel (1 or 2)
        st (bool): Relay state (True or False)"""

        if (ch == 1):
            GPIO.output(self.relay1, GPIO.HIGH if st else GPIO.LOW)
        elif (ch == 2):
            GPIO.output(self.relay2, GPIO.HIGH if st else GPIO.LOW)
        return

    def toggle(self, ch):
        """Inverts the relay's state.

        Parameters:
        ch (byte): Relay channel (1 or 2)"""

        self.write(ch, not self.read(ch))
        return

    #Relay Read Methods

    def read(self, ch):
        """Reads the relay state.

        Parameters:
        ch (byte): Relay channel (1 or 2)

        Returns:
        bool: Relay state (True of False)"""

        if (ch == 1):
            return GPIO.input(self.relay1)
        elif (ch == 2):
            return GPIO.input(self.relay2)

    #Disposal

    def __del__(self):
        """Releases the resources."""

        try:
            if self.is_initialized:
                GPIO.output(self.relay1, GPIO.LOW)
                GPIO.output(self.relay2, GPIO.LOW)
                GPIO.cleanup()
                del self.is_initialized
        except:
            pass
