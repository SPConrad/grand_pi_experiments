#!/usr.local.bin/python

import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)


green = 23
blue = 18

trig = 25
echo = 24


GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)


GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

def distance():
    GPIO.output(trig, True)

    time.sleep(0.00001)
    GPIO.output(trig, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(echo) == 0:
        StartTime = time.time()

    while GPIO.input(echo) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime

    distance = (TimeElapsed * 34300) / 2

    return distance

##def beep():
##    print ("Beep")
##    GPIO.output(blue, GPIO.LOW)
##    time.sleep(1.0)
##    GPIO.output(blue, GPIO.HIGH)

if __name__ == '__main__':
    try:
        while True:
            #dist = distance()
            #print ("Measured distance = %.1f cm" % dist)
            time.sleep(1)
            beep()

    except KeyboardInterrupt:
        print("Measurement stopped by user")
        GPIO.cleanup()
