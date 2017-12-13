from flask import Flask, request, jsonify, render_template
import os
import pymongo
import binascii
import json

client = pymongo.MongoClient("localhost", 27017)
db = client.flask_auth

app = Flask(__name__)


@app.route('/register', methods=["GET", "POST"])
def register():
    param = json.loads(request.get_data())

    if param:
        token = binascii.hexlify(os.urandom(16))
        db.users.insert({"username": param["username"], "token": token})
        return jsonify({"token": token})
    else :
        return jsonify({"message" : "Please provide the username."})


@app.route('/unprotected', methods=["GET", "POST"])
def unprotected():
    return jsonify({"message" : "Anyone can view this."})


@app.route('/protected', methods=["GET", "POST"])
def protected():
    if request.args.get("token"):
        token = request.args.get("token")
        if db.users.find_one({"token" : token}):
            return jsonify({"message" : "Valid token. Only valid users can view this"})
        else:
            return jsonify({"message" : "Please supply a valid token, this token cannot be found."})
    else:
        return jsonify({"message" : "Please supply a token."})


if __name__ == "__main__":
    app.run(debug=True)
