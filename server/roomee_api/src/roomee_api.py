from flask import Flask, request, jsonify
import os
from src.insert_query_DB import insert_user, query_user, query_answer

app = Flask(__name__)


# method to return user from the insert_query_DB.py file
# note that this does not check if the user has been created.
def get_user(username):
    is_valid(username)
    user = query_user(username)
    return user


# method to return all answers from the insert_query_DB.py file
# note that this does not check if the user has completed the quiz.
def get_answers(id):
    answers = query_answer(
        id
    )  ##CHANGE WHEN RILEY CHANGES THE FUNCTION, We wish to have all answers from this call

    return answers


def is_valid(dirty_string):
    if not type(dirty_string) is str or " " in dirty_string:
        return False

    else:
        return True


# Method to return a boolean to the endpoint /api/users if user_id exists


@app.route("/answers/<username>", methods=["GET", "POST"])
# I suspect this will need to be altered to take a username parameter so we know whose answers we're checking - Kieran
def get_answers(username):
    if request.method == "GET":
        # Mock list of user answers
        answer_ids = []

        return jsonify({"answer_ids": answer_ids})

    if request.method == "POST":
        # Fetch answer_id to check
        data = request.get_json()
        answer_id = data["answer_id"]

        # Mock list of answer ids
        answer_ids = [27, 8, 90]

        if answer_id in answer_ids:
            return jsonify({"answer_exists": True})
        else:
            return jsonify({"answer_exists": False})


# Method to return all questions to an endpoint /api/questions
@app.route("/questions", methods=["GET"])
def get_questions():
    question_ids = []
    return jsonify({"question_ids": question_ids})


# Method to check if a user exists and create them if they don't
@app.route("/user/<username>", methods=["PUT"])
def user_creation(username):
    if request.method == "PUT":
        user = get_user(username)

        if user == {}:
            # user doesn't exist
            # create entry for user
            insert_user(username, "")

            return jsonify({"message": "User created."}), 200

        else:
            # user already exists
            return jsonify({"message": "User exists"}), 204


# Login endpint:
# I am assuming to data will look something like this:
# users = {'username': 'password'}


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Is this what you mean by sanitize? I am removing any leading/trailing whitespace
    if is_valid(username) and is_valid(password):
        user = get_user(username)

        if not user == {} and user["password"] == password:
            return jsonify({"message": "Login successful."}), 200
        else:
            return jsonify({"message": "Invalid username or password."}), 403

    else:
        return jsonify({"message": "Invalid username or password format"}), 400


# register endpoint to take in and save username and password
@app.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # sanitize data
    if is_valid(username) and is_valid(password):
        insert_user(username, password)

        return jsonify({"User created"}), 200

    else:
        return jsonify({"message": "Invalid username or password format"}), 400
