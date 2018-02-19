#!/usr/bin/python

import Adafruit_BMP.BMP085 as BMP085
import time
sensor = BMP085.BMP085()

def get_data():
    print('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
    print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()))
    print('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
    print('Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure()))



# Main loop
try:
    while True:
        get_data()
        time.sleep(5)
    
except KeyboardInterrupt:
    print "\Quitting"
    GPIO.cleanup()
    
