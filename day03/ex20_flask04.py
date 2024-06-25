from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def get():
	value1 = request.args.get("이름", "user") # 주소창 뒤에 /?이름=ㅁㅁㅁ&주소=부산 형태로 작성
	value2 = request.args.get("주소", "부산") # 키&value&키=value
	return value1 + ":" + value2

if __name__ == "__main__" :
	app.run(host="0.0.0.0", port="10011", debug=True)
