import requests
import string
import json
import time

url = 'http://34.232.95.23/automation/ip-update/'

def checkIp():
    print("check ip")
    output = requests.get("https://api.ipify.org?format=json").text
    print(output)
    resp = json.loads(output)
    for item in resp:
        print(item)
        print(resp[item])

    r = requests.post(url, 
        




try:
    while True:
        checkIp()
        time.sleep(60)

finally:
    print ("keyboard interrupt")
