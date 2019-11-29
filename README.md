# flask-mongodb-rest-api

## Server code

Configure mongoDb and get the server running on localhost:27017

Setup python3 along with pip3

To install dependencies:
```shell
	sudo pip3 install flask
	sudo pip3 install pymongo
```

Run the command: ```python3 server.py```

The server will run on localhost:5000

The device data can be pushed on the server using POST request on http://localhost:5000/post_data

The device data can be retrieved from the server using GET request on http://localhost:5000/get_data

