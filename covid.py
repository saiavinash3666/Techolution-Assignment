from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    res = requests.get('https://api.covid19api.com/summary')
    case = res.json()
    return render_template("index.html",cases=case)

if __name__ == '__main__':
    app.run()
