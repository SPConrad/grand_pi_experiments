import RPi.GPIO as GPIO
import picamera
import time
import requests
camera = picamera.PiCamera()

mot_sensor = 21

num = {' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(1,1,1,0,0,0,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1)}

GPIO.setmode(GPIO.BCM)
# GPIO ports for the 7seg pins
segments =  (11,4,23,8,7,10,18,25)
# 7seg_segment_pins (11,7,4,2,1,10,5,3) +  100R inline
 
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)
 
# GPIO ports for the digit 0-3 pins 
digits = (22,27,17,24)
# 7seg_digit_pins (12,9,8,6) digits 0-3 respectively
 
for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)

GPIO.setup(mot_sensor, GPIO.IN)

url = 'http://34.232.95.23/uploadfile/'
imageCount = 0
timeToSleep = 50
try:
    while True:
        #n = time.ctime()[11:13]+time.ctime()[14:16]
        #s = str(n).rjust(4)
        #s = str(imageCount).rjust(4)
        #for digit in range(4):
        #    for loop in range(0,7):
        #       GPIO.output(segments[loop], num[s[digit]][loop])
##                if (int(time.ctime()[18:19])%2 == 0) and (digit == 1):
##                    GPIO.output(25, 1)
##                else:
##                    GPIO.output(25, 0)
##            GPIO.output(digits[digit], 0)
##            time.sleep(0.001)
##            GPIO.output(digits[digit], 1)
    
##    motIO = GPIO.input(mot_sensor)
##    if motIO == 0:                 #When output from motion sensor is LOW
##        print ("No motion detected",motIO)
##        time.sleep(1.0)
##    elif motIO == 1:               #When output from motion sensor is HIGH
        epoch = time.time()
##        print ("Motion detected",motIO)
        newfile = '/home/pi/catwatcher/image_%s.jpg' % epoch
##        print (newfile)
        camera.capture(newfile)
        time.sleep(360)

        file = {'file': open(newfile, 'rb')}

        r = requests.post(url, files=file)
        
        

finally:
    GPIO.cleanup()

        
