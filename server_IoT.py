import sys

from flask import Flask, request
import json
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)

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
        print(str(request.json).replace("'", '"'), file=sys.stderr)
        data = json.loads(str(request.json).replace("'", '"'))
        ret_str = "{"
        for k in data:
            ret_str += '"' + k + '":"' + data[k] + '",'
            # print(k, data[k])
            print(k + ": " + data[k], file=sys.stderr)
        ret_str = ret_str[:-1]
        ret_str += "}"
        return ret_str


if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0', port=6000)
