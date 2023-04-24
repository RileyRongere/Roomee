from flask import Flask, request, jsonify
import os
import insert_query_DB

app = Flask(__name__)


# Method to return every user to the endpoint /api/users

#This probably doesn't need an endpoint associated with it. I don't think it will be called from outside the API -Kieran
@app.route("/users", methods=["GET"])
def get_users():
    # Mock list of user ids
    user_ids = []

    return jsonify({"user_ids": user_ids})


# Method to return a boolean to the endpoint /api/users if user_id exists

#Same as above. This probably won't be called from the outside and so doesn't really need an endpoint -Kieran
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


@app.route("/answers", methods=["GET", "POST"])
#I suspect this will need to be altered to take a username parameter so we know whose answers we're checking - Kieran
def get_answers():
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


# Check if user data is complete

#Another that might not need an endpoint -Kieran
@app.route("/user_is_complete/<username>", methods=["GET"])
def user_is_complete(username):
    # Mock user
    user = {"Joe": {"questions": []}}
    if username in user:
        completed = bool(user[username]["questions"])
        return jsonify({"is_completed": completed})
    else:
        return jsonify({"error": "User not found"})


# Method to return all questions to an endpoint /api/questions
@app.route("/questions", methods=["GET"])
def get_questions():
    question_ids = []
    return jsonify({"question_ids": question_ids})


# User methods endpoint, passes username as identifier
# Still creating handlers dependent on the state of the dictionary object from FE
@app.route("/user/<username>", methods=["GET", "POST"])
def user_creation(username):
    if request.method == "GET":
        # access DB to find user

        # if the user exists
        if username:
            user = {}
            # json object creation code here
            return jsonify(username)
        # else (username doesn't exist)
        else:
            return jsonify({"error": "User not found"}), 404

    elif request.method == "POST":
        # retrieve dictionary 
        username_request_object = request.get_json()
        # process dictionary from POST to figure out the task to perform on the given data
        # if completing a user's password setup (handler)
        Task = "user_creation"
        # if completing a user's answers (handler)
        Task = "answer_creation"

        return jsonify({"message": f"{Task} Complete"})

# DB method implementation      in-progress
@app.route("/test", methods=["POST"])
def test_user_create():
    user_details_object = request.get_json()
    print(user_details_object)
    #insert_user(user_details_object[])


    return jsonify("Made user.")