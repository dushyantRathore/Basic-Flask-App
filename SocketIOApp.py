from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)

app.config["SECRET_KEY"] = "secretkey"
socketio = SocketIO(app)


@socketio.on("message") # Handle an event on a message
def handle_message(msg):
    print "Message : "  +msg
    send(msg, broadcast=True)


@app.route("/")
def index():
    return render_template("ChatIndex.html")

if __name__ == "__main__":
    socketio.run(app)
