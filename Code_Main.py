from flask import Flask,request,render_template

app = Flask(__name__)

# @ denotes a decorator
@app.route('/')
def index():
    return "Hello World";

# For strings
@app.route('/profile/<username>')
def display_name(username):
    return "<h1>Welcome " + username + "</h1>"

# For integers
@app.route('/post/<int:id>')
def display_ID(id):
    return "ID is : " + str(id)

# HTTP Methods
@app.route('/http', methods=['GET', 'POST'])
def http_method():
    if request.method == 'POST':
        return "It was a POST Request"
    else :
        return "It was a GET Request"

if __name__ == "__main__":
    app.run()

