import RPi.GPIO as GPIO
import picamera
import time
import Adafruit_DHT
#camera = picamera.PiCamera()


off_btn=38
on_btn=40
##on_led=7
##off_led=36
##temp_sens=37
##mot_sens=38
##
dht11=Adafruit_DHT.DHT11
dht11_gpio = 26

enabled = True

GPIO.setmode(GPIO.BOARD)
GPIO.setup(off_btn, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(on_btn, GPIO.IN, pull_up_down = GPIO.PUD_UP)
##GPIO.setup(on_led, GPIO.OUT)
##GPIO.setup(off_led, GPIO.OUT)
##GPIO.setup(mot_sens, GPIO.IN)

oldOffButtonState = True
oldOnButtonState = True

##GPIO.output(on_led, GPIO.HIGH)
##GPIO.output(off_led, GPIO.HIGH)
##GPIO.output(off_led, False)

while True:
    
##    humidity, temperature = Adafruit_DHT.read_retry(dht11, dht11_gpio)
##
##    if humidity is not None and temperature is not None:
##      print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
##    else:
##      print('Failed to get reading. Try again!')


    # If it's enabled
    offButton = GPIO.input(off_btn)
    onButton = GPIO.input(on_btn)

    if enabled:
        if offButton == False:
            print("off button")
##            GPIO.output(off_led, GPIO.HIGH)
##            GPIO.output(on_led, False)
            oldOffButtonState = offButton
            time.sleep(0.1)
            enabled = False
        ##else:
            # Otherwise, listen for input
##            motIO = GPIO.input(mot_sens)

            # Listen for motion input
##            if motIO == 0:
##                print ("No motion detected",motIO)
##            elif motIO == 1:               
##                epoch = time.time()
##                print ("Motion detected",motIO)
##                #camera.capture('image_%s.jpg' % epoch)
##                time.sleep(0.1)
    

    if onButton == False and enabled == False:
        print("on button")
        oldOnButtonState = onButton
##        GPIO.output(on_led, GPIO.HIGH)
##        GPIO.output(off_led, False)
        time.sleep(0.1)
        enabled = True
    

        
##    if enabled:
##        
##        # If the off button is pushed, turn it off
##        offIO = GPIO.input(off_btn)
##        if offIO == 1:
##            enabled = False
##            GPIO.output(on_led, False)
##            GPIO.output(off_led, True)
        #else:
            # Otherwise, listen for input
            #motIO = GPIO.input(mot_sens)
            #tempIO = GPIO.input(temp_sens)

            # Listen for motion input
            #if motIO == 0:
            #    print ("No motion detected",motIO)
            #elif motIO == 1:               
            #    epoch = time.time()
            #    print ("Motion detected",motIO)
                #camera.capture('image_%s.jpg' % epoch)
            #    time.sleep(0.1)
                
            # Listen for humditiy/temp input
            #if tempIO == 0:
            #    print ("No temp and humidity",motIO)
            #    time.sleep(1.0)
            #elif tempIO == 1:       
            #    print ("Temp and humidity",motIO)
    # If we're turned off
    #else:
        # Listen for the on button
        #onIO = GPIO.input(on_btn)
        # If the button is pushed, turn it on
        #if onIO == 1:
        #    enabled = True
        #    GPIO.output(off_led, False)
        #    GPIO.output(on_led, True)
            

        
