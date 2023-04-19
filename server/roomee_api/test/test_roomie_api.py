from roomee_api import app
from pytest import fixture
import json


@fixture
def test_client():
    return app.test_client()


def test_get_users(test_client):
    # make a GET request to the `/users` endpoint
    response = test_client.get("/users")
    data = json.loads(response.data.decode())

    # check if response status code is 200 and contains bytes object
    assert response.status_code == 200
    assert type(data) == list


def test_post_users(test_client):
    # Create params for POST
    headers = {"Content-Type": "application/json"}
    payload = {"first_name": "name", "last_name": "name2", "gender": "female"}
    false_payload = {"user_id": 66}

    # Create POSTs
    response = test_client.post("/users", json=payload, headers=headers)
    data = json.loads(response.data.decode())

    false_response = test_client.post("/users", json=false_payload, headers=headers)
    false_data = json.loads(response.data.decode())

    # Good response and a True boolean
    assert response.status_code == 201  # Successful POST
    assert type(data) == dict

    # Bad response
    assert (
        false_response.status_code == 201
    )  # Successful POST, No payload schema implemented
    assert type(data) == dict


def test_post_questions(test_client):
    # Create params for POST
    headers = {"Content-Type": "application/json"}
    payload = {"question_id": 1, "user_id": 1234, "value": 13}
    false_payload = {"question_id": 66, "value": 13}

    # Create POSTs
    response = test_client.post("/questions", json=payload, headers=headers)
    data = json.loads(response.data.decode())

    false_response = test_client.post("/questions", json=false_payload, headers=headers)
    false_data = json.loads(false_response.data.decode())

    # Good response and a True boolean
    assert response.status_code == 201  # Successful POST
    assert type(data) == dict

    # Bad response
    assert false_response.status_code == 400  # Error
    assert false_data == {"error": "Missing parameter: user_id"}
