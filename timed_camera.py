import os
import RPi.GPIO as GPIO
import picamera
import time
from shutil import copy2
import requests
from fractions import Fraction
camera = picamera.PiCamera()

camera.resolution = (1920,1080)
camera.rotation = 90
#camera.iso = 800
#camera.shutter_speed = 50000
GPIO.setmode(GPIO.BCM)

url = 'http://34.232.95.23/uploadfile/'
imageCount = 0
timeToSleep = 50
try:
    while True:
	#camera.framerate = Fraction(1, 5)
	#camera.shutter_speed = 5000000
	camera.shutter_speed = 50000
	time.sleep(10)
	epoch = time.time()
 	camera.annotate_text = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))
	camera.exposure_mode = 'off'
	newfile = '/home/pi/catwatcher/image_%s.jpg' % epoch
	camera.capture(newfile)
	print (newfile)
        uploadfile = '/home/pi/catwatcher/latest.jpg'
	os.system('cp %s %s' % (newfile, uploadfile))
	copy2(newfile, uploadfile)
        file = {'file': open(uploadfile, 'rb')}

        r = requests.post(url, files=file)
        time.sleep(360)
finally:
	GPIO.cleanup()
