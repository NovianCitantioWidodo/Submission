from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        data = [{
            "user": {
                        "username": "test coding",
                        "email":"test@coding.test",
                        "encrypted_password": "123454",
                        "phone": "0182737",
                        "address": "asadssssaa",
                        "city": "aaa",
                        "country": "aaa",
                        "name": "postman",
                        "postcode": "12345"
                    }
                }]
    elif request.method == "POST":
        data = [{
            "email": "test@coding.test",
            "token": "jncjnvhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhkvhvhvhkvhvvkhvjsncj",
            "username": "test coding"
        }]
    return make_response(jsonify({'data': data}), 200)

@app.route('/signin', methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        data = [{
                    "email": "test@coding.test",
                    "password": "123456"
                }]
    elif request.method == "POST":
        data = [{
                    "email": "test@coding.test",
                    "token": "jncjnvhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhkvhvhvhkvhvvkhvjsncj",
                    "username": "test coding",
                }]
    return make_response(jsonify({'data': data}), 200)

@app.route('/shoping', methods=["UPDATE", "DELETE"])
def shoping():
    if request.method == "UPDATE":
        data = [{
                    "id": "shop_1 UPDATE"
                }]
    elif request.method == "DELETE":
        data = [{
                    "id": "shop_1 DELETE"
                }]
    return make_response(jsonify({'data': data}), 200)

if __name__ == "__main__" :
    app.run(host="0.0.0.0", port="5000")