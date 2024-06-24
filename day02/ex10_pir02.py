# pir

import RPi.GPIO as GPIO
import time

priPin = 24
red = 4
blue = 5
green = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(priPin, GPIO.IN)

GPIO.output(red, True)
GPIO.output(green, True)
GPIO.output(blue, True)

try :
	while True :
		if GPIO.input(priPin) == True :
			print("Detected")
			GPIO.output(red, False)
			GPIO.output(green, False)
			GPIO.output(blue, False)
			time.sleep(1)
		else:
			GPIO.output(red, True)
			GPIO.output(green, True)
			GPIO.output(blue, True)
except KeyboardInterrupt :
	GPIO.cleanup()
