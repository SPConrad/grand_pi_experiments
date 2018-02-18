import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
mic=35
vib=37
mot=38
GPIO.setmode(GPIO.BOARD)
GPIO.setup(mic, GPIO.IN) 
GPIO.setup(vib, GPIO.IN)
GPIO.setup(mot, GPIO.IN)
GPIO.setup
while True:
    micIO=GPIO.input(35)
    vib=GPIO.input(37)
    mot=GPIO.input(38)

    
    if micIO==0:                 #When output from motion sensor is LOW
        print ("No sound",micIO)
        time.sleep(0.1)
    elif micIO==1:               #When output from motion sensor is HIGH
        print ("Sound",micIO)
        time.sleep(0.1)

        
    

    
    if vib==0:                 #When output from motion sensor is LOW
        print ("No shake",vib)
        time.sleep(0.1)
    elif vib==1:               #When output from motion sensor is HIGH
        print ("Shake detected",vib)
        time.sleep(0.1)

