# Turta IoT HAT 3 Helper for Raspbian
# Distributed under the terms of the MIT license.

# Python Library for Buzzer.
# Version 1.0.0
# Released: July 16th, 2019

# Visit https://docs.turta.io for documentation.

import RPi.GPIO as GPIO
from time import sleep

class BuzzerDriver(object):
    """Buzzer Driver."""

    #Variables
    is_initialized = False
    pwm = None

    #Buzzer Pin
    sounder = 13

    #Initialize

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.sounder, GPIO.OUT, initial = GPIO.LOW)
        self.pwm = GPIO.PWM(self.sounder, 5000)
        self.pwm.start(0)
        self.is_initialized = True
        return

    #Buzzer Control Mehtods

    def start(self, freq = 5000):
        """Generates sound.

        Parameters:
        freq (int): Frequency (1000 to 10000, default is 5000)"""

        self.pwm.ChangeFrequency(freq)
        self.pwm.start(50)
        return

    def stop(self):
        """Stops generating sound."""

        self.pwm.stop()
        return

    def beep(self):
        """Plays a 'be beep' tone."""
        self.start(1000)
        sleep(0.15)
        self.start(10000)
        sleep(0.07)
        self.stop()

    #Disposal

    def __del__(self):
        """Releases the resources."""

        try:
            if self.is_initialized:
                self.pwm.stop()
                GPIO.cleanup()
                del self.is_initialized
        except:
            pass
