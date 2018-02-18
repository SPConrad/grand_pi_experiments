import os
import requests
import RPi.GPIO as GPIO
import picamera
from datetime import datetime
from xml.etree import ElementTree

BBC_WORLD_NEWS_RSS = 'http://podcasts.files.bbci.co.uk/p02nq0gn.rss'


# download podcast every day at 6:05AM
# put in folder
# point to newest download to play


mot_sens = 7

temp_hum = 36


DUMMY_LINK = 'http://open.live.bbc.co.uk/mediaselector/5/redir/version/2.0/mediaset/audio-nondrm-download/proto/http/vpid/p05y34l1.mp3'

enabled = False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(mot_sens, GPIO.IN)
GPIO.setup(temp_hum, GPIO.IN)


downloadedToday = False


def download_file(url):    
    print ("download")
    r = requests.get(url)
    f = open('/home/pi/podcasts/latest.mp3', 'wb')
    print ("open")
    for chunk in r.iter_content(chunk_size=512 * 1024):
        print ("for chunk")
        if chunk:
            f.write(chunk)
            print ("writing")
    f.close()
    downloadedToday = True


def get_rss():
    url = ""
    response = requests.get(BBC_WORLD_NEWS_RSS, stream=True)
    response.raw.decode_content = True
    counter = 0
    events = ElementTree.iterparse(response.raw)
    for event, elem in events:
        counter = counter + 1
        #if elem.tag == "url":
        if (elem.items()):
            if (elem.get("type") == "audio/mpeg"):
                print ("audio/mpeg")
                url = elem.get("url")
                print (url)
                download_file(url)
                break
        if (counter > 50):
            break


if __name__ == '__main__':
    try:
        while True:
            # do main loop stuff
            time = datetime.now()
            print (time.hour)
            if (downloadedToday == False):
                if (time.hour > 7):
                    print ("it's after 7, download")
                    get_rss()
            else:
                time.sleep(3600)
            
            

    except KeyboardInterrupt:
        print("Listening stopped by user")
        GPIO.cleanup()


