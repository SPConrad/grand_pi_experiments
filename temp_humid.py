import Adafruit_DHT
import time
import Adafruit_BMP.BMP085 as BMP085
import requests
import json
import RPi.GPIO as GPIO
 
# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor1=Adafruit_DHT.DHT11
#sensor2=BMP085.BMP085()

GPIO.setmode(GPIO.BCM)
 
# Set GPIO sensor is connected to
#soundGpio = 21
humidGpio = 17

#GPIO.setup(soundGpio, GPIO.IN)
GPIO.setup(humidGpio, GPIO.IN)

sleepTime = 10

url = 'http://34.232.95.23/homeauto/environment/'

def getTemp(): 
  # Use read_retry method. This will retry up to 15 times to
  # get a sensor reading (waiting 2 seconds between each retry).
  humidity, temperature = Adafruit_DHT.read_retry(sensor1, humidGpio)
   
  # Reading the DHT11 is very sensitive to timings and occasionally
  # the Pi might fail to get a valid reading. So check if readings are valid.
  if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
  else:
    print('Failed to get reading. Try again!')

def getTpas():
  print('Temp = {0:0.2f} *C'.format(sensor2.read_temperature()))
  print(sensor2.read_temperature())
  print('Pressure = {0:0.2f} Pa'.format(sensor2.read_pressure()))
  print('Altitude = {0:0.2f} m'.format(sensor2.read_altitude()))
  print('Sealevel Pressure = {0:0.2f} Pa'.format(sensor2.read_sealevel_pressure()))
  data = {}
  data['temp'] = sensor2.read_temperature()
  data['pres'] = sensor2.read_pressure()
  data['alt'] = sensor2.read_altitude()
  data['spres'] = sensor2.read_sealevel_pressure()
  print (json.dumps(data))
  #r = requests.post(url, json=json)
  #print (r.status_code)
  #print (r.json())

  
  


if __name__ == '__main__':
    try:
        while True:
            # do main loop stuff
            getTemp()
            #getTpas()
            time.sleep(sleepTime)
            
            

    except KeyboardInterrupt:
        print("Listening stopped by user")
        GPIO.cleanup()


