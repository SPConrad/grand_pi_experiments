#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time,random, datetime

GPIO.setmode(GPIO.BCM)

hall = 19

red_pin = 16
green_pin = 21
blue_pin = 20

GPIO.setup(hall, GPIO.IN)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

Freq = 100 #hz

red_pin = GPIO.PWM(red_pin, Freq)
red_pin.start(0)
green_pin = GPIO.PWM(green_pin, Freq)
green_pin.start(0)
blue_pin = GPIO.PWM(blue_pin, Freq)
blue_pin.start(0)

RUNNING = True

def color(R, G, B):
    red_pin.ChangeDutyCycle(R)
    green_pin.ChangeDutyCycle(G)
    blue_pin.ChangeDutyCycle(B)
    
##    red_pin.ChangeDutyCycle(0)
##    green_pin.ChangeDutyCycle(0)
##    blue_pin.ChangeDutyCycle(0)

oldState = 0

def sensorCallback(channel):
# Called if sensor output goes LOW
    if GPIO.input(hall):
        timestamp = time.time()
        stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
        print "Sensor LOW " + stamp
        color((0),(2),(0))
    else: 
        # Called if sensor output goes HIGH
        timestamp = time.time()
        stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
        print "Sensor HIGH " + stamp
        color((2),(0),(0))



GPIO.add_event_detect(hall, GPIO.BOTH, callback=sensorCallback)
##GPIO.add_event_detect(hall, GPIO.RISING, callback=sensorCallback2)

try:
##    main()
    while RUNNING:
##        print(time.time())
##        if GPIO.input(hall) == 0:
##            if oldState == 1:
##                color((0),(2),(0))
##                oldState = 0
##                print("hall on")
##        if GPIO.input(hall) == 1:
##            if oldState == 0:
##                color((2),(0),(0))
##                oldState = 1
##                print("hall off") 
            
        time.sleep(0.5)


except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
