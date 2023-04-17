from flask import Flask, request, jsonify, g
import sqlite3
import os

app = Flask(__name__)

DATABASE = 'roomee.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db

@app.teardown_appcontext
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route('/users', methods=['GET'])
def get_users():
    db = get_db()
    cur = db.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    cur.close()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    gender = data.get('gender')

    # Insert the user data into the database
    db = get_db()
    cur = db.cursor()
    query = '''
    INSERT INTO users (first_name, last_name, gender)
    VALUES (?, ?, ?)
    '''
    cur.execute(query, (first_name, last_name, gender))
    db.commit()
    cur.close()

    # Return a success message or the created user object
    return jsonify({'message': 'User created successfully'}), 201

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"