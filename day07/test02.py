import RPi.GPIO as GPIO
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
import time

form_class = uic.loadUiType("./test02.ui")[0]

LED_RED = 4
LED_BLUE = 5
LED_GREEN = 6

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 버튼 클릭 이벤트 연결
        self.Btn_ON.clicked.connect(self.btnOnFunction)
        self.Btn_OFF.clicked.connect(self.btnOffFunction)
        self.Btn_Quit.clicked.connect(self.btnQuitFunction)

        # 체크박스 상태 변경 시그널 연결
        self.Chk_RED.stateChanged.connect(self.chkRedFunction)
        self.Chk_BLUE.stateChanged.connect(self.chkBlueFunction)
        self.Chk_GREEN.stateChanged.connect(self.chkGreenFunction)

        # GPIO 초기화
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_RED, GPIO.OUT)
        GPIO.setup(LED_BLUE, GPIO.OUT)
        GPIO.setup(LED_GREEN, GPIO.OUT)

	# 이벤트 함수 정리
    def btnOnFunction(self):
        self.lineEdit.setText("LED ON")
        GPIO.output(LED_RED, False)
        GPIO.output(LED_BLUE, False)
        GPIO.output(LED_GREEN, False)
        time.sleep(0.5)
        GPIO.output(LED_RED, True)
        GPIO.output(LED_BLUE, True)
        GPIO.output(LED_GREEN, True)
        print("LED ON CLICK!!")

    def btnOffFunction(self):
        GPIO.output(LED_RED, True)
        GPIO.output(LED_BLUE, True)
        GPIO.output(LED_GREEN, True)
        print("LED OFF CLICK!!")

    def btnQuitFunction(self):
        GPIO.cleanup()
        print("Quit CLICK!!")
        QApplication.instance().quit()

    def chkRedFunction(self, state):
        if state == Qt.Checked:
            GPIO.output(LED_RED, False)
        else:
            GPIO.output(LED_RED, True)

    def chkBlueFunction(self, state):
        if state == Qt.Checked:
            GPIO.output(LED_BLUE, False)
        else:
            GPIO.output(LED_BLUE, True)

    def chkGreenFunction(self, state):
        if state == Qt.Checked:
            GPIO.output(LED_GREEN, False)
        else:
            GPIO.output(LED_GREEN, True)


# 메인함수
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())
