import json
import os
import pytest

from deliberate_spending import app
from deliberate_spending.views import access_token

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# TODO make all of the testing API response based
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

# TODO test unhappy path for each API endpoint

# TODO test helper methods

def test_get_access_token(client):
    public_token = os.getenv('TEST_PUBLIC_TOKEN')
    data = { "public_token": public_token }
    response = client.post('/get_access_token', data=data)
    assert response.status_code == 200

def test_auth(client):
    access_token = os.getenv('TEST_ACCESS_TOKEN')
    response = client.get('/auth')
    assert response.status_code == 200

def test_transactions(client):
    access_token = os.getenv('TEST_ACCESS_TOKEN')
    response = client.get('/transactions')
    assert response.status_code == 200


