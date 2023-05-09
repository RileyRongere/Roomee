# test file

from flask import Flask, request, jsonify
import os
import json
import sys
from src.insert_query_DB import mySQL

# for dummy test
import mysql.connector

app = Flask(__name__)

# mockedDB for FE testing

# dummy endpoint for testing
@app.route("/dumb", methods=["GET"])
def dumb():
    conn = mysql.connector.connect(
        user="MYSQL_USER",
        password="MYSQL_PASSWORD",
        host="localhost",
        port="9906",
        database="roomee",
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USER")
    results = cursor.fetchall()

    return jsonify(results)


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

        return jsonify({"message": "Answers successfully posted"}), 201


# Method to return all questions to an endpoint /api/questions
@app.route("/questions", methods=["GET"])
def get_questions():
    db_conn = mySQL()
    if request.method == "GET":
        questions = db_conn.query_all_questions()
        return jsonify({"questions": questions}), 200


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
# users = {'username': 'password'}


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    # Is this what you mean by sanitize? I am removing any leading/trailing whitespace
    if is_valid(email) and is_valid(password):
        user = get_user(email)
        if not user == {} and user["password"] == password:
            return jsonify({"user": user, "message": "Login successful."}), 200
        else:
            return jsonify({"message": "Invalid email or password."}), 403

    else:
        return jsonify({"message": "Invalid email or password format"}), 400


# register endpoint to take in and save username and password
@app.route("/register", methods=["POST"])
def register_user():
    db_conn = mySQL()
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    # sanitize data
    db_conn.insert_user(email, password)

    user = get_user(email)

    return jsonify({"user": user, "message": "User created"}), 200

    # if is_valid(email) and is_valid(password):
    #     db_conn.insert_user(email, password)

    #     user = get_user(email)

    #     return jsonify({"user": user, "message": "User created"}), 200

    # else:
    #     return jsonify({"message": "Invalid email or password format"}), 400


# Function to generate match in format frontend wants
def match_format(id):
    db_conn = mySQL()
    qid = []  # temp question id
    question = []  # temp question
    answers = []  # temp answers

    curr_answers = db_conn.query_answer(id)  # list
    # [{AnswerID, UserID, QuestionID, Answer}]

    qid = [q["QuestionID"] for q in curr_answers]  # question IDs
    for j in qid:
        question.append(
            db_conn.query_question(j["QuestionID"])["Question"]
        )  # add question
        # this seems faster than iterating through the all_questions variable that
        # is commented out.

    answers = [q["Answer"] for q in curr_answers]  # answers

    return {
        "question_ids": qid,
        "questions": question,
        "answers": answers,
    }  # format frontend wants


# match endpoint
@app.route("/matches", methods=["GET"])
def get_matches():
    # should output in way depicted by frontend
    db_conn = mySQL()
    data = request.get_json()
    user_id = data.get("user_id")

    input_info = match_format(user_id)  # inputted person's question data

    matches = db_conn.query_matches(user_id)  # list of dicts
    # [{MatchID, UserID_1, UserID_2, PercentMatch}]

    # all_questions = db_conn.query_all_questions() #all questions for reference
    # [{QuestionID, Question}]

    # need to query answers for every user
    match_dict = {}
    for i in matches:
        curr_id = i["UserID_2"]  # current match id
        curr_match = match_format(curr_id)
        curr_match["matchScore"] = i["PercentMatch"]
        match_dict[curr_id] = curr_match

    return (
        jsonify({user_id: input_info, "matches": match_dict}),
        200,
    )  # as frontend desires
