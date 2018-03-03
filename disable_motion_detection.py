import RPi.GPIO as GPIO
import time
import os
from subprocess import check_output

btn=7
led=40

dht11_gpio = 26

enabled = False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(btn, GPIO.IN, pull_up_down = GPIO.PUD_UP)

oldButtonState = True

def listen_for_input(enabled):
    button = GPIO.input(btn)
    if enabled == True:
        if button == False:
            print("button")
            oldButtonState = False
            GPIO.output(led, False)
            disable_motion()
            time.sleep(1.0)
            enabled = False
    else:
        if button == False and enabled == False:
            enabled = True
            GPIO.output(led, True)
            print("restart")
            os.system("sudo motion -b")
            time.sleep(1.0)
            

    return enabled

def get_pid(name):
    return check_output(["pidof", name])

def disable_motion():
    pids = get_pid("motion")
    pids = pids.split(' ')
    for pid in pids:
        os.system("sudo kill %s" % pid)
        print("pid is %s" % pid)


# Main Loop
try:
    
    while True:
        enabled = listen_for_input(enabled)

except KeyboardInterrupt:
    print "\Quitting"
    GPIO.cleanup()
        
