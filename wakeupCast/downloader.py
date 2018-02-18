import os
import urllib2
import RPi.GPIO as GPIO
import picamera
import time

BBC_WORLD_NEWS_RSS = 'http://podcasts.files.bbci.co.uk/p02nq0gn.rss'


# download podcast every day at 6:05AM
# put in folder
# point to newest download to play


mot_sens = 7

temp_hum = 36

button_1 = 38
button_2 = 40

button_1_last = 0
button_2_last = 0


DUMMY_LINK = 'http://open.live.bbc.co.uk/mediaselector/5/redir/version/2.0/mediaset/audio-nondrm-download/proto/http/vpid/p05y34l1.mp3'

enabled = False

GPIO.setmode(GPIO.BOARD)

GPIO.setup(mot_sens, GPIO.IN)
GPIO.setup(temp_hum, GPIO.IN)
GPIO.setup(button_1, GPIO.IN)
GPIO.setup(button_2, GPIO.IN)



def download_file():    
    web_file = urllib2.urlopen(DUMMY_LINK)
    out_file = open('/pi/podcasts/', 'w')
    out_file.write(web_file.read())
    out_file.close()






if __name__ == '__main__':
    try:
        while True:
            # do main loop stuff
            button_1_input = GPIO.input(button_1)
            button_2_input = GPIO.input(button_2)
            if enabled:
                if offButton == False:
                    print("off button")
        ##            GPIO.output(off_led, GPIO.HIGH)
        ##            GPIO.output(on_led, False)
                    oldOffButtonState = offButton
                    time.sleep(0.1)
                    enabled = False

                    
##            else: 
##                if (GPIO.input(button_2) == 0):
##                    print ("Button_2 pressed")

                
            time.sleep(0.001)
            # start button listening script from here?
            

    except KeyboardInterrupt:
        print("Measurement stopped by user")
        GPIO.cleanup()


