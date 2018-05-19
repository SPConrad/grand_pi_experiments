import RPi.GPIO as GPIO
import requests
import time

control = [5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]

motor1_bcm = 18
#motor2_bcm = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1_bcm,GPIO.OUT)
#GPIO.setup(motor2_bcm,GPIO.OUT)

m1 = GPIO.PWM(motor1_bcm, 50)
#m2 = GPIO.PWM(motor2_bcm, 50)

m1.start(2.5)
#m2.start(7.5)

try:
    while True:
        for x in range(11):
            m1.ChangeDutyCycle(control[x])
            time.sleep(0.05)
            print x

        for x in range (9, 0, -1):
            m1.ChangeDutyCycle(control[x])
            time.sleep(0.05)
            print x

except KeyboardInterrupt:
    GPIO.cleanup()
