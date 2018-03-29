#!/usr/bin/python

from lib_oled96 import ssd1306
import time
from PIL import ImageFont, ImageDraw, Image
font = ImageFont.truetype('FreeSerif.ttf', 15)
import Adafruit_BMP.BMP085 as BMP085
sensor = BMP085.BMP085()

from smbus import SMBus

i2cbus = SMBus(1)

oled = ssd1306(i2cbus)
draw = oled.canvas

def get_data():
    oled.cls()
    temp = 'Temp: {0:0.2f} *C'.format(sensor.read_temperature())
    pres = 'Press: {0:0.2f} Pa'.format(sensor.read_pressure())
    alt = 'Alt: {0:0.2f} m'.format(sensor.read_altitude())
    print(temp)
    print(pres)
    print(alt)
    draw.text((0, 0), time.strftime("%I:%M:%S"), font=font, fill=1)
    draw.text((0, 15), temp, font=font, fill=1)
    draw.text((0, 30), pres, font=font, fill=1)
    draw.text((0, 45), alt, font=font, fill=1)
    oled.display()


# Main loop
try:
    while True:
        get_data()
        time.sleep(2)
    
except KeyboardInterrupt:
    print "\Quitting"
    #GPIO.cleanup()
    
