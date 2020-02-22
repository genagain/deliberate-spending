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
    assert b"Click the button below to open a list of Institutions. After you select one, you'll be guided through an authentication process." in response.data
