from flask import Flask, request, jsonify
import os
from src.insert_query_DB import mySQL

app = Flask(__name__)


# method to return user from the insert_query_DB.py file
# note that this does not check if the user has been created.
def get_user(email):
    is_valid(email)
    db_conn = mySQL()
    user = db_conn.query_user_by_email(email)
    return user


# method to return all answers from the insert_query_DB.py file
# note that this does not check if the user has completed the quiz.
def get_answers(id):
    db_conn = mySQL()
    answers = db_conn.query_answer_by_id(
        id
    )  ##CHANGE WHEN RILEY CHANGES THE FUNCTION, We wish to have all answers from this call

    return answers


def is_valid(dirty_string):
    if not type(dirty_string) is str or " " in dirty_string:
        return False

    else:
        return True


@app.route("/answers", methods=["GET", "POST"])
# I suspect this will need to be altered to take a ID parameter so we know whose answers we're checking - Kieran
def get_answers():
    db_conn = mySQL()
    if request.method == "GET":
        # Fetch stuff from call
        data = request.get_json()
        user_id = data.get("user_id")

        answers = db_conn.query_answer(user_id)

        return jsonify(answers)

    if request.method == "POST":
        # Fetch stuff from call
        data = request.get_json()
        user_id = data.get("user_id")
        question_ids = data.get("question_id")  # list
        answers = data.get("answers")  # list

        for i in question_ids:
            db_conn.insert_answer(i, user_id, answers[i])

        return jsonify("Answers successfully posted"), 201


# Method to return all questions to an endpoint /api/questions
# @app.route("/questions", methods=["GET"])
# def get_questions():
#     question_ids = []
#     return jsonify({"question_ids": question_ids})


# Method to check if a user exists and create them if they don't
@app.route("/user/<email>", methods=["PUT"])
def user_creation(email):
    db_conn = mySQL()
    if request.method == "PUT":
        user = get_user(email)

        if user == {}:
            # user doesn't exist
            # create entry for user
            db_conn.insert_user(email, "")

            return jsonify({"message": "User created."}), 200

        else:
            # user already exists
            return jsonify({"message": "User exists"}), 204


# Login endpint:
# I am assuming to data will look something like this:
# users = {'email': 'password'}


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    # Is this what you mean by sanitize? I am removing any leading/trailing whitespace
    if is_valid(email) and is_valid(password):
        user = get_user(email)

        if not user == {} and user["password"] == password:
            return jsonify({"message": "Login successful."}), 200
        else:
            return jsonify({"message": "Invalid email or password."}), 403

    else:
        return jsonify({"message": "Invalid email or password format"}), 400


# register endpoint to take in and save email and password
@app.route("/register", methods=["POST"])
def register_user():
    db_conn = mySQL()
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    # sanitize data
    if is_valid(email) and is_valid(password):
        db_conn.insert_user(email, password)

        return jsonify({"User created"}), 200

    else:
        return jsonify({"message": "Invalid email or password format"}), 400
