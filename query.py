from flask import Flask,render_template,request
import sqlite3 as sql
import string

app = Flask(__name__)

@app.route('/search')
def search():
    return render_template("search.html")


@app.route('/query', methods=['POST', 'GET'])
def query():
    if request.method == "POST":
        name = request.form["name"]

        con = sql.connect("college.db")
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM student WHERE name = ?", (name,))

        rows = cur.fetchall()

        return render_template("list.html", rows=rows)

if __name__ == "__main__":
    app.run(debug=True)