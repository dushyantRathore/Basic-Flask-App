from flask import Flask,request,render_template,jsonify
import sqlite3 as sql

app = Flask(__name__)

# Webpage containing the Registration Form
@app.route('/new')
def new_user():
    return render_template("registration.html")

# Add new Data to the Table in the Database
@app.route('/addnew', methods=['POST', 'GET'])
def addnew():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']

        print name
        print email
        print age

        with sql.connect("college.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO student(name, email, age) VALUES(?,?,?)",(name,email,age,))

            con.commit()
            msg = "Record successfully added"

        return render_template("result.html", msg=msg)
        con.close()

# List out the data from the Table in the Database
@app.route('/list')
def list():
    con = sql.connect("college.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from student")

    rows = cur.fetchall()

    return render_template("list.html", rows=rows)

if __name__ == "__main__":
    app.run(debug=True)

