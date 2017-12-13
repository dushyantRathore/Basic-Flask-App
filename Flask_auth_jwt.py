from flask import Flask, jsonify, make_response, request
import jwt
import datetime
from functools import wraps
import json

app = Flask(__name__)

app.config["SECRET_KEY"] = "secretkey"


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get("token")

        print "Token : " + str(token)

        if not token:
            return jsonify({"message": "Token is missing"})

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])
            print "Data : " + str(data)

        except:
            return jsonify({"message": "Token is invalid"})

        return f(*args, **kwargs)

    return decorated


@app.route('/unprotected', methods=["GET", "POST"])
def unprotected():
    return jsonify({"message": "Anybody can view this"})


@app.route('/protected', methods=["GET", "POST"])
@token_required
def protected():
    return jsonify({"message": "This is only visible to people with valid tokens"})


@app.route('/login', methods=["GET", "POST"])
def login():
    param = json.loads(request.get_data())

    if param and param["password"] == "12345678":
        token = jwt.encode({"user": param["username"], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=20)}, app.config["SECRET_KEY"])
        return jsonify({"token": token})
    else :
        return jsonify({"message": "Could not verify"})


if __name__ == "__main__":
    app.run(debug=True)