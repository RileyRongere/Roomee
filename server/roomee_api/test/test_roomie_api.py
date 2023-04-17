from roomee_api import app
from pytest import fixture
import json

# test client
@fixture
def test_client():
    return app.test_client()


# Integration tests for client-app interaction

def test_hello_world(test_client):

    # create a test client
    #client = app.test_client()

    # make a GET request to the `/hello` endpoint
    response = test_client.get('/hello')

    # check if response status code is 200 and contains bytes object
    assert response.status_code == 200

    assert b'Hello, World!' in response.data


def test_get_users(test_client):

    # make a GET request to the `/users` endpoint
    response = test_client.get('/hello')

    # check if response status code is 200 and contains bytes object
    assert response.status_code == 200
    assert b'Hello, World!' in response.data

# Tests if user exists using a both a valid and invalid id
def test_check_user(test_client):

    # Create params for POST
    headers = {'Content-Type': 'application/json'}
    payload = {'user_id': 37}
    false_payload = {'user_id': 66}

    # Create POSTs
    response = test_client.post('/users', json=payload, headers=headers)
    data = json.loads(response.data.decode())

    false_response = test_client.post('/users', json=false_payload, headers=headers)
    false_data = json.loads(response.data.decode())

    # Good response and a True boolean
    assert response.status_code == 200
    assert data['user_exists']

    # Good response and a False boolean
    assert false_response.status_code == 200
    assert false_data['user_exists']
