from roomee_api import app
from pytest import fixture

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
