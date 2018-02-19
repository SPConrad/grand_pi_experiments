#!/usr/bin/python
import sys
import Adafruit_DHT
import platform_detect

while True:
    print("test")


    humidity, temperature = Adafruit_DHT.read_retry(11, 20)
    print("test")
    
    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
    



# Define error constants.
DHT_SUCCESS        =  0
DHT_ERROR_TIMEOUT  = -1
DHT_ERROR_CHECKSUM = -2
DHT_ERROR_ARGUMENT = -3
DHT_ERROR_GPIO     = -4
TRANSIENT_ERRORS = [DHT_ERROR_CHECKSUM, DHT_ERROR_TIMEOUT]

# Define sensor type constants.
DHT11  = 11
DHT22  = 22
AM2302 = 22
SENSORS = [DHT11, DHT22, AM2302]


def get_platform():
    """Return a DHT platform interface for the currently detected platform."""
    plat = platform_detect.platform_detect()
    if plat == platform_detect.RASPBERRY_PI:
        # Check for version 1 or 2 of the pi.
        version = platform_detect.pi_version()
        if version == 1:
            from . import Raspberry_Pi
            return Raspberry_Pi
        elif version == 2:
            from . import Raspberry_Pi_2
            return Raspberry_Pi_2
        elif version == 3:
            """Use Pi 2 driver even though running on Pi 3"""
            from . import Raspberry_Pi_2
            return Raspberry_Pi_2
        else:
            raise RuntimeError('No driver for detected Raspberry Pi version available!')
    elif plat == platform_detect.BEAGLEBONE_BLACK:
        from . import Beaglebone_Black
        return Beaglebone_Black
    else:
        raise RuntimeError('Unknown platform.')

def read(sensor, pin, platform=None):
    """Read DHT sensor of specified sensor type (DHT11, DHT22, or AM2302) on
    specified pin and return a tuple of humidity (as a floating point value
    in percent) and temperature (as a floating point value in Celsius). Note that
    because the sensor requires strict timing to read and Linux is not a real
    time OS, a result is not guaranteed to be returned!  In some cases this will
    return the tuple (None, None) which indicates the function should be retried.
    Also note the DHT sensor cannot be read faster than about once every 2 seconds.
    Platform is an optional parameter which allows you to override the detected
    platform interface--ignore this parameter unless you receive unknown platform
    errors and want to override the detection.
    """
    if sensor not in SENSORS:
        raise ValueError('Expected DHT11, DHT22, or AM2302 sensor value.')
    if platform is None:
        platform = get_platform()
    return platform.read(sensor, pin)


def read_retry(sensor, pin, retries=15, delay_seconds=2, platform=None):
    """Read DHT sensor of specified sensor type (DHT11, DHT22, or AM2302) on
    specified pin and return a tuple of humidity (as a floating point value
    in percent) and temperature (as a floating point value in Celsius).
    Unlike the read function, this read_retry function will attempt to read
    multiple times (up to the specified max retries) until a good reading can be
    found. If a good reading cannot be found after the amount of retries, a tuple
    of (None, None) is returned. The delay between retries is by default 2
    seconds, but can be overridden.
    """
    print("read retry")
    for i in range(retries):
        humidity, temperature = read(sensor, pin, platform)
        if humidity is not None and temperature is not None:
            return (humidity, temperature)
        time.sleep(delay_seconds)
    return (None, None)

