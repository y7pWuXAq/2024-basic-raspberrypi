# 복습
import RPi.GPIO as GPIO
import time

# 0~9 까지 1byte hex값
fndDatas = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x27, 0x7f, 0x6f]
fndSegs = [4, 5, 6, 24, 26, 26, 13] # a ~ f pin
fndSels = [20, 21, 22, 23] # fnd 선택 pin

# GPIO 설정
GPIO.setmode(GPIO.BCM)
for fndSeg in fndSegs:
	GPIO.setup(fndSeg, GPIO.OUT)
	GPIO.output(fndSeg, 0)

for fndSel in fndSels:
	GPIO.setup(fndSel, GPIO.OUT)
	GPIO.output(fndSel, 1)

def fndOut(data, sel): # LED 화면에 띄울 숫자형태를 만드는 함수
	for i in range(0, 7):
		GPIO.output(fndSegs[i], fndDatas[data] & (0x01 << i)) # 화살표 방향으로 i 만큼 이동
		# i = 1 : 0000 0001 -> 0000 0010
		for j in range(0, 4) : # 표시 할 자릿수의 fnd 선택
			if j == sel :
				GPIO.output(fndSels[j], 0)
			else :
				GPIO.output(fndSels[j], 1)

count = 0

try:
	while True:
		count += 1
		d1000 = (count / 1000) % 10
		d100 = (count / 100) % 10
		d10 = (count / 10) % 10
		d1 = count % 10
		d = [d1, d10, d100, d1000]

		for i in range(3, -1, -1):
			fndOut(int(d[i]), i) # 자리수와 값을 전달
			time.sleep(0.3)

except KeyboardInterrupt:
	GPIO.cleanup()