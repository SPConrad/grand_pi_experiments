#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time,random


RUNNING = True
GPIO.setmode(GPIO.BCM)
red = 26
green = 16
blue = 19

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

Freq = 100 #hz

RED = GPIO.PWM(red, Freq)
RED.start(0)
GREEN = GPIO.PWM(green, Freq)
GREEN.start(0)
BLUE = GPIO.PWM(blue, Freq)
BLUE.start(0)

def color(R, G, B, on_time):
    RED.ChangeDutyCycle(R)
    GREEN.ChangeDutyCycle(G)
    BLUE.ChangeDutyCycle(B)
    time.sleep(on_time)
    
    RED.ChangeDutyCycle(0)
    GREEN.ChangeDutyCycle(0)
    BLUE.ChangeDutyCycle(0)


print ("Light it up!")
print ("Press CTRL + C to quit.\n")
print (" R G B\n-------")

# Main loop
try:
    while RUNNING:
        for x in range(0, 2):
            for y in range(0, 2):
                for z in range(0, 2):
                    print (x, y, z)
                    # slow ramp up power percentage of each active color
                    for i in range(0, 50):
                        color((x*i),(y*i),(z*i), 0.02)

except KeyboardInterrupt:
    RUNNING = False
    print "\Quitting"

finally:
    GPIO.cleanup()
