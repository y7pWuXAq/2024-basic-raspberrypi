import RPi.GPIO as GPIO
import time

# RGB LED Pinnumber setting
red_pin = 4
blue_pin = 5
green_pin = 6

GPIO.setmode(GPIO.BCM)  # GPIO.BOARD(1~40)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

try:
    while(True):
        GPIO.output(red_pin, False)
        GPIO.output(green_pin, True)
        GPIO.output(blue_pin, True)
        time.sleep(1)

        GPIO.output(red_pin, True)
        GPIO.output(green_pin, True)
        GPIO.output(blue_pin, False)
        time.sleep(1)

        GPIO.output(red_pin, True)
        GPIO.output(green_pin, False)
        GPIO.output(blue_pin, True)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

