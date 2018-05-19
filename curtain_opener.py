#!/usr/bin/python
# Import required libraries
import sys
import time
from datetime import datetime
import RPi.GPIO as GPIO
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24
StepPins = [6,13,19,26]
 
# Set all pins as output
for pin in StepPins:
  #print "Setup pins"
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)
 
# Define advanced sequence
# as shown in manufacturers datasheet
Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]
        
StepCount = len(Seq)
StepDir = 1 # Set to 1 or 2 for clockwise
            # Set to -1 or -2 for anti-clockwise
 
# Read wait time from command line
if len(sys.argv)>1:
  WaitTime = int(sys.argv[1])/float(1000)
else:
  WaitTime = 10/float(1000)

#500 full steps = 1 rotation


def motor():
  StepCounter = 0
  run = True
  runs = 0
  while run == True:
    print StepCounter,
    #print Seq[StepCounter]
   
    for pin in range(0,4):
      xpin=StepPins[pin]# Get GPIO
      if Seq[StepCounter][pin]!=0:
        #print " Enable GPIO %i" %(xpin)
        GPIO.output(xpin, True)
      else:
        GPIO.output(xpin, False)
   
    StepCounter += StepDir
   
    # If we reach the end of the sequence
    # start again
    if (StepCounter>=StepCount):
      StepCounter = 0
      runs = runs + 1
      print runs
    if (StepCounter<0):
      StepCounter = StepCount+StepDir
   
    # Wait before moving on
    time.sleep(WaitTime)
 
# Start main loop
try:
    curtainsOpen = False
    runs = 0
    while True:
      now = datetime.now()
      print now.hour
      if curtainsOpen == False:
          if now.hour >= 7 and now.hour <= 8:
            print "it's after 7, open the blinds"
            print "run motor"
            curtainsOpen = True
          else:
            print "not time to open yet"
      else:
        if now.hour > 15:
          print "Afternoon, close the blinds"
          print "Run motor"
          curtainsOpen = False
          
      print "long sleep"
      time.sleep(3600)
        
          
      ##motor()
      #time.sleep(361)
     
      

finally:
    print("Keyboard interrupt")
    GPIO.cleanup()
