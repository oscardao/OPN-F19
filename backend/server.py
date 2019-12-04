from flask import Flask, jsonify, request
import json
import mysql.connector

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'takehome'

def connect():
	return mysql.connector.connect(host='thdatabase', database='takehome',user='root')

@app.route('/')
def index():
	return 'Me name Oscab'

@app.route('/persons/', methods=['GET'])
def getPersons():
	connection = connect()
	statement = "SELECT * FROM Person"
	
	cur = connection.cursor()
	cur.execute(statement)

	rowz = cur.fetchall()
	rowAway = []
	
	for r in rowz:
		row = (row.PersonID, row.Firstname, row.Lastname)
		rowAway.append(row)
	
	
	data = json.dumps(rowAway)
	jsonData = jsonify(data)
	return jsonData

@app.route('/person/', methods=['POST'])
def addPerson():
	connection = connect()
	statement = "INSERT INTO Person (Firstname, Lastname) VALUES (%s, %s)"
	val = (requrest.form['firstname'], request.form['lastname'])
	connect.cursor().execute(statement, val)
	connect.commit()

if __name__ == '__main__':
    app.run()

