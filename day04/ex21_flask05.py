# 동일한 폴더 위치에 templates 폴더를 만들고 거기에 html 파일 생성 후 실행

from flask import Flask, request, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

blue_led = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(blue_led, GPIO.OUT)
GPIO.cleanup()

@app.route('/')
def home() :
	return render_template("index.html")

@app.route('/data', methods = ['POST'])
def data() :
	data = request.form['led']

	if(data == 'on'):
		GPIO.output(blue_led, 0)
		return home()

	elif(data == 'off'):
		GPIO.output(blue_led, 1)
		return home()

if __name__ == '__main__' :
	app.run(host='0.0.0.0', port='81', debug=True)
