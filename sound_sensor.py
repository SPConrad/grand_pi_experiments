import time
import requests
import json
import RPi.GPIO as GPIO
import logging

GPIO.setmode(GPIO.BCM)
 
# Set GPIO sensor is connected to
soundGpio = 21

GPIO.setup(soundGpio, GPIO.IN)

sleepTime = 10

url = 'http://34.232.95.23/homeauto/environment/'



def getSound():
    if GPIO.input(soundGpio) == GPIO.LOW:
        print("sound input low")
        #time.sleep(10)
  
  


if __name__ == '__main__':
    try:
        while True:
            # do main loop stuff
            #getSound()
            time.sleep(0.1)
            log_form = '%(levelname)s } %(asctime)-15s | %(message)s'
            logging.basicConfig(format=log_format, level=logging.DEBUG)
            
            
            

    except KeyboardInterrupt:
        print("Listening stopped by user")
        GPIO.cleanup()


