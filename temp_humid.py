import Adafruit_DHT
import time
 
# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor=Adafruit_DHT.DHT11
 
# Set GPIO sensor is connected to
gpio=26

sleepTime = 3

def getTemp(): 
  # Use read_retry method. This will retry up to 15 times to
  # get a sensor reading (waiting 2 seconds between each retry).
  humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
   
  # Reading the DHT11 is very sensitive to timings and occasionally
  # the Pi might fail to get a valid reading. So check if readings are valid.
  if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
  else:
    print('Failed to get reading. Try again!')



if __name__ == '__main__':
    try:
        while True:
            # do main loop stuff
            getTemp()
            time.sleep(sleepTime)
            
            

    except KeyboardInterrupt:
        print("Listening stopped by user")
        GPIO.cleanup()


