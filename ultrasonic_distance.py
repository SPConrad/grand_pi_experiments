#!/usr.local.bin/python

import RPi.GPIO as GPIO
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0


# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# 128x64 display with hardware I2C:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
def clearDisplay():
    disp.clear()
    disp.display()


class Corner:
    front = 0
    back = 1
    left = 0
    right = 1
    
    label = ""
    distanceArray = []
    

    def __init__(self, label):
        self.label = label

    def setLabel(label):
        self.label = label

    def addToDistanceArray(newDistance):
        self.distanceArray.append(newDistance)

    def getPositionTarget():
        return

    def getAverage():
        average = 0
        for num in self.distanceArray:
            average = average + num

        average = average / len(self.distanceArray)

        return average

GPIO.setmode(GPIO.BCM)

trig = 5
echo = 26

TRIG = 5
ECHO = 26

distanceArray = []

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def distance():
    GPIO.output(TRIG, False)
    print "Waiting For Sensor To Settle"
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
      pulse_start = time.time()

    while GPIO.input(ECHO)==1:
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)
    
    return distance

def getAverageOfArray(array):
    average = 0
    for num in array:
        average = average + num

    average = average / len(distanceArray)

    return average

    
corners = []
corners.append(Corner("back-right"))
corners.append(Corner("back-left"))
corners.append(Corner("front-right"))
corners.append(Corner("front-left"))

font = ImageFont.truetype("/home/pi/Downloads/fonts/OpenSans-Regular.ttf", 18)

def writeDistance(distance):
    clearDisplay()
    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    width = disp.width
    height = disp.height
    image = Image.new('1', (width, height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)
    displayString = "AvDst: %.2fcm" % distance
    
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    draw.text((10, 10), displayString, font=font, fill=255)

    
        
    disp.image(image)
    disp.display()

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            distanceArray.append(dist)
            print ("Measured distance = %.1f cm" % dist)
            
            print ("Current average = %.1f cm" % getAverageOfArray(distanceArray))
            writeDistance(getAverageOfArray(distanceArray))
    except KeyboardInterrupt:
        print("Measurement stopped by user")
        GPIO.cleanup()
