import RPi.GPIO as GPIO
import time

relayPin = 25 # Spin
red = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)

try :
	while True :
		GPIO.output(relayPin, 1) # 릴레이 켜기
		GPIO.output(red, 0)
		time.sleep(1) # 1초 대기
		GPIO.output(relayPin, 0) # 릴레이 끄기
		GPIO.output(red, 0)
		time.sleep(1)

except KeyboardInterrupt :
	GPIO.cleanup()
