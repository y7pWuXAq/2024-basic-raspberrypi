# LED에 1234 띄우기

import RPi.GPIO as GPIO
import time

segPins = [24, 5, 6, 12, 13, 16, 17]
COM = [20, 21, 22, 23]
GPIO.setmode(GPIO.BCM)

for pin in segPins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, True)

for com in COM:
	GPIO.setup(com, GPIO.OUT)

seqs = [
    [0, 1, 1, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 1, 0, 1],  # 2
    [1, 1, 1, 1, 0, 0, 1],  # 3
    [0, 1, 1, 0, 0, 1, 1],  # 4
]

try:
	while True:
			for com, seq in zip(COM, seqs):
				for reset in COM:
					GPIO.output(reset,  False)
				GPIO.output(com, True)
				for i in range(0, 7):
					GPIO.output(segPins[i], seq[i])
				time.sleep(0.001)

except KeyboardInterrupt:
	GPIO.cleanup()