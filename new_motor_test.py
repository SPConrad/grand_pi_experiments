# Servo Control
import time
from RPIO import PWM

servo = PWM.Servo()
motor = 18

# Set servo on GPIO17 to 1200 (1.2ms)
servo.set_servo(motor, 1200)

# Set servo on GPIO17 to 2000 (2.0ms)
servo.set_servo(motor, 2000)

# Clear servo on GPIO17
servo.stop_servo(motor)

