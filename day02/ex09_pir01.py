# pir

import RPi.GPIO as GPIO
import time

priPin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(priPin, GPIO.IN)

try :
    while True :
        if GPIO.input(priPin) == True :
            print("Detected")
            time.sleep(0.5)
except KeyboardInterrupt :
    GPIO.cleanup()