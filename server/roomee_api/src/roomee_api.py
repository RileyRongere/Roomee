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
            return jsonify({"user": user, "message": "Login successful."}), 200
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

        user = get_user(email)

        return jsonify({"user": user, "message": "User created"}), 200

    else:
        return jsonify({"message": "Invalid email or password format"}), 400


# Function to generate match in format frontend wants
def dumb_format(id):
    # The name was because I was frustrated. No personal offense should be taken.
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

    input_info = dumb_format(user_id)  # inputted person's question data

    matches = db_conn.query_matches(user_id)  # list of dicts
    # [{MatchID, UserID_1, UserID_2, PercentMatch}]

    # all_questions = db_conn.query_all_questions() #all questions for reference
    # [{QuestionID, Question}]

    # need to query answers for every user
    match_dict = {}
    for i in matches:
        curr_id = i["UserID_2"]  # current match id
        curr_match = dumb_format(curr_id)
        curr_match["matchScore"] = i["PercentMatch"]
        match_dict[curr_id] = curr_match

    return (
        jsonify({user_id: input_info, "matches": match_dict}),
        200,
    )  # as frontend desires
