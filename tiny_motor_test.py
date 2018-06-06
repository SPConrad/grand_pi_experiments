import RPi.GPIO as GPIO
from time import sleep

ENABLE_PIN = 25
IN1 = 24
IN2 = 23
ENGINE_FREQ = 500

class pump:
    def __init__(self):
        self.enable_pin = ENABLE_PIN
        self.in1_pin = IN1
        self.in2_pin = IN2

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.enable_pin, GPIO.OUT)
        GPIO.setup(self.in1_pin, GPIO.OUT)
        GPIO.setup(self.in2_pin, GPIO.OUT)

        self.pwm = GPIO.PWM(self.enable_pin, ENGINE_FREQ)

    def start(self, num):
        self.pwm.start(0)
        print("start %i" % num)
        if (num == 0):
            GPIO.output(self.in1_pin, True)
            GPIO.output(self.in2_pin, False)
            
            self.pwm.ChangeDutyCycle(100)

        if (num == 1):
            GPIO.output(self.in2_pin, True)
            GPIO.output(self.in1_pin, False)
            
            self.pwm.ChangeDutyCycle(100)



    def stop(self):
        self.pwm.stop()

if __name__ == '__main__':
    p = pump()
    p.start(0)
    sleep(5)
    p.stop()
    p.start(1)
    sleep(5)
    p.stop()
    GPIO.cleanup()
