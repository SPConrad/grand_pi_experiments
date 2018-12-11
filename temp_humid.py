import Adafruit_DHT
import time
import requests
import json
import RPi.GPIO as GPIO
 
# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor = Adafruit_DHT.DHT11

room = "fireplace"

GPIO.setmode(GPIO.BCM)
 
# Set GPIO sensor is connected to
sensorPin = 18

GPIO.setup(sensorPin, GPIO.IN)

sleepTime = 1800

url = 'http://spconrad.com/newreading/'
def getTemp(): 
  # Use read_retry method. This will retry up to 15 times to
  # get a sensor reading (waiting 2 seconds between each retry).
  print("Get temp")
  humidity, temperature = Adafruit_DHT.read_retry(sensor, sensorPin)
  print("Got temp")
  # Reading the DHT11 is very sensitive to timings and occasionally
  # the Pi might fail to get a valid reading. So check if readings are valid.
  if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    #data = {}
    #data['sensor_id'] = room
    #data['temp'] = temperature
    #data['humidity'] = humidity
    #formData = dict(room='fireplace', temp=temperature, humidity=humidity)
    payload = {'room': room, 'temp': temperature,'humidity': humidity}
    #print(data)
    #jsonData = json.dumps(data)
    headers = {'content-type': 'multipaert/form-data'}
    r = requests.request("POST", url, data=payload, params=headers)
    
    print(r.request)

    print(r.status_code)
    print(r.text)
    print(r.headers)
    print(r.encoding)
  else:
    print('Failed to get reading. Try again!')

    
def test(): 
  # Use read_retry method. This will retry up to 15 times to
  # get a sensor reading (waiting 2 seconds between each retry).
  print("Get temp")
  humidity, temperature = Adafruit_DHT.read_retry(sensor, sensorPin)
  print("Got temp")

  if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))

if __name__ == '__main__':
    try:
        while True:
            # do main loop stuff
            getTemp()
            time.sleep(sleepTime)
            print("loop")
            
            

    except KeyboardInterrupt:
        print("Listening stopped by user")
        GPIO.cleanup()


