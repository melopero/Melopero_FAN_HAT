#!/usr/bin/env python3
import os
import time
import RPi.GPIO as GPIO
    

minimum_always_ON=True
minimum_speed=30
target_temp=52
DEBUG=False
current_speed=0



def getCPUtemperature():
    global current_speed
    res = os.popen('vcgencmd measure_temp').readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    if(DEBUG):
        print("temp is {0}, current speed: {1}".format(temp,current_speed)) #Uncomment here for testing
    return temp

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    myPWM=GPIO.PWM(18,50)
    myPWM.start(minimum_speed)
    current_speed=minimum_speed
    while True:
        temp = float(getCPUtemperature())
        if(temp<target_temp and not minimum_always_ON):
            myPWM.ChangeDutyCycle(0)
            current_speed=0
            time.sleep(1)
            continue
        if(temp<target_temp and minimum_always_ON):
            myPWM.ChangeDutyCycle(minimum_speed)
            current_speed=minimum_speed
            time.sleep(1)
            continue
        
        if(temp>target_temp and temp<56):
            myPWM.ChangeDutyCycle(40)
            current_speed=40
            time.sleep(1)
            continue
        if(temp>56 and temp<60):
            myPWM.ChangeDutyCycle(50)
            time.sleep(1)
            continue
        if(temp>60 and temp<65):
            myPWM.ChangeDutyCycle(60)
            current_speed=60
            time.sleep(1)
            continue
        if(temp>65 and temp<70):
            myPWM.ChangeDutyCycle(70)
            current_speed=70
            time.sleep(1)
            continue
        if(temp>70 and temp<74):
            myPWM.ChangeDutyCycle(80)
            current_speed=80
            time.sleep(1)
            continue
        if(temp>74 and temp<76):
            myPWM.ChangeDutyCycle(90)
            current_speed=90
            time.sleep(1)
            continue
        if(temp>76):
           #handleFan(100)
            myPWM.ChangeDutyCycle(100)
            current_speed=100
            time.sleep(1)
            continue
            
        
        

except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt 
    GPIO.cleanup() # resets all GPIO ports used by this program
