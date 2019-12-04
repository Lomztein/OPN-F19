from flask import Flask, request, jsonify
import mysql.connector
import json

app = Flask (__name__)

def connect ():
	return mysql.connector.connect (
		host='database',
		user='root',
		passwd='',
		database='opn'
	)

@app.route ("/persons", methods = ['GET'])
def select ():
	try:
		cn = connect ()
		cursor = cn.cursor ()
		cursor.execute ("SELECT * FROM persons")
		result = cursor.fetchall ()
		cn.close ()

		persons = []
		for PersonID, Firstname, Lastname in result:
			person = {
				'PersonID': PersonID,
				'Firstname': Firstname,
				'Lastname': Lastname
			}
			persons.append(person)

		return jsonify(persons)
	except Exception as exc:
		return str(exc)

@app.route ("/person", methods = ['POST'])
def insert ():
	try:
		firstname = request.form.get('firstname')
		lastname = request.form.get('lastname')
		cn = connect ()
		cursor = cn.cursor().execute ("INSERT INTO persons (Firstname, Lastname) VALUES (\'" + firstname + "\', \'" + lastname + " \')")
		cn.commit ()
		cn.close ()
		return "Person succesfully entered into database."
	except Exception as exc:
		return str(exc)

if (__name__ == '__main__'):
	app.run (host='0.0.0.0')
