from flask import Flask,render_template,request

app = Flask(__name__)

# Home Page
@app.route('/exam')
def index():
    return render_template("marks.html")


# Marks input
@app.route('/check', methods=['POST', 'GET'])
def check():
    if request.method == 'POST':
        marks = int(request.form['marks'])
        print marks

        return render_template("status.html", marks=marks)  # Transfer Control


if __name__ == "__main__":
    app.run()