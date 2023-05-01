from flask import Flask, request, jsonify
import os
from src.insert_query_DB import insert_user, query_user, query_answer, insert_answer

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


@app.route("/answers", methods=["GET", "POST"])
# I suspect this will need to be altered to take a ID parameter so we know whose answers we're checking - Kieran
def get_answers():
    if request.method == "GET":

        data = request.get_json()
        user_id = data.get("user_id")

        ##
        # answers = query_answer(user_id) #call currently doesn't work for this
        answers = {"q": "a"}  # dummy
        ##

        return jsonify(answers)

    if request.method == "POST":
        # Fetch answer_id to check
        data = request.get_json()
        user_id = data.get("user_id")
        question_id = data.get("question_id")
        answer = data.get("answer")

        ##
        result = query_answer(
            user_id
        )  # will won't to call it with the user_id, which query_answer does not currently have
        ##

        if result == {}:
            insert_answer(question_id, user_id, answer)
        else:
            return jsonify(result)


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
