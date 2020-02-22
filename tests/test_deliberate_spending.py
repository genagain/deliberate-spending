import pytest

from deliberate_spending import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert b"Click the button below to open a list of Institutions. After you select one, you'll be guided through an authentication process." in rv.data
