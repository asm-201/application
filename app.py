# app.py
# main run
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world. First run. change to dynamism!\n'


if __name__ == '__main__':
    app.run(debug=True)
