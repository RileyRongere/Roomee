# test file

from flask import Flask, request, jsonify
import os
import json
import sys

app = Flask(__name__)

# mockedDB for FE testing


# helper functions for mockedDB
def get_next_user_id(data):
    user_ids = [
        int(key.replace("user_id", ""))
        for key in data.keys()
        if key.startswith("user_id")
    ]
    return "user_id" + str(max(user_ids) + 1)


def search_username(data, target_username):
    for user_id, user_data in data.items():
        if "username" in user_data and user_data["username"] == target_username:
            return user_id, user_data
    return {}


def mocked_user(username):
    with open("roomee.store", "r") as mocked_DB:
        fake_DB = json.load(mocked_DB)
        return search_username(fake_DB, username)


def mocked_get_answers(username):
    with open("roomee.store", "r") as mocked_DB:
        fake_DB = json.load(mocked_DB)
        print(fake_DB, file=sys.stderr)
        print("MOCK CALL", file=sys.stderr)
        print(username, file=sys.stderr)
        userSearch = search_username(fake_DB, username)
        print(userSearch, file=sys.stderr)

        return (userSearch[1])["answers"]


def mocked_get_questions():
    with open("roomee.store", "r") as mocked_DB:
        fake_DB = json.load(mocked_DB)
        return fake_DB["questions"]


def mocked_user_insert(username, password):
    with open("roomee.store", "r") as mocked_DB:
        fake_DB = json.load(mocked_DB)

        print(fake_DB, file=sys.stderr)

    # write new user
    print(get_next_user_id(fake_DB), file=sys.stderr)
    fake_DB[get_next_user_id(fake_DB)] = {
        "username": username,
        "password": password,
        "answers": [3, 3],
    }

    file_json_object = json.dumps(fake_DB)

    with open("roomee.store", "w") as mocked_DB:
        mocked_DB.write(file_json_object)


def mocked_user_update_answers(username, answers):
    with open("roomee.store", "r") as mocked_DB:
        fake_DB = json.load(mocked_DB)

    user_id, user_data = search_username(fake_DB, username)

    fake_DB[user_id]["answers"] = answers

    file_json_object = json.dumps(fake_DB)

    with open("roomee.store", "w") as mocked_DB:
        mocked_DB.write(file_json_object)


# method to return user from the insert_query_DB.py file
# note that this does not check if the user has been created.
def get_user(username):
    is_valid(username)
    user = mySQL().query_user(username)
    return user


# method to return all answers from the insert_query_DB.py file
# note that this does not check if the user has completed the quiz.
def get_answers(id):
    answers = mySQL().query_answer(
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
        # answer_ids = []

        # return jsonify({"answer_ids": answer_ids})
        print("GET ANSWERS CALL")
        print(username)
        answers = mocked_get_answers(username)
        return jsonify({"answers": answers})

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
    # question_ids = []
    # return jsonify({"question_ids": question_ids})

    questions = mocked_get_questions()
    return jsonify({"questions": questions})


# Method to check if a user exists and create them if they don't
@app.route("/user/<username>", methods=["PUT"])
def user_creation(username):
    if request.method == "PUT":
        user = mocked_user(username)

        if user == {}:
            # user doesn't exist

            return jsonify({"message": "User does not exist"}), 200

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

    print(data, file=sys.stderr)

    # Is this what you mean by sanitize? I am removing any leading/trailing whitespace
    if is_valid(username) and is_valid(password):
        user = mocked_user(username)
        print(user, file=sys.stderr)

        if not user == {} and user[1]["password"] == password:
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
        mocked_user_insert(username, password)

        return jsonify({"message": "User created"}), 200

    else:
        return jsonify({"message": "Invalid username or password format"}), 400
