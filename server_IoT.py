from flask import Flask, request
import json
import logging

# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)

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
        ret_str = "{"
        for k in data:
            ret_str += '"' + k + '":"' + data[k] + '",'
            print(k, data[k])
        ret_str = ret_str[:-1]
        ret_str += "}"
        return ret_str


if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0', port=6000)



