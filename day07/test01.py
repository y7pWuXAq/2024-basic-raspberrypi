import RPi.GPIO as GPIO
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("./test01.ui")[0]

LED_RED = 4
LED_BLUE = 5
LED_GREEN = 6


class WindowClass(QMainWindow, form_class) :
	def __init__(self) :
		super().__init__()
		self.setupUi(self)

		# 버튼 클릭 이벤트 연결
		self.Btn_ON.clicked.connect(self.btnOnFunction)
		self.Btn_OFF.clicked.connect(self.btnOffFunction)

		self.Btn_RED.clicked.connect(self.btnRedFunction)
		self.Btn_BLUE.clicked.connect(self.btnBlueFunction)
		self.Btn_GREEN.clicked.connect(self.btnGreenFunction)
		self.Btn_WHITE.clicked.connect(self.btnWhiteFunction)

		# GPIO 초기화 설정
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(LED_RED, GPIO.OUT)
		GPIO.setup(LED_BLUE, GPIO.OUT)
		GPIO.setup(LED_GREEN, GPIO.OUT)

	# 버튼 이벤트 함수
	def btnOnFunction(self) :
		print("LED ON CLICK!!")

	def btnOffFunction(self) :
		GPIO.output(LED_RED, True)
		GPIO.output(LED_BLUE, True)
		GPIO.output(LED_GREEN, True)
		GPIO.cleanup()
		print("LED OFF CLICK!!")

	def btnRedFunction(self) :
		GPIO.output(LED_RED, False)
		GPIO.output(LED_BLUE, True)
		GPIO.output(LED_GREEN, True)
		print("LED RED CLICK!!")

	def btnBlueFunction(self) :
		GPIO.output(LED_RED, True)
		GPIO.output(LED_BLUE, False)
		GPIO.output(LED_GREEN, True)
		print("LED BLUE CLICK!!")

	def btnGreenFunction(self) :
		GPIO.output(LED_RED, True)
		GPIO.output(LED_BLUE, True)
		GPIO.output(LED_GREEN, False)
		print("LED GREEN CLICK!!")

	def btnWhiteFunction(self) :
		GPIO.output(LED_RED, False)
		GPIO.output(LED_BLUE, False)
		GPIO.output(LED_GREEN, False)
		print("LED WHITE CLICK!!")


# 메인함수
if __name__ == "__main__" :
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()
