# 주소창 안에서 변수 <> 사용하기

import RPi.GPIO as GPIO
from flask import Flask
led = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

GPIO.output(led, True)

app = Flask(__name__)

@app.route("/")
def hello():
	return "LED Control Web page"

@app.route("/led/<state>")
def fun(state):
	if state == "on":
		GPIO.output(led, False)
		return "<h1>LED ON</h1>"
	elif state == "off":
		GPIO.output(led, True)
		return "<h1>LED OFF</h1>"
	elif state == "clear":
		GPIO.cleanup()
if __name__ == "__main__":
	app.run(host="0.0.0.0", port="10111", debug=True)