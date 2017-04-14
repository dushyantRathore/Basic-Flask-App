from flask import Flask
import sqlite3

conn = sqlite3.connect('college.db')  # Database Connection
print "Opened Database Successfully"

conn.execute('CREATE TABLE student(name TEXT, email TEXT, age INT)')  # Create a table in the database
print "Table created successfully"

conn.close()

