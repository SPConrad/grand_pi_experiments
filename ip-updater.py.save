import requests
import string
import json
import time

url = 'http://34.232.95.23/automation/helper/'

def checkIp():
    print("check ip")
    output = requests.get("https://api.ipify.org?format=json").text
    print(output)
    resp = json.loads(output)
    for item in resp:
        print(item)
        print(resp[item])
        address = resp["ip"]

    r = requests.post(url, data={"address" : address})

    print r.content
    print r.text





try:
    while True:
        checkIp()
        time.sleep(600)

finally:
    print ("keyboard interrupt")
