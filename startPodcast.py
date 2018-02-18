import os
import urllib2
import RPi.GPIO as GPIO
import picamera
import time

BBC_WORLD_NEWS_RSS = 'http://podcasts.files.bbci.co.uk/p02nq0gn.rss'


on_btn = 38
off_btn = 40

button_1_last = 0
button_2_last = 0


DUMMY_LINK = 'http://open.live.bbc.co.uk/mediaselector/5/redir/version/2.0/mediaset/audio-nondrm-download/proto/http/vpid/p05y34l1.mp3'

enabled = False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(on_btn, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(off_btn, GPIO.IN, pull_up_down = GPIO.PUD_UP)


if __name__ == '__main__':
    try:
        while True:
            # do main loop stuff
            onButton = GPIO.input(on_btn)
            offButton = GPIO.input(off_btn)
            if enabled:
                if offButton == False:
                    print("off button")
        ##            GPIO.output(off_led, GPIO.HIGH)
        ##            GPIO.output(on_led, False)
                    oldOffButtonState = offButton
                    time.sleep(0.1)
                    enabled = False
        
            if onButton == False and enabled == False:
                print("on button")
                oldOnButtonState = onButton
        ##        GPIO.output(on_led, GPIO.HIGH)
        ##        GPIO.output(off_led, False)
                time.sleep(0.1)
                enabled = True
                
            time.sleep(0.001)
            

    except KeyboardInterrupt:
        print("Listening stopped by user")
        GPIO.cleanup()


