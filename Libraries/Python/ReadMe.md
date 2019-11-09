# Python Libraries
This directory includes Python libraries for Turta IoT HAT 3.

## Index
* __Turta_Accel.py:__ Python Library for NXP MMA8491Q 3-Axis Accelerometer & Tilt Sensor.
* __Turta_Analog.py:__ Python Library for TI ADS1018 ADC.
* __Turta_Button.py:__ Python Library for Button.
* __Turta_Buzzer.py:__ Python Library for Buzzer.
* __Turta_Digital.py:__ Python Library for Digital IO Ports.
* __Turta_IRRemote.py:__ Python Library for IR Remote Controller Transmitter.
* __Turta_Light.py:__ Python Library for Broadcom APDS-9960 Ambient & RGB Light, Proximity and Gesture Detection Sensor.
* __Turta_Photocoupler.py:__ Python Library for Photocouplers.
* __Turta_Relay.py:__ Python Library for Relays.

## Installation of Python Libraries
* Use 'pip3 install turta-iothat3' to download and install libraries automatically.
* Use 'pip3 install --upgrade --user turta-iothat3' to update your libraries.
* Use 'pip3 uninstall turta-iothat3' to uninstall the libraries.
* If you wish to install libraries manually, copy the ingredients of Python folder to the project folder.
* To use the 'ATECC608A Cryptographic Co-Processor', please refer to our documentation at [docs.turta.io](https://docs.turta.io).

## Dependencies for Python Libraries
The package installer installs other libraries required for IoT HAT 3's operation.
* We're using 'SMBus' for I2C communication. To install it manually, type 'sudo pip3 install smbus' to the terminal.
* We're using 'spidev' for SPI communication. To install it manually, type 'sudo pip3 install spidev' to the terminal.
* We're using 'RPi.GPIO' for GPIO access. To install it manually, type 'pip3 install RPi.GPIO' to the terminal.
* We're using Python 3 for the libraries and samples.

## Documentation
Visit [docs.turta.io](https://docs.turta.io) for documentation.
