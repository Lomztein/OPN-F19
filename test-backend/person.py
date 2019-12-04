from flask import Flask
import mysql.connector

app = Flask (__name__)

@app.route ("/person", methods = ['GET'])
def select ():
	return "Epstein didn't kill himself."

if (__name__ == '__main__'):
	app.run (host='0.0.0.0')
