import os
import urllib2
import RPi.GPIO as GPIO
import picamera
import time

BBC_WORLD_NEWS_RSS = 'http://podcasts.files.bbci.co.uk/p02nq0gn.rss'


# download podcast every day at 6:05AM
# put in folder
# point to newest download to play


mot_sens = 4

temp_hum = 16

button_1 = 20
button_2 = 21

button_1_last = 0
button_2_last = 0


DUMMY_LINK = 'http://open.live.bbc.co.uk/mediaselector/5/redir/version/2.0/mediaset/audio-nondrm-download/proto/http/vpid/p05y34l1.mp3'


GPIO.setmode(GPIO.BCM)

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
            button_1_input = GPIO.INPUT(button_1)
            button_2_input = GPIO.INPUT(button_2)
            if (button_1_input):
                print ("%s" % button_1_input)
                button_1_last = last
                print ("Button_1 pressed")

            if (GPIO.INPUT(button_2)):
                print ("Button_2 pressed")

                
            time.sleep(0.001)
            # start button listening script from here?
            

    except KeyboardInterrupt:
        print("Measurement stopped by user")
        GPIO.cleanup()


