#!/usr.local.bin/python

import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)


if __name__ == '__main__':
    try:
        while True:
            # do main loop stuff
            time.sleep(1)

    except KeyboardInterrupt:
        print("Measurement stopped by user")
        GPIO.cleanup()


