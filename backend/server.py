from flask import Flask, jsonify, request
import json
import mysql.connector

app = Flask(__name__)

class Person:
	def __init__(self, Firstname, Lastname, PersonID):
		self.Firstname = Firstname
		self.Lastname = Lastname
		self.PersonID = PersonID

def connect():
	return mysql.connector.connect(host='database', database='takehome',user='root')

@app.route('/persons/')
def getPersons():
	connection = connect()

	cur = connection.cursor()
	cur.execute("SELECT * FROM Person")

	rows = cur.fetchall()

	personArray = []
	personDictionary = {}

	for r in rows:
		personDictionary = {'Firstname': r[1], 'PersonID': r[0], 'Lastname': r[2]}
		personArray.append(personDictionary)
		personDictionary = {}

	return jsonify(personArray)

@app.route('/person', methods=['POST'])
def addPerson():
	connection = connect()
	statement = "INSERT INTO Person (Firstname, Lastname) VALUES (%s, %s)"
	val = (request.form['firstname'], request.form['lastname'])
	connection.cursor().execute(statement, val)
	connection.commit()
	return "Don't add anything more please"

if __name__ == '__main__':
    app.run()
