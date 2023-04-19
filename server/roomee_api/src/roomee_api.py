from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


# Method to return every user to the endpoint /api/users
@app.route("/users", methods=["GET"])
def get_users():
    # Mock list of user ids
    user_ids = []

    return jsonify({"user_ids": user_ids})


# Method to return a boolean to the endpoint /api/users if user_id exists
@app.route("/users", methods=["POST"])
def check_user_exists():
    # Fetch user_id to check from response
    data = request.get_json()
    user_id = data["user_id"]

    # Mock list of user ids
    user_ids = [37, 43, 1009]

    if user_id in user_ids:
        return jsonify({"user_exists": True})
    else:
        return jsonify({"user_exists": False})
    
@app.route("/answers", methods=["GET"])
def get_answers():
    # Mock list of user answers
    answer_ids = []

    return jsonify({"answer_ids": answer_ids})

@app.route("/answers", methods=["POST"])
def check_answers_exist():
    # Fetch answer_id to check
    data = request.get_json()
    answer_id = data["answer_id"]

    # Mock list of answer ids
    answer_ids = [27, 8, 90]

    if answer_id in answer_ids:
        return jsonify({"answer_exists": True})
    else:
        return jsonify({"answer_exists": False})

#Check if user data is complete
@app.route("/user_is_complete/<username>", methods=['GET'])
def user_is_complete(username):
    #Mock user
    user={'Joe':{'questions':[]}}
    if username in user:
        completed = bool(users[username]['questions'])
        return jsonify({'is_completed': completed})
    else:
        return jsonify({'error': 'User not found'})

