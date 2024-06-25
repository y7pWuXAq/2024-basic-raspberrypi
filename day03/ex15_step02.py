## ex14_step01.py 반복문으로 수정
 
import RPi.GPIO as GPIO
import time

steps = [21, 22, 23, 24]

GPIO.setmode(GPIO.BCM)

i = 3
for stepPin in steps:
	GPIO.setup(stepPin, GPIO.OUT)
	GPIO.output(stepPin, 0)

res = [[0,0,0,1], [0,0,1,1], [0,0,1,0], [0,1,1,0], [0,1,0,0], [1,1,0,0], [1,0,0,0], [1,0,0,1]]

try:
	while 1:
		for ires in res :
			for num in range(0,4) :
				GPIO.output(steps[num], ires[num])
			time.sleep(0.1)

except KeyboardInterrupt:
	GPIO.cleanup()