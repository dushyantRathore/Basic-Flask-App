from flask import Flask, render_template

app = Flask(__name__)

#  Mapping Multiple URLs
@app.route("/profile/")
@app.route("/profile/<user>")
def index(user=None):
    return render_template("user.html", user=user)


if __name__ == "__main__":
    app.run()