from flask import Flask, render_template

app = Flask(__name__)

@app.route('/profile/<username>')
def display(username):
    return render_template("profile.html", name = username)

if __name__ == "__main__":
    app.run()
