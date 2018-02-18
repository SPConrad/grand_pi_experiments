#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

light_sensor = 38

def rc_time(light_sensor):
    count = 0
    #Output on the pin
    GPIO.setup(light_sensor, GPIO.OUT)
    GPIO.output(light_sensor, GPIO.LOW)
    time.sleep(0.1)

    #Listen for input
    GPIO.setup(light_sensor, GPIO.IN)

    #Count until the pin goes to "high"
    while (GPIO.input(light_sensor) == GPIO.LOW):
        count +=1

    return count

try:
    # main loop
    while True:
        print rc_time(light_sensor)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
