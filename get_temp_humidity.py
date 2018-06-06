import Adafruit_DHT
import time
import Adafruit_BMP.BMP085 as BMP085
import requests
import json
import RPi.GPIO as GPIO
 
# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor1=Adafruit_DHT.DHT11

GPIO.setmode(GPIO.BCM)
 
tempGPIO = 21

GPIO.setup(tempGPIO, GPIO.IN)

sleepTime = 30

url = 'http://34.232.95.23/sensors/oldbull/'

def getTemp():
  # Use read_retry method. This will retry up to 15 times to
  # get a sensor reading (waiting 2 seconds between each retry).
  humidity, temperature = Adafruit_DHT.read_retry(sensor1, tempGPIO)
   
  # Reading the DHT11 is very sensitive to timings and occasionally
  # the Pi might fail to get a valid reading. So check if readings are valid.
  if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    data = {}
    data['temp'] = temperature
    data['humidity'] = humidity
    data['sensorId'] = 0
    json_package = json.dumps(data)
    print json_package
    r = requests.post(url, json=json_package)
    print(r)
    
  else:
    print('Failed to get reading. Try again!')

if __name__ == '__main__':
    try:
        while True:
            # do main loop stuff
            print("Main loop")
            getTemp()
            time.sleep(sleepTime)
            
            

    except KeyboardInterrupt:
        print("Listening stopped by user")
        GPIO.cleanup()


