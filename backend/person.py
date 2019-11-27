from flask import Flask
from flask import request
import mysql.connector

app = Flask (__name__)

def connect ():
	return mysql.connector.connect (
		host="database",
		user="root",
		password="mysql",
		database="opn"
	)

@app.route ("/persons", methods = ['GET'])
def select ():
	try:
		cn = connect ()
		cursor = cn.cursor ().execute ("SELECT * FROM persons")
		result = cusor.fetchall ()

		array = []
		for (Firstname, Lastname) in result:
			array.append ('\"firstname\": \"' + Firstname + '\", ' + '\"lastname\": \"' + Lastname + '\"')
		seperator = ", "
		seperator.join (array)
		json = '[' + array + ']'
		cn.close ()
		return json
	except:
		return "[]"

@app.route ("/person", methods = ['POST'])
def insert ():
	try:
		firstname = request.form.get('firstname')
		lastname = request.form.get('lastname')
		cn = connect ()
		cursor = cn.cursor().execute ("INSERT INTO persons VALUES (" + firstname + ", " + lastname + ")")
		return "Person succesfully entered into database."
	except:
		return "Failed to connect to database."

if (__name__ == '__main__'):
	app.run (host='0.0.0.0')
