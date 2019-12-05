from flask import Flask, jsonify, request
import json
import mysql.connector

app = Flask(__name__)

class Person:
	def __init__(self, firstname, lastname, id):
		self.firstname = firstname
		self.lastname = lastname
		self.id = id

def connect():
	return mysql.connector.connect(host='database', database='takehome',user='root')

@app.route('/persons', methods=['GET'])
def getPersons():
	connection = connect()
	statement = "SELECT * FROM Person"

	cur = connection.cursor()
	cur.execute(statement)

	rowz = cur.fetchall()
	rowArray = []

	for r in rowz:
		row = (r[0], r[1], r[2])
		rowArray.append(row)

	data = json.dumps(rowArray)
	jsonData = jsonify(data)
	return jsonData

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
