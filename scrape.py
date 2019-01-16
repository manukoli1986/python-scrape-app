from flask import Flask
import requests
import json
import time
import random

app = Flask(__name__)
start_time = time.clock()

@app.route("/")
def hello():
    r = requests.get('http://dojodevopschallenge.s3-website-eu-west-1.amazonaws.com/fortune_of_the_day.json')

    r = json.loads(r.text)
    selindex = random.randint(0, len(r) - 1)
    return "<h1>"+str(r[ selindex ]['message'])+"</h1>"

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=8080, debug=True)
