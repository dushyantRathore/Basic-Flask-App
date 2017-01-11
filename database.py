from flask import Flask
import sqlite3

conn = sqlite3.connect('college.db')
print "Opened Database Successfully"

conn.execute('CREATE TABLE student(name TEXT, email TEXT, age INT)')
print "Table created successfully"

conn.close()

