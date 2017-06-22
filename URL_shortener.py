from flask import Flask,request,render_template,json
import requests
from pyshorteners import Shortener

app = Flask(__name__)

API_KEY = "AIzaSyD29r2SCshKNkDsmfuwXhZmrUzkhF3eUdg"


@app.route('/')
def index():
    return render_template('URL_index.html')


@app.route('/shorten', methods=['POST', 'GET'])
def shorten():
    if request.method == 'POST':
        long_url = request.form['long_url']
        print long_url

        api_key = API_KEY
        shortener = Shortener('Google', api_key=api_key)
        short_url = shortener.short(long_url)

        print short_url

        return render_template('Shortened_URL.html', short_url = short_url)



if __name__ =="__main__":
    app.run(debug=True)