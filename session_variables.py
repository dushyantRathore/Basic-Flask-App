from flask import Flask,request,render_template,session

app = Flask(__name__)
app.secret_key = "secret key"

@app.route("/setvalue/<value>", methods=["GET", "POST"])
def setvalue(value):
    print(value)
    session["value"] = value
    return "Value set"

@app.route("/getvalue", methods=["GET", "POST"])
def getvalue():
    print(session["value"])
    return "The session variable value is : " + str(session["value"])

if __name__ == "__main__":
    app.run(debug=True)