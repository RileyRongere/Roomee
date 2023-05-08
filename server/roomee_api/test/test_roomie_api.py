from roomee_api import app
from pytest import fixture
from unittest.mock import patch
import json


# test client
@fixture
def test_client():
    return app.test_client()


# test client POST headers
@fixture
def headers():
    return {"Content-Type": "application/json"}


# Integration tests for client-app interaction


# tests response code and data of one correct empty list named answer_ids (as function is implemented 4/27)
def test_get_answers(test_client, headers):
    post_response = test_client.post(
        "/answers/JohnDoe", json={"answer_id": 27}, headers=headers
    )
    response = test_client.get("/answers/JohnDoe")
    data = json.loads(response.data.decode())
    post_data = json.loads(post_response.data.decode())

    assert data["answer_ids"] == []
    assert response.status_code == 200

    assert post_data["answer_exists"] == True
    assert response.status_code == 200


# tests response for containing empty list
def test_get_questions(test_client, headers):
    response = test_client.get("/questions")
    data = json.loads(response.data.decode())

    assert data["question_ids"] == []
    assert response.status_code == 200


# tests that user_creation, was not able to patch the query_user from insert_query_DB file
def test_user_creation(test_client):
    response = test_client.put("/user/JohnDoe", json={})
    assert response.status == "500 INTERNAL SERVER ERROR"


# tests login, still cannot access/mock the table correctly, no test for sanitization or valid user
def test_login(test_client, headers):
    response = test_client.post("/login", headers=headers, json={})
    good_response = test_client.post(
        "/login", headers=headers, json={"username": "test", "password": "test"}
    )

    # Wrong data test
    assert response.status == "400 BAD REQUEST"


# tests registering users for given data not being correct, otherwise will throw DB error
def test_register_user(test_client, headers):
    # tests functionality of sanitization
    bad_data_response = test_client.post("/register", headers=headers, json={})

    assert bad_data_response.status_code == 400


# def test_get_users(test_client):
#     # make a GET request to the `/users` endpoint
#     response = test_client.get("/users")
#     data = json.loads(response.data.decode())

#     # check if response status code is 200 and contains bytes object
#     assert response.status_code == 200
#     assert data["user_ids"] == []


# # Tests if user exists using a both a valid and invalid id
# def test_check_user(test_client):
#     # Create params for POST
#     headers = {"Content-Type": "application/json"}
#     payload = {"user_id": 37}
#     false_payload = {"user_id": 66}

#     # Create POSTs
#     response = test_client.post("/users", json=payload, headers=headers)
#     data = json.loads(response.data.decode())

#     false_response = test_client.post("/users", json=false_payload, headers=headers)
#     false_data = json.loads(response.data.decode())

#     # Good response and a True boolean
#     assert response.status_code == 200
#     assert data["user_exists"]

#     # Good response and a False boolean
#     assert false_response.status_code == 200
#     assert false_data["user_exists"]


# def test_get_questions(test_client):
#     # make a GET request to the `/questions` endpoint
#     response = test_client.get("/questions")
#     data = json.loads(response.data.decode())

#     # check if response status code is 200 and contains bytes object
#     assert response.status_code == 200
#     assert data["question_ids"] == []


# def test_get_answers(test_client):
#     # make a GET request to the '/answers' endpoint
#     response = test_client.get("/answers")
#     data = json.loads(response.data.decode())

#     # check is response status code is 200 and contains bytes object
#     assert response.status_code == 200
#     assert data["answer_ids"] == []


# def test_check_answers(test_client):
#     # create params for POST
#     headers = {"Content-Type": "application/json"}
#     payload = {"answer_id": 27}
#     false_payload = {"answer_id": 40}

#     # create POSTs
#     response = test_client.post("/answers", json=payload, headers=headers)
#     data = json.loads(response.data.decode())

#     false_response = test_client.post("/answers", json=false_payload, headers=headers)
#     false_data = json.loads(response.data.decode())

#     # good response and True boolean
#     assert response.status_code == 200
#     assert data["answer_exists"]

#     # good response and False boolean
#     assert false_response.status_code == 200
#     assert false_data["answer_exists"]


# # tests user endpoint functionality
# def test_get_user_creation(test_client):
#     response = test_client.get("/user/False")
#     assert json.loads(response.data.decode()) == "False"
