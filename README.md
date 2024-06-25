## 2024-basic-raspberrypi
IoT 개발자 과정 라즈베리파이 학습 리포지토리



### DAY 01

- 물리적 핀번호와 프로그램 핀번호는 다르기 때문에 반드시 구분 필요

- Python GPIO 함수
    
    ```python
    # GPIO 설정함수
    
    ## 모드 설정
    GPIO.setmode(GPIO.BOARD) ## WPI 모드
    GPIO.setmode(GPIO.BCM) # BCM 모드
    
    # 입출력 형태 지정
    GPIO.setup(핀번호, GPIO.mode) ##IN/OUT
    ## channel: 핀번호
    ## mode: 입출력 설정 (IN/OUT)
    
    GPIO.cleanup() ## 핀 초기화
    
    # GPIO 출력함수
    GPIO.output(channel, state)
    ## channel: 핀번호
    ## state: HIGL/LOW or 1/0 or True/False
    
    # GPIO 입력함수
    GPIO.input(channel)
    ## channel: 핀번호
    
    # 시간 지연함수
    time.sleep(secs)
    ```

- 핀은 레지스터와 연결되어 있고,  HIGH(= Vcc, 5V) or LOW(= Gnd, 0V)의 비트 값 저장
- 전기 공급 → 전류 흐름 → 동작

- 하드웨어 설계 기본 법칙
    - 옴의 법칙(V=IR)
        - 전류(I): 전하의 흐름
        - 전압(V)
        - 저항

    - 키르히호프의 법칙
        - 전압 법칙
        - 전류 법칙

    - 플로팅 상태

    - 스위치
        - 풀업저항 (저항이 VCC 쪽에 연결)
            - 스위치를 누르지 않으면 VCC 값(= 1)이 그대로 레지스터(=입력)에 들어감

        - 풀다운 저항 (저항이 GND 쪽에 연결)
            - 스위치 off: 입력 핀에 0V(=0) (VCC의 전압이 인가되지 않음)
            - 스위치 on : VCC에서 공급되는 전압이 전항에 막혀 입력 핀에 전류가 흘러들어감 (5V)

- 스위치 클릭 마다 LED 색 변경
    - ex04_input02.py

- 키보드 입력 값(1~8)마다 8음계 소리 출력
    - ex07_pwm01.py



### DAY 02

- 파이썬 가상환경 생성 : python -m venv (--system-site-packages) env
    - --system-site-packages : 라이브러리 포함하는 옵션
- 가상환경 접속 : source ./env/bin/activate 
- 가상환경 종료 : deactivate
- 가상환경에 라즈베리파이 설치 : sudo pip install RPi.GPIO
    
    - 라즈베리파이 핀의 전류 상태 확인
    - sudo git clone https://github.com/WiringPi/WiringPi
    - cd WiringPi 에서 sudo ./build
    - gpio readall
    - Name(Pin), V(핀 상황)



### DAY 03

- 릴레이(Relay) : 라즈베리와 아두이노에서 제공하는 전력만으로 구동할 수 없는 외부기기를 컨트롤하고 싶을 때 외부 전원을 릴레이와 연결하여 조건이 만족할 때 아두이노에서 신호를 보내 컨트롤

- 코일에 전류가 흐르면 자성이 생겨 (=전자석) NO의 접점이 닫히고, NC의 접점이 열리게 된다
    - NC : Nomal Close (접점이 닫혀져있음)
    - NO : Nomal Open (접점이 열려있음)
    - COM : 공통단자

- 스탭모터(Step Motor) : 전기를 흘리면 펄스(신호)를 줬을 때 그에 맞게 동작하는 모터, 이 동작 또한 회전하는 것이 아닌 지정된 각도에 따라 움직임. 

- 스텝모터가 돌아가는 반복문 알고리즘 작성
    - ex14_step01.py

- Flask 활용 웹서버 가동
    - ex16_flask01.py / ex17_flask02.py

- 웹을 통해 LED on/off 제어하기
    - ex18_flask03.py / ex19_flask03-1.py

- get 형태로 파라미터 입력 받기
    - ex20_flask04.py



### DAY 04

- 파이썬 버전확인 : python -v
- pip 버전 확인 : pip -v

- 동일한 폴더 위치에 templates 폴더 생성 후 html 파일 만들어 생성
    - ex21_flask05.py

- 라즈베리파이에 카메라 연결하여 사진 찍고 저장하기
    - ex22_cam01.py

    ```python
    from picamera2 import Picamera2, Preview
    import time

    picam2 = Picamera2()
    camera_config = picam2.create_preview_configuration()
    picam2.configure(camera_config)
    picam2.start()
    time.sleep(2)
    picam2.capture_file("test1.jpg")
    ```

- 스위치를 연결하여 사진 찍기
    - ex23_cam02.py

- FND 4Digit 7Segment 표시하기
    - ex24_4Digit_7Segment.py