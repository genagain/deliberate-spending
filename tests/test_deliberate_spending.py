import json
import os
import pytest

from deliberate_spending import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# TODO make all of the testing API response based
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_get_access_token(client, monkeypatch):
    public_token = os.getenv('PUBLIC_TOKEN')
    data = { "public_token": public_token }
    response = client.post('/get_access_token', data=data)
    assert response.status_code == 200

