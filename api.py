from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/<num>")
def low_or_high(num):
	number = int(num)
	result = 'equal'
	if number < 100:
		result = "low"
	elif number > 100:
		result = 'high'
    
	return jsonify(
        value=result
    )
