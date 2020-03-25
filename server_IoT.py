from flask import Flask, request
import json
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/get_data', methods=['GET'])
def get_data():
    if request.method == 'GET':
        return_string = ''
        return return_string


@app.route('/post_data', methods=['POST'])
def post_data():
    if request.method == 'POST':
        data = dict(request.form)
        for k in data:
            print(k, data[k])
        return "200"


if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0')


