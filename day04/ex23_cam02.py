from picamera2 import Picamera2
import RPi.GPIO as GPIO
import time

swPin = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin, GPIO.IN)

try :
	while True :
		if GPIO.input(swPin) == True :
			print("CLICK!")
			time.sleep(0.3)

except KeyboardInterrupt :
	GPIO.cleanup()
