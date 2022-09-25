from flask import Flask, request
from tasks import square

app = Flask(__name__)

@app.route('/')
def health():
    return "App is working."


@app.route('/test', methods=['POST'])
def func():
    input = request.get_json()["input"]
    output = input**2
    return {"output": output}


@app.route("/square", methods=["POST"])
def call_square():
    input = request.get_json()["input"]
    for i in range(input):
        async_results = square.delay(i)
    return {"output": async_results.id}


if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")
