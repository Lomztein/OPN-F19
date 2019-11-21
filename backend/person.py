from flask import Flask
import mysql.connector

app = Flask (__name__)

if (__name__ == '__main__'):
	app.run ()

def connect ():
	return mysql.connector.connect (
		host="database",
		user="root",
		password="mysql",
		database="opn"
	)

@app.route ("/person", methods = ['GET'])
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
def insert (firstname, lastname):
	try:
		cn = connect ()
		cursor = cn.cursor().execute ("INSERT INTO persons VALUES (" + firstname + ", " + lastname + ")")
		return "Person succesfully entered into database."
	except:
		return "Failed to connect to database."
